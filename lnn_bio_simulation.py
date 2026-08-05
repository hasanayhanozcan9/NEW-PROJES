# ==============================================================================
# BIOKERNEL SOVEREIGN IP REGISTRY
# MODULE: lnn_bio_simulation.py (Core Engine)
# AUTHOR: Hasan Ayhan Özcan
# STATUS: PROPRIETARY & CONFIDENTIAL (100% FULL MODE)
# DESCRIPTION: Core Liquid Neural Network simulation for fluidic environments.
# ==============================================================================
import torch
import torch.nn as nn
import torch.nn.functional as F

class LiquidTimeConstantNode(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, unfolding_steps: int = 6):
        super(LiquidTimeConstantNode, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.unfolding_steps = unfolding_steps
        self.w_in = nn.Linear(input_dim, hidden_dim)
        self.w_rec = nn.Linear(hidden_dim, hidden_dim)
        self.tau_sys = nn.Parameter(torch.Tensor(hidden_dim).uniform_(0.1, 1.0))
        self.c_m = nn.Parameter(torch.ones(hidden_dim))
        self.g_leak = nn.Parameter(torch.ones(hidden_dim) * 0.05)
        self.v_rest = nn.Parameter(torch.zeros(hidden_dim))

    def _compute_dynamic_tau(self, x: torch.Tensor, h: torch.Tensor) -> torch.Tensor:
        synaptic_drive = F.silu(self.w_in(x) + self.w_rec(h))
        return self.tau_sys / (self.c_m + self.g_leak + synaptic_drive + 1e-8)

    def _ode_solver(self, x_t: torch.Tensor, h_prev: torch.Tensor, delta_t: float) -> torch.Tensor:
        h_current = h_prev
        dt_step = delta_t / self.unfolding_steps
        for _ in range(self.unfolding_steps):
            tau_t = self._compute_dynamic_tau(x_t, h_current)
            synaptic_input = torch.tanh(self.w_in(x_t))
            dh_dt = - (h_current - self.v_rest) / tau_t + synaptic_input
            h_current = h_current + dh_dt * dt_step
        return h_current

    def forward(self, x_t: torch.Tensor, h_prev: torch.Tensor, delta_t: float) -> torch.Tensor:
        return self._ode_solver(x_t, h_prev, delta_t)

class LNNBioSimulator(nn.Module):
    def __init__(self, sensors: int, neurons: int, output_dim: int):
        super(LNNBioSimulator, self).__init__()
        self.liquid_node = LiquidTimeConstantNode(sensors, neurons)
        self.readout = nn.Linear(neurons, output_dim)
        self._init_weights()

    def _init_weights(self):
        nn.init.xavier_uniform_(self.liquid_node.w_in.weight)
        nn.init.orthogonal_(self.liquid_node.w_rec.weight)

    def forward(self, bio_data_stream: torch.Tensor, dt=0.01):
        batch_size, seq_len, _ = bio_data_stream.shape
        h_state = torch.zeros(batch_size, self.liquid_node.hidden_dim, device=bio_data_stream.device)
        outputs = []
        for t in range(seq_len):
            h_state = self.liquid_node(bio_data_stream[:, t, :], h_state, dt)
            outputs.append(h_state.unsqueeze(1))
        liquid_states = torch.cat(outputs, dim=1)
        final_prediction = self.readout(liquid_states)
        return final_prediction
