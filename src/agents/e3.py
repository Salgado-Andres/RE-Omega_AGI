"""Neutral Agent e₃."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any

@dataclass
class E3Agent:
    name: str = "E3Agent"

    async def critique(self, data: Any) -> Any:
        await asyncio.sleep(0)
        logging.debug("E3Agent critiquing data: %s", data)
        return data
