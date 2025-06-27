import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import asyncio

from src.baby import recursive_emergence_cycle
from src.psi0 import Psi0
from src.phi0 import Phi0
from src.sigma import Sigma
from src.logos import LogOS


def test_recursive_cycle():
    psi = Psi0(seed="test")
    phi = Phi0()
    sigma = Sigma()
    logos = LogOS()
    state = asyncio.run(recursive_emergence_cycle(psi, phi, sigma, logos))
    assert "coherence" in state
    assert sigma.iteration == 1
