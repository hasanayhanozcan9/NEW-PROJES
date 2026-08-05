import gradio as gr
import time
import os

core_modules = {
    "sovereign_orchestrator.py": "Sovereign AI Master Orchestrator",
    "lnn_bio_simulation.py": "Liquid Neural Networks (LNN) Fluidic Engine",
    "snn_biosensor.py": "Neuromorphic Computing & SNN Transducers",
    "ais_memory_engine.py": "Agentic AI Swarm Protocols & Immune Memory",
}

def boot_sequence():
    log_text = ""
    
    # Başlık simülasyonu
    log_text += "====================================================\n"
    log_text += "      BIOKERNEL SOVEREIGN OS - v1.0.0 BOOT SEQUENCE \n"
    log_text += "      AUTHOR: HASAN AYHAN ÖZCAN                     \n"
    log_text += "====================================================\n\n"
    yield log_text
    time.sleep(1)

    # Modül kontrolü
    log_text += "[+] Initializing Core Bio-Digital Engines...\n"
    yield log_text

    for filename, desc in core_modules.items():
        if os.path.exists(filename):
            log_text += f"  --> [{filename}] {desc} ... ONLINE\n"
        else:
            log_text += f"  --> [{filename}] {desc} ... STANDBY\n"
        yield log_text
        time.sleep(0.4)

    # Kısıtlama ve uyarılar
    log_text += "\n[!] SYSTEM HALT: Modules P1 through P105 are RESTRICTED.\n"
    log_text += "[!] Commercial IP Vault is locked by cryptographically sealed hash.\n"
    yield log_text
    time.sleep(1)

    log_text += "\n[X] ACCESS DENIED to Phase 2-13 Modules. Symbiotic License required.\n"
    log_text += "[i] Please contact hasanayhanozcan9@gmail.com for enterprise integration.\n"
    yield log_text
    time.sleep(1)

    # Kapanış
    log_text += "\n[+] System entering autonomous idle state. Biokernel Active: Monitoring local biological mesh network...\n"
    yield log_text

# Siyah-Beyaz Hacker temasıyla arayüzü oluştur
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🧬 BIOKERNEL: THE SOVEREIGN BIO-DIGITAL ECOSYSTEM & IP REGISTRY")
    gr.Markdown("### AUTHOR: HASAN AYHAN ÖZCAN")
    gr.Markdown("---")
    
    gr.Markdown("Click the button below to launch the sovereign system boot sequence live in the browser.")
    
    with gr.Row():
        run_btn = gr.Button("🚀 Run Biokernel Boot Sequence", variant="primary")
    
    # Terminal ekranı simülasyonu
    output_box = gr.Code(language="shell", label="System Terminal")
    
    # Butona basıldığında boot_sequence fonksiyonunu çalıştır ve çıktıyı ekrana akıt (yield)
    run_btn.click(fn=boot_sequence, inputs=[], outputs=[output_box])

demo.launch()
