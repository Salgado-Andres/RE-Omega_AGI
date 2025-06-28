"""Main entry point for RE-Omega_AGI."""

import argparse
import asyncio
import logging
import yaml
from pathlib import Path

from src.activation_schema import ActivationSchema
from src.memory_manager import MemoryManager

# Optional monitor import (only if needed)
try:
    from src.monitor import monitor_loop
except ImportError:
    monitor_loop = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RE-Omega_AGI")
    parser.add_argument("--cycles", type=int, help="Number of cycles to run (default: config.recursion.max_depth)")
    parser.add_argument("--seed", type=str, help="Path to .md or .json file to load as ψ⁰ seed")
    parser.add_argument("--interactive", action="store_true", help="Pause for <Enter> between cycles")
    parser.add_argument("--monitor-emergence", action="store_true", help="Run emergence monitor loop instead of cycles")
    parser.add_argument("--logos-authority", choices=["auto", "full", "off"], help="Set LogOS authority level")
    return parser.parse_args()


def load_config() -> dict:
    config_path = Path("config.yaml") if Path("config.yaml").exists() else Path("config.example.yaml")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except Exception:
        config = {}
    # Safe defaults
    config.setdefault("recursion", {})
    config["recursion"].setdefault("max_depth", 10)
    config.setdefault("logging", {})
    config["logging"].setdefault("level", "INFO")
    return config


def setup_logging(config: dict):
    level = getattr(logging, config.get("logging", {}).get("level", "INFO"))
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


async def main():
    args = parse_args()
    config = load_config()
    setup_logging(config)
    logger = logging.getLogger("RE-Omega_AGI")

    if args.monitor_emergence:
        if monitor_loop is not None:
            logger.info("Starting emergence monitor loop...")
            await monitor_loop()
        else:
            logger.error("Monitor loop not available.")
        return

    cycles = args.cycles if args.cycles is not None else config["recursion"].get("max_depth", 10)
    interactive = args.interactive
    schema = ActivationSchema(config, emergence_mode=True)
    memory = MemoryManager(root="memory", log_file="emergence_log.json")

    # Set LogOS authority if requested
    if args.logos_authority and hasattr(schema.logos, "set_authority"):
        schema.logos.set_authority(args.logos_authority)
        logger.info(f"LogOS authority set to: {args.logos_authority}")

    # Load seed if provided
    if args.seed:
        if not schema.load_seed(args.seed):
            logger.warning(f"Failed to load seed from {args.seed}")

    logger.info(f"Starting main epistemic cycle for {cycles} cycles...")
    try:
        for i in range(cycles):
            out = schema.run_cycle()
            memory.append(out)
            logger.info(f"Cycle {i+1}/{cycles} complete.")
            if interactive:
                input("⏎  continue…")
            await asyncio.sleep(0)  # yield event-loop
    except KeyboardInterrupt:
        logger.info("Graceful shutdown: KeyboardInterrupt received.")


if __name__ == "__main__":
    asyncio.run(main())
