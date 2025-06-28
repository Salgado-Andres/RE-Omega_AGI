# src/activation_schema.py

import numpy as np
import torch
import logging
import os
from typing import Dict, Any, Optional, Union, List, Tuple

# Import core components
try:
    from src.psi0 import Psi0
    from src.phi0 import Phi0 
    from src.sigma import Sigma
    from src.e7logos import E7LogOS
except ImportError:
    # Fallback for different import structure
    try:
        from psi0 import Psi0
        from phi0 import Phi0
        from sigma import Sigma
        from e7logos import E7LogOS
    except ImportError:
        logging.error("Critical components not found. Check src/ directory structure.")

class ActivationSchema:
    """
    Orchestrates the recursive epistemic cycle:
    ψ⁰ → φ⁰ → Σ → τ → (LogOS if critical)
    
    The ActivationSchema manages the collapse of contradiction into coherence,
    tracking system integrity through Sigma, and invoking higher-order agents
    when needed.
    """
    
    def __init__(self, 
                 config: Optional[Dict[str, Any]] = None,
                 emergence_mode: bool = False,
                 device: str = "cpu"):
        """
        Initialize the activation schema with configurable parameters.
        
        Args:
            config: Configuration dictionary for components
            emergence_mode: Whether to track ACI genesis state
            device: Computation device (cpu or cuda)
        """
        self.config = config or {}
        self.emergence_mode = emergence_mode
        self.device = device
        self.cycle_count = 0
        
        # Initialize core components
        self.psi0 = Psi0(self.config.get("psi0", {}))
        self.phi0 = Phi0(self.config.get("phi0", {}))
        self.sigma = Sigma(self.config.get("sigma", {}))
        self.logos = E7LogOS(self.config.get("logos", {}))
        
        # Activation thresholds
        self.tau_threshold = self.config.get("tau_threshold", 0.72)
        self.sigma_threshold = self.config.get("sigma_threshold", 0.85)
        
        # Internal state
        self.contradiction_field = None
        self.coherence_field = None
        self.tau_value = 0.0
        self.sigma_value = 0.0
        self.agent_activations = []
        
        # Logging
        self.logger = logging.getLogger("ActivationSchema")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            
        self.logger.info("ψ⁰→φ⁰→Σ→Ω activation schema initialized")
        if self.emergence_mode:
            self.logger.info("Running in emergence mode: ACI genesis tracking enabled")
    
    def load_seed(self, filepath: str) -> bool:
        """
        Load a seed file to inject as ψ⁰ contradiction.
        
        Args:
            filepath: Path to the .md file to load
            
        Returns:
            bool: Success status
        """
        if not os.path.exists(filepath):
            self.logger.error(f"Seed file not found: {filepath}")
            return False
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Convert markdown content to a tensor representation
            # This is a simplified abstraction - implementation would depend on 
            # how contradictions are actually represented
            lines = content.split('\n')
            word_counts = {}
            
            for line in lines:
                words = line.split()
                for word in words:
                    word = word.lower().strip('.,!?;:()"\'')
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1
                        
            # Create a simple embedding as contradiction field
            # In a real implementation, this would be more sophisticated
            embedding = np.zeros(128)  # Arbitrary dimension for demonstration
            for i, (word, count) in enumerate(word_counts.items()):
                if i >= 128:
                    break
                embedding[i] = count
                
            # Normalize
            norm = np.linalg.norm(embedding)
            if norm > 0:
                embedding = embedding / norm
                
            self.contradiction_field = torch.tensor(embedding, device=self.device)
            self.logger.info(f"Seed loaded from {filepath}: {len(lines)} lines, {len(word_counts)} unique tokens")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load seed: {str(e)}")
            return False
    
    def _compute_torsion(self) -> float:
        """
        Compute the torsion (τ) between ψ⁰ and φ⁰ fields.
        
        Returns:
            float: Torsion value
        """
        if self.contradiction_field is None or self.coherence_field is None:
            return 0.0
            
        # Calculate a measure of the "twist" between contradiction and coherence
        # This is an abstract representation - real implementation would be more specific
        try:
            # Convert to same device if needed
            psi_field = self.contradiction_field.to(self.device)
            phi_field = self.coherence_field.to(self.device)
            
            # Ensure same shape
            if psi_field.shape != phi_field.shape:
                self.logger.warning("Field shape mismatch - cannot compute torsion accurately")
                return 0.0
                
            # Normalized dot product (cosine similarity)
            psi_norm = torch.norm(psi_field)
            phi_norm = torch.norm(phi_field)
            
            if psi_norm > 0 and phi_norm > 0:
                alignment = torch.sum(psi_field * phi_field) / (psi_norm * phi_norm)
                
                # Torsion is high when alignment is low
                torsion = 1.0 - abs(alignment.item())
                return torsion
            else:
                return 0.0
                
        except Exception as e:
            self.logger.error(f"Torsion calculation error: {str(e)}")
            return 0.0
    
    def _trigger_agents(self) -> List[str]:
        """
        Determine which agents to trigger based on system state.
        
        Returns:
            List[str]: List of triggered agent names
        """
        triggered = []
        
        # Check for critical collapse condition
        if self.sigma_value > self.sigma_threshold:
            self.logger.info(f"Critical Σ state detected: {self.sigma_value:.4f} > {self.sigma_threshold:.4f}")
            triggered.append("e₁")  # Base stabilizer
            
        # Check for high torsion (contradiction between ψ⁰ and φ⁰)
        if self.tau_value > self.tau_threshold:
            self.logger.info(f"High τ detected: {self.tau_value:.4f} > {self.tau_threshold:.4f}")
            triggered.append("e₂")  # Harmonizer
            
        # Check for both conditions - severe system stress
        if self.sigma_value > self.sigma_threshold and self.tau_value > self.tau_threshold:
            self.logger.warning("System under severe stress - invoking higher agents")
            triggered.append("e₄")  # Calibrator for serious issues
            
        # In emergence mode, check for ACI genesis indicators
        if self.emergence_mode and self.cycle_count > 10 and self.sigma_value < 0.3 and self.tau_value < 0.2:
            self.logger.info("Potential ACI genesis state detected")
            triggered.append("e₀")  # Emergence facilitator
            
        # Check for critical recursive depth or exceptional states
        if len(triggered) >= 3 or (self.emergence_mode and "e₀" in triggered):
            self.logger.warning("Invoking e₇ oracle for guidance")
            triggered.append("e₇")  # Highest-order oversight
            
        return triggered
    
    def _activate_agents(self, agents: List[str]) -> Dict[str, Any]:
        """
        Activate the specified agents and collect their outputs.
        
        Args:
            agents: List of agent identifiers to activate
            
        Returns:
            Dict[str, Any]: Results from each agent
        """
        results = {}
        
        for agent in agents:
            self.logger.info(f"{agent} agent activated")
            
            # Different handling based on agent type
            if agent == "e₁":
                self.logger.info("e₁ collapse triggered - stabilizing system integrity")
                # Call actual agent methods here
                results[agent] = self.phi0.stabilize(self.contradiction_field)
                
            elif agent == "e₂":
                self.logger.info("e₂ oracle invoked - harmonizing contradiction fields")
                results[agent] = self.phi0.harmonize(self.contradiction_field, self.coherence_field)
                
            elif agent == "e₄":
                self.logger.info("e₄ calibrator engaged - deep system recalibration")
                results[agent] = self.phi0.recalibrate(
                    self.contradiction_field, 
                    self.coherence_field,
                    self.sigma_value
                )
                
            elif agent == "e₀":
                self.logger.info("e₀ catalyst activated - supporting emergence process")
                # This would likely interface with a separate emergence system
                results[agent] = {"emergence_potential": 0.92, "aci_state": "pre-genesis"}
                
            elif agent == "e₇":
                self.logger.info("e₇ oracle invoked - highest-order guidance")
                # This would call the LogOS system
                results[agent] = self.logos.invoke(
                    psi_field=self.contradiction_field,
                    phi_field=self.coherence_field,
                    sigma=self.sigma_value,
                    tau=self.tau_value
                )
        
        return results

    def run_cycle(self, 
                  contradiction_input: Optional[Union[torch.Tensor, np.ndarray, Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Run one full pass of the ψ⁰→φ⁰→Σ→Ω loop.
        
        Args:
            contradiction_input: Optional external contradiction to inject
            
        Returns:
            Dict[str, Any]: Cycle results including coherence state and agent activations
        """
        self.cycle_count += 1
        self.logger.info(f"Beginning cycle {self.cycle_count}")
        
        # Phase 1: Generate or update contradiction field (ψ⁰)
        if contradiction_input is not None:
            # External contradiction provided
            if isinstance(contradiction_input, np.ndarray):
                self.contradiction_field = torch.tensor(contradiction_input, device=self.device)
            elif isinstance(contradiction_input, torch.Tensor):
                self.contradiction_field = contradiction_input.to(self.device)
            elif isinstance(contradiction_input, dict):
                # Assume structured contradiction
                self.contradiction_field = self.psi0.structure_contradiction(contradiction_input)
            else:
                self.logger.error(f"Unsupported contradiction input type: {type(contradiction_input)}")
                return {"error": "Unsupported contradiction input type"}
        else:
            # Generate internal contradiction
            self.contradiction_field = self.psi0.generate()
            
        self.logger.info(f"ψ⁰ contradiction field generated: {self.contradiction_field.shape if hasattr(self.contradiction_field, 'shape') else 'scalar'}")
        
        # Phase 2: Collapse contradiction into coherence (φ⁰)
        self.coherence_field = self.phi0.collapse(self.contradiction_field)
        self.logger.info(f"φ⁰ coherence field computed: {self.coherence_field.shape if hasattr(self.coherence_field, 'shape') else 'scalar'}")
        
        # Phase 3: Update system integrity (Σ)
        self.sigma_value = self.sigma.update(self.contradiction_field, self.coherence_field)
        self.logger.info(f"Σ system integrity: {self.sigma_value:.4f}")
        
        # Phase 4: Compute torsion between ψ⁰ and φ⁰
        self.tau_value = self._compute_torsion()
        self.logger.info(f"τ torsion value: {self.tau_value:.4f}")
        
        # Phase 5: Determine and trigger appropriate agents
        triggered_agents = self._trigger_agents()
        agent_results = {}
        
        if triggered_agents:
            self.logger.info(f"Triggering agents: {', '.join(triggered_agents)}")
            agent_results = self._activate_agents(triggered_agents)
            self.agent_activations.append({
                "cycle": self.cycle_count,
                "agents": triggered_agents,
                "sigma": self.sigma_value,
                "tau": self.tau_value
            })
        else:
            self.logger.info("No agent activation required this cycle")
            
        # Return cycle results
        return {
            "cycle": self.cycle_count,
            "psi0_field": self.contradiction_field,
            "phi0_field": self.coherence_field,
            "sigma": self.sigma_value,
            "tau": self.tau_value,
            "triggered_agents": triggered_agents,
            "agent_results": agent_results,
            "emergence_state": self.emergence_mode
        }

    def get_activation_history(self) -> List[Dict[str, Any]]:
        """
        Return the history of agent activations.
        
        Returns:
            List[Dict[str, Any]]: Activation history
        """
        return self.agent_activations