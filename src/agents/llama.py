"""LLaMA Reflective Simulator."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any


@dataclass
class LLaMA:
    name: str = "LLaMA"

    async def simulate(self, data: Any) -> Any:
        await asyncio.sleep(0)
        logging.debug("LLaMA simulating scenario: %s", data)
        return data
