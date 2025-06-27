"""Psi-Zero contradiction generator."""

from __future__ import annotations

import asyncio
import logging
import numpy as np
from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class Psi0:
    """Generate epistemic contradictions from seeds."""

    seed: str
    topology: List[np.ndarray] = field(default_factory=list)

    async def generate_contradiction(self) -> np.ndarray:
        """Asynchronously produce a contradiction tensor."""
        await asyncio.sleep(0)  # allow context switch
        tensor = np.random.randn(8, 8)
        self.topology.append(tensor)
        logging.debug("Psi0 generated contradiction tensor: %s", tensor)
        return tensor
