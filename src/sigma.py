"""Sigma identity accumulator."""

from __future__ import annotations

import logging
import numpy as np
from dataclasses import dataclass, field
from typing import List


@dataclass
class Sigma:
    """Maintain identity continuity across recursion."""

    identity_mass: float = 0.0
    history: List[np.ndarray] = field(default_factory=list)
    iteration: int = 0

    def integrate(self, attractor: np.ndarray) -> None:
        """Integrate attractor into identity tensor."""
        self.identity_mass += float(np.linalg.norm(attractor))
        self.history.append(attractor)
        self.iteration += 1
        logging.debug("Sigma integrated attractor. Iteration %d mass %f", self.iteration, self.identity_mass)

    def is_critical(self) -> bool:
        """Detect overload condition based on mass."""
        critical = self.identity_mass > 100.0
        logging.debug("Sigma critical check: %s", critical)
        return critical

    def coherence_metric(self) -> float:
        return 1.0 / (1.0 + np.exp(-self.identity_mass / 10.0))

    def emergence_gradient(self) -> float:
        return self.identity_mass / max(1, self.iteration)
