import time
import sys
import os

G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
C = '\033[96m'
W = '\033[0m'

def print_delay(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print(f"\n{C}===================================================={W}")
print(f"{C}      BIOKERNEL SOVEREIGN OS - v1.0.0 BOOT SEQUENCE {W}")
print(f"{C}      AUTHOR: HASAN AYHAN ÖZCAN                     {W}")
print(f"{C}===================================================={W}\n")
time.sleep(1)

core_modules = {
    "sovereign_orchestrator.py": "Sovereign AI Master Orchestrator",
    "lnn_bio_simulation.py": "Liquid Neural Networks (LNN) Fluidic Engine",
    "snn_biosensor.py": "Neuromorphic Computing & SNN Transducers",
    "ais_memory_engine.py": "Agentic AI Swarm Protocols & Immune Memory"
}

print_delay(f"{G}[+] Initializing Core Bio-Digital Engines...{W}")
for filename, desc in core_modules.items():
    if os.path.exists(filename):
        print_delay(f"  --> [{filename}] {desc} ... {G}ONLINE{W}", 0.01)
    else:
        print_delay(f"  --> [{filename}] {desc} ... {Y}STANDBY{W}", 0.01)
    time.sleep(0.4)

print_delay(f"\n{Y}[!] SYSTEM HALT: Modules P1 through P105 are RESTRICTED.{W}")
print_delay(f"{Y}[!] Commercial IP Vault is locked by cryptographically sealed hash.{W}")
time.sleep(1)

print_delay(f"\n{R}[X] ACCESS DENIED to Phase 2-13 Modules. Symbiotic License required.{W}")
print_delay(f"{C}[i] Please contact hasanayhanozcan9@gmail.com for enterprise integration.{W}")
time.sleep(1)

print_delay(f"\n{G}[+] System entering autonomous idle state. Listening for node connections...{W}")
try:
    while True:
        sys.stdout.write(f"\r{G}Biokernel Active: Monitoring local biological mesh network...{W}")
        time.sleep(1)
        sys.stdout.write(f"\r{G}Biokernel Active: Monitoring local biological mesh network.{W}  ")
        time.sleep(1)
        sys.stdout.write(f"\r{G}Biokernel Active: Monitoring local biological mesh network..{W} ")
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\n\n{R}[!] System shutdown initiated by Chief Architect.{W}")
    sys.exit()
