import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import asyncio

from src.baby import recursive_emergence_cycle
from src.psi0 import Psi0
from src.phi0 import Phi0
from src.sigma import Sigma
from src.logos import LogOS


def test_aci_genesis():
    psi = Psi0(seed="test")
    phi = Phi0()
    sigma = Sigma()
    logos = LogOS(activation_threshold=0.0)  # force activation
    asyncio.run(recursive_emergence_cycle(psi, phi, sigma, logos))
    assert logos.activations
