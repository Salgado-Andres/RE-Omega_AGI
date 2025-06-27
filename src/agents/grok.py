"""Grok Spectral Critic."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any


@dataclass
class Grok:
    name: str = "Grok"

    async def critique(self, data: Any) -> Any:
        await asyncio.sleep(0)
        logging.debug("Grok critiquing data: %s", data)
        return data
