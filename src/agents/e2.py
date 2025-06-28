"""Neutral Agent e₂."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any

@dataclass
class E2Agent:
    name: str = "E2Agent"

    async def map(self, data: Any) -> Any:
        await asyncio.sleep(0)
        logging.debug("E2Agent mapping data: %s", data)
        return data
