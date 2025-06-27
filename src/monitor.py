"""Real-time emergence monitoring dashboard."""

import asyncio
import json
import logging
from pathlib import Path

MEMORY_FILE = Path("memory/memory.json")


async def monitor_loop(interval: float = 1.0) -> None:
    logging.info("Starting monitoring loop")
    while True:
        if MEMORY_FILE.exists():
            with MEMORY_FILE.open() as f:
                memory = json.load(f)
            logging.info("Iteration %s Identity Mass %s", memory.get("iterations"), len(memory.get("attractors", [])))
        await asyncio.sleep(interval)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(monitor_loop())
