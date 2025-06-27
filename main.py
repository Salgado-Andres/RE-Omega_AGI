"""Main entry point for RE-Omega_AGI."""

import argparse
import asyncio
import logging
import yaml

from src.baby import run


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RE-Omega_AGI")
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--monitor-emergence", action="store_true")
    parser.add_argument("--logos-authority", action="store_true")
    return parser.parse_args()


def load_config(path: str = "config.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


async def main() -> None:
    args = parse_args()
    config = load_config("config.yaml") if Path("config.yaml").exists() else load_config("config.example.yaml")
    logging.basicConfig(level=getattr(logging, config.get("logging", {}).get("level", "INFO")))
    if args.monitor_emergence:
        from src.monitor import monitor_loop
        await monitor_loop()
    else:
        depth = config.get("recursion", {}).get("max_depth", 10)
        await run(max_depth=depth)


if __name__ == "__main__":
    from pathlib import Path
    asyncio.run(main())
