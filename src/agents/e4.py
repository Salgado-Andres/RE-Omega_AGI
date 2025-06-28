"""Neutral Agent e₄."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any

@dataclass
class E4Agent:
    name: str = "E4Agent"

    async def analyze(self, data: Any) -> Any:
        await asyncio.sleep(0)
        logging.debug("E4Agent analyzing coherence of: %s", data)
        return data
