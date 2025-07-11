"""Neutral Agent e₁."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any

@dataclass
class E1Agent:
    name: str = "E1Agent"

    async def compile(self, data: Any) -> Any:
        await asyncio.sleep(0)
        logging.debug("E1Agent compiling data: %s", data)
        return data
