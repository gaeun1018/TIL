from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple

import torch
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as T

CIFAR10_MEAN = (0.4914, 0.4822, 0.4465)
CIFAR10_STD  = (0.2023, 0.1994, 0.2010)

@dataclass
class DataConfig:
    data_dir: str = "./data"
    batch_size: int = 128
    test_batch_size: int = 256
    num_workers: int = 2
    pin_memory: bool = True
    augment: bool = True
    normalize: bool = True

def build_transforms(train: bool, augment: bool, normalize: bool):
    tfms = []
    if train and augment:
        tfms += [
            T.RandomCrop(32, padding=4),
            T.RandomHorizontalFlip(),
        ]
    tfms.append(T.ToTensor())
    if normalize:
        tfms.append(T.Normalize(CIFAR10_MEAN, CIFAR10_STD))
    return T.Compose(tfms)

def make_loaders(cfg: DataConfig):
    train_t = build_transforms(train=True, augment=cfg.augment, normalize=cfg.normalize)
    test_t  = build_transforms(train=False, augment=False, normalize=cfg.normalize)

    trainset = torchvision.datasets.CIFAR10(root=cfg.data_dir, train=True, download=True, transform=train_t)
    testset  = torchvision.datasets.CIFAR10(root=cfg.data_dir, train=False, download=True, transform=test_t)

    trainloader = DataLoader(
        trainset,
        batch_size=cfg.batch_size,
        shuffle=True,
        num_workers=cfg.num_workers,
        pin_memory=cfg.pin_memory,
    )
    testloader = DataLoader(
        testset,
        batch_size=cfg.test_batch_size,
        shuffle=False,
        num_workers=cfg.num_workers,
        pin_memory=cfg.pin_memory,
    )
    return trainloader, testloader, trainset.classes
