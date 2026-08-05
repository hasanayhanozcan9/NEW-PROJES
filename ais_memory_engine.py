# ==============================================================================
# BIOKERNEL SOVEREIGN IP REGISTRY
# MODULE: ais_memory_engine.py (Core Engine)
# AUTHOR: Hasan Ayhan Özcan
# STATUS: PROPRIETARY & CONFIDENTIAL (100% FULL MODE)
# DESCRIPTION: Artificial Immune System memory for adaptive threat retention.
# ==============================================================================
import hashlib
import time
import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
import threading
import json

@dataclass
class ThreatAntibody:
    threat_hash: str
    generation_time: float
    neutralization_weight: np.ndarray
    clonal_lifespan: int = 1000
    affinity_score: float = 0.0
    mutation_history: List[float] = field(default_factory=list)

class AISMemoryEngine:
    def __init__(self, somatic_hypermutation_rate: float = 0.01, max_memory_cells: int = 100000):
        self.antibody_registry: Dict[str, ThreatAntibody] = {}
        self.mutation_rate = somatic_hypermutation_rate
        self.max_memory = max_memory_cells
        self.macrophage_queue = []
        self._lock = threading.Lock()
        self.owner_signature = "Hasan Ayhan Özcan - Sovereign AI"

    def _generate_epitope_hash(self, payload: bytes) -> str:
        hasher = hashlib.sha384()
        hasher.update(payload)
        hasher.update(self.owner_signature.encode('utf-8'))
        return hasher.hexdigest()

    def clonal_selection(self, threat_payload: bytes, affinity_matrix: np.ndarray) -> Tuple[bool, float]:
        epitope = self._generate_epitope_hash(threat_payload)
        with self._lock:
            if epitope in self.antibody_registry:
                current_affinity = self._affinity_maturation(epitope)
                return True, current_affinity
            self._generate_new_antibody(epitope, affinity_matrix)
            self._manage_memory_population()
            return False, 0.0

    def _generate_new_antibody(self, epitope: str, matrix: np.ndarray):
        weights = np.random.normal(loc=0.0, scale=self.mutation_rate, size=matrix.shape)
        antibody = ThreatAntibody(
            threat_hash=epitope,
            generation_time=time.time(),
            neutralization_weight=weights,
            affinity_score=0.1
        )
        self.antibody_registry[epitope] = antibody
        self.macrophage_queue.append(epitope)

    def _affinity_maturation(self, epitope: str) -> float:
        antibody = self.antibody_registry[epitope]
        antibody.clonal_lifespan += 500
        antibody.affinity_score = min(1.0, antibody.affinity_score + (self.mutation_rate * np.log(antibody.clonal_lifespan)))
        antibody.neutralization_weight *= (1 + (self.mutation_rate * antibody.affinity_score))
        antibody.mutation_history.append(antibody.affinity_score)
        return antibody.affinity_score

    def _manage_memory_population(self):
        if len(self.antibody_registry) > self.max_memory:
            sorted_antibodies = sorted(self.antibody_registry.items(), key=lambda x: (x[1].affinity_score, x[1].clonal_lifespan))
            cull_count = int(self.max_memory * 0.1)
            for i in range(cull_count):
                del self.antibody_registry[sorted_antibodies[i][0]]

    def export_immune_ledger(self) -> str:
        ledger = {k: {"lifespan": v.clonal_lifespan, "affinity": v.affinity_score} for k, v in self.antibody_registry.items()}
        return json.dumps(ledger, indent=4)
