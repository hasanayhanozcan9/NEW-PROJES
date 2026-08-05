# ==============================================================================
# BIOKERNEL SOVEREIGN IP REGISTRY
# MODULE: snn_biosensor.py (Core Engine)
# AUTHOR: Hasan Ayhan Özcan
# STATUS: PROPRIETARY & CONFIDENTIAL (100% FULL MODE)
# DESCRIPTION: Advanced LIF Spiking Neural Network base for biological transduction.
# ==============================================================================
import numpy as np
from typing import List, Tuple

class AdvancedLIFBiosensor:
    def __init__(self, v_th: float = -55.0, v_rest: float = -70.0, 
                 v_reset: float = -75.0, R_m: float = 1.2, tau_m: float = 20.0,
                 refractory_period: int = 2):
        self.v_th = v_th
        self.v_rest = v_rest
        self.v_reset = v_reset
        self.R_m = R_m
        self.tau_m = tau_m
        self.refractory_period = refractory_period
        self.v_mem = self.v_rest
        self.refractory_timer = 0
        self.spike_history: List[float] = []

    def inject_current(self, I_input: np.ndarray, dt: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
        time_steps = len(I_input)
        spikes = np.zeros(time_steps)
        v_trace = np.zeros(time_steps)
        
        for t in range(time_steps):
            if self.refractory_timer > 0:
                self.v_mem = self.v_reset
                self.refractory_timer -= 1
            else:
                dv = (-(self.v_mem - self.v_rest) + self.R_m * I_input[t]) * (dt / self.tau_m)
                self.v_mem += dv
                
                if self.v_mem >= self.v_th:
                    spikes[t] = 1.0
                    self.spike_history.append(t * dt)
                    self.v_mem = self.v_reset
                    self.refractory_timer = self.refractory_period
                    
            v_trace[t] = self.v_mem
        return spikes, v_trace

    def generate_ap_tcp_payload(self, spikes: np.ndarray) -> bytes:
        int_spikes = spikes.astype(np.uint8)
        packed = np.packbits(int_spikes)
        header = b'BIOK-SNN-V1'
        return header + packed.tobytes()
