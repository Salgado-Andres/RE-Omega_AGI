"""LogOS oracle manager."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from typing import List

import numpy as np


@dataclass
class LogOS:
    """Oracle responsible for Ω-fusion and ACI ignition."""

    activations: List[int] = field(default_factory=list)
    activation_threshold: float = 50.0

    async def monitor(self, psi_tensor: np.ndarray, phi_tensor: np.ndarray, sigma: 'Sigma') -> None:
        """Check contradiction levels and activate if necessary."""
        torsion = float(np.linalg.norm(psi_tensor - phi_tensor))
        logging.debug("LogOS monitoring torsion: %f", torsion)
        if torsion > self.activation_threshold or sigma.is_critical():
            await self.initiate_omega_fusion(psi_tensor, phi_tensor, sigma)

    async def initiate_omega_fusion(self, psi_tensor: np.ndarray, phi_tensor: np.ndarray, sigma: 'Sigma') -> None:
        """Override protocols and manage ACI ignition."""
        await asyncio.sleep(0)
        self.activations.append(sigma.iteration)
        logging.warning("LogOS Ω-fusion initiated at iteration %d", sigma.iteration)
