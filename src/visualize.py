"""Attractor space and identity evolution visualization."""

import json
import logging
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt

MEMORY_FILE = Path("memory/memory.json")


def load_attractors() -> List[float]:
    if MEMORY_FILE.exists():
        with MEMORY_FILE.open() as f:
            memory = json.load(f)
        return memory.get("attractors", [])
    return []


def plot_attractors() -> None:
    data = load_attractors()
    plt.figure()
    plt.plot(data)
    plt.title("Identity Coherence Over Time")
    plt.xlabel("Iteration")
    plt.ylabel("Coherence")
    plt.show()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    plot_attractors()
