from __future__ import annotations
import argparse
from typing import Tuple

import torch
import torch.nn as nn
import torch.optim as optim

from data import DataConfig, make_loaders
from model import SimpleCNN
from utils import set_seed, save_checkpoint

def parse_args():
    p = argparse.ArgumentParser(description="Train CIFAR-10 classifier (SimpleCNN).")
    p.add_argument("--epochs", type=int, default=120)
    p.add_argument("--seed", type=int, default=42)

    # data
    p.add_argument("--data_dir", type=str, default="./data")
    p.add_argument("--batch_size", type=int, default=128)
    p.add_argument("--test_batch_size", type=int, default=256)
    p.add_argument("--num_workers", type=int, default=2)
    p.add_argument("--no_pin_memory", action="store_true")
    p.add_argument("--no_augment", action="store_true")
    p.add_argument("--no_normalize", action="store_true")

    # model
    p.add_argument("--use_bn", action="store_true")
    p.add_argument("--dropout", type=float, default=0.0)

    # optimization
    p.add_argument("--optimizer", choices=["sgd", "adam"], default="sgd")
    p.add_argument("--lr", type=float, default=None, help="If omitted, uses a sensible default per optimizer.")
    p.add_argument("--momentum", type=float, default=0.9)
    p.add_argument("--weight_decay", type=float, default=5e-4)
    p.add_argument("--label_smoothing", type=float, default=0.05)

    # scheduler
    p.add_argument("--scheduler", choices=["none", "multistep", "cosine"], default="multistep")
    p.add_argument("--milestones", type=str, default="60,120", help="Comma-separated epochs for MultiStepLR.")
    p.add_argument("--gamma", type=float, default=0.2)

    # output
    p.add_argument("--ckpt_dir", type=str, default="./checkpoints")
    p.add_argument("--ckpt_name", type=str, default="best.pt")
    return p.parse_args()

def make_optimizer(args, model: nn.Module):
    if args.optimizer == "adam":
        lr = args.lr if args.lr is not None else 1e-3
        return optim.Adam(model.parameters(), lr=lr, weight_decay=args.weight_decay)
    else:
        lr = args.lr if args.lr is not None else 0.1
        return optim.SGD(
            model.parameters(),
            lr=lr,
            momentum=args.momentum,
            weight_decay=args.weight_decay,
            nesterov=True,
        )

def make_scheduler(args, optimizer):
    if args.scheduler == "none":
        return None
    if args.scheduler == "cosine":
        return optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    # multistep
    milestones = [int(x.strip()) for x in args.milestones.split(",") if x.strip()]
    return optim.lr_scheduler.MultiStepLR(optimizer, milestones=milestones, gamma=args.gamma)

def run_epoch(model, loader, criterion, optimizer=None, device="cpu"):
    train_mode = optimizer is not None
    model.train(train_mode)

    total, correct, loss_sum = 0, 0, 0.0
    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        if train_mode:
            optimizer.zero_grad(set_to_none=True)

        logits = model(images)
        loss = criterion(logits, labels)

        if train_mode:
            loss.backward()
            optimizer.step()

        loss_sum += loss.item() * labels.size(0)
        pred = logits.argmax(dim=1)
        correct += (pred == labels).sum().item()
        total += labels.size(0)

    return loss_sum / total, correct / total

def main():
    args = parse_args()
    set_seed(args.seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    data_cfg = DataConfig(
        data_dir=args.data_dir,
        batch_size=args.batch_size,
        test_batch_size=args.test_batch_size,
        num_workers=args.num_workers,
        pin_memory=not args.no_pin_memory,
        augment=not args.no_augment,
        normalize=not args.no_normalize,
    )
    trainloader, testloader, classes = make_loaders(data_cfg)

    model = SimpleCNN(use_bn=args.use_bn, dropout=args.dropout).to(device)

    criterion = nn.CrossEntropyLoss(label_smoothing=args.label_smoothing)

    optimizer = make_optimizer(args, model)
    scheduler = make_scheduler(args, optimizer)

    best_acc = 0.0
    ckpt_path = f"{args.ckpt_dir.rstrip('/')}/{args.ckpt_name}"

    for epoch in range(1, args.epochs + 1):
        tr_loss, tr_acc = run_epoch(model, trainloader, criterion, optimizer=optimizer, device=device)
        te_loss, te_acc = run_epoch(model, testloader,  criterion, optimizer=None,      device=device)

        if scheduler is not None:
            scheduler.step()

        if te_acc > best_acc:
            best_acc = te_acc
            save_checkpoint(ckpt_path, model, extra={"best_acc": best_acc, "epoch": epoch, "args": vars(args)})

        lr_now = optimizer.param_groups[0]["lr"]
        print(
            f"[{epoch:03d}/{args.epochs}] "
            f"lr={lr_now:.5f} | "
            f"train loss/acc {tr_loss:.4f}/{tr_acc:.3f} | "
            f"test loss/acc {te_loss:.4f}/{te_acc:.3f} | "
            f"best {best_acc:.3f}"
        )

    print(f"Done. Best test accuracy: {best_acc*100:.2f}%")
    print(f"Saved best checkpoint to: {ckpt_path}")

if __name__ == "__main__":
    main()
