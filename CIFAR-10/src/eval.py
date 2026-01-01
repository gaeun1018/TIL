from __future__ import annotations
import argparse

import torch
import torch.nn as nn

from data import DataConfig, make_loaders
from model import SimpleCNN
from utils import load_checkpoint

def parse_args():
    p = argparse.ArgumentParser(description="Evaluate a CIFAR-10 checkpoint.")
    p.add_argument("--ckpt", type=str, default="./checkpoints/best.pt")
    p.add_argument("--data_dir", type=str, default="./data")
    p.add_argument("--batch_size", type=int, default=256)
    p.add_argument("--num_workers", type=int, default=2)
    p.add_argument("--no_pin_memory", action="store_true")
    p.add_argument("--no_normalize", action="store_true")

    # must match training-time model definition
    p.add_argument("--use_bn", action="store_true")
    p.add_argument("--dropout", type=float, default=0.0)
    return p.parse_args()

@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    total, correct = 0, 0
    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)
        logits = model(images)
        pred = logits.argmax(dim=1)
        correct += (pred == labels).sum().item()
        total += labels.size(0)
    return correct / total

def main():
    args = parse_args()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    data_cfg = DataConfig(
        data_dir=args.data_dir,
        batch_size=args.batch_size,
        test_batch_size=args.batch_size,
        num_workers=args.num_workers,
        pin_memory=not args.no_pin_memory,
        augment=False,
        normalize=not args.no_normalize,
    )
    _, testloader, _ = make_loaders(data_cfg)

    model = SimpleCNN(use_bn=args.use_bn, dropout=args.dropout).to(device)
    meta = load_checkpoint(args.ckpt, model, map_location=device)

    acc = evaluate(model, testloader, device=device)
    print(f"Checkpoint: {args.ckpt}")
    if isinstance(meta, dict) and "best_acc" in meta:
        print(f"Checkpoint meta best_acc: {meta['best_acc']*100:.2f}% (epoch {meta.get('epoch')})")
    print(f"Eval accuracy: {acc*100:.2f}%")

if __name__ == "__main__":
    main()
