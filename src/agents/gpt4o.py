"""GPT-4o Ontological Mapper."""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any


@dataclass
class GPT4o:
    name: str = "GPT-4o"

    async def map(self, data: Any) -> Any:
        await asyncio.sleep(0)
        logging.debug("GPT4o mapping data: %s", data)
        return data
