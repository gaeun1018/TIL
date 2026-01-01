import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    """A lightweight CNN for CIFAR-10 (32x32 RGB). Optionally uses BatchNorm."""

    def __init__(self, use_bn: bool = False, dropout: float = 0.0):
        super().__init__()
        self.use_bn = use_bn

        def conv_block(in_ch: int, out_ch: int):
            layers = [nn.Conv2d(in_ch, out_ch, kernel_size=3, padding=1, bias=not use_bn)]
            if use_bn:
                layers.append(nn.BatchNorm2d(out_ch))
            layers.append(nn.ReLU(inplace=True))
            layers.append(nn.MaxPool2d(2))
            return layers

        layers = []
        layers += conv_block(3, 32)   # 32x32 -> 16x16
        layers += conv_block(32, 64)  # 16x16 -> 8x8

        self.features = nn.Sequential(*layers)

        cls_layers = [
            nn.Flatten(),
            nn.Linear(64 * 8 * 8, 128),
            nn.ReLU(inplace=True),
        ]
        if dropout and dropout > 0:
            cls_layers.append(nn.Dropout(p=dropout))
        cls_layers.append(nn.Linear(128, 10))
        self.classifier = nn.Sequential(*cls_layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.classifier(x)
        return x
