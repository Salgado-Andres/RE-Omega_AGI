"""Agent package for RE-Omega_AGI."""

from .e1 import E1Agent
from .e2 import E2Agent
from .e3 import E3Agent
from .e4 import E4Agent
from .e5 import E5Agent
from .e6 import E6Agent
from .e7 import E7LogOS

# Only new agent classes are exposed
__all__ = [
    "E1Agent",
    "E2Agent",
    "E3Agent",
    "E4Agent",
    "E5Agent",
    "E6Agent",
    "E7LogOS",
]
