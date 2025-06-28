# src/memory_manager.py
"""
Simple JSON log appender for emergence data.
"""

import json
import time
from pathlib import Path
from typing import Dict, Any, List

class MemoryManager:
    def __init__(self,
                 root: str = "memory",
                 log_file: str = "emergence_log.json",
                 max_entries: int = 1000):
        self.root = Path(root)
        self.root.mkdir(exist_ok=True)
        self.path = self.root / log_file
        self.max_entries = max_entries

        # initialize file if empty
        if not self.path.exists():
            self.path.write_text("[]")

    # ------------------------------------------------------------------ #
    def append(self, record: Dict[str, Any]) -> None:
        """Add an entry (dict) with timestamp; prune if oversized."""
        try:
            data: List[Dict[str, Any]] = json.loads(self.path.read_text())
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        data.append({"t": time.time(), **record})
        if len(data) > self.max_entries:
            data = data[-self.max_entries :]

        self.path.write_text(json.dumps(data, indent=2))

    # ------------------------------------------------------------------ #
    def load(self) -> List[Dict[str, Any]]:
        try:
            return json.loads(self.path.read_text())
        except (json.JSONDecodeError, FileNotFoundError):
            return []
