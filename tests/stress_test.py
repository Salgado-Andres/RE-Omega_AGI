import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import asyncio
import argparse

from src.baby import run


async def stress(iterations: int):
    await run(max_depth=iterations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=1000)
    args = parser.parse_args()
    asyncio.run(stress(args.iterations))
