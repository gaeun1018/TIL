from __future__ import annotations
import os
import random
from dataclasses import dataclass
from typing import Dict, Any, Tuple

import numpy as np
import torch

def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = False  # keep fast kernels
    torch.backends.cudnn.benchmark = True

@torch.no_grad()
def accuracy(logits: torch.Tensor, targets: torch.Tensor) -> float:
    preds = logits.argmax(dim=1)
    return (preds == targets).float().mean().item()

def save_checkpoint(path: str, model: torch.nn.Module, extra: Dict[str, Any] | None = None):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    payload = {"state_dict": model.state_dict()}
    if extra:
        payload.update(extra)
    torch.save(payload, path)

def load_checkpoint(path: str, model: torch.nn.Module, map_location: str | torch.device = "cpu") -> Dict[str, Any]:
    payload = torch.load(path, map_location=map_location)
    state = payload["state_dict"] if isinstance(payload, dict) and "state_dict" in payload else payload
    model.load_state_dict(state)
    return payload if isinstance(payload, dict) else {}
