import gradio as gr
import time
import os

def run_demo():
    # Siyah terminal kutusunu oluşturan HTML yapısı
    def format_html(text):
        return f"""
        <div style="background-color: #0c0c0c; color: #cccccc; padding: 20px; 
                    font-family: 'Courier New', monospace; font-size: 16px; 
                    border-radius: 8px; border: 1px solid #333; min-height: 400px; 
                    white-space: pre-wrap;">{text}</div>
        """
    
    log = ""
    yield format_html(log)
    
    # Renkli metin ekleme fonksiyonu
    def add_text(new_text, color="white"):
        nonlocal log
        color_map = {
            "green": "#00FF00", 
            "yellow": "#FFFF00", 
            "red": "#FF0000", 
            "cyan": "#00FFFF", 
            "white": "#FFFFFF"
        }
        log += f'<span style="color: {color_map.get(color, "white")}">{new_text}</span>'
        return format_html(log)

    # 1. Başlık Kısmı
    yield add_text("\n====================================================\n", "cyan")
    yield add_text("      BIOKERNEL SOVEREIGN OS - v1.0.0 BOOT SEQUENCE \n", "cyan")
    yield add_text("      AUTHOR: HASAN AYHAN ÖZCAN                     \n", "cyan")
    yield add_text("====================================================\n\n", "cyan")
    time.sleep(1)

    # 2. Modüllerin Yüklenmesi
    yield add_text("[+] Initializing Core Bio-Digital Engines...\n", "green")
    
    core_modules = {
        "sovereign_orchestrator.py": "Sovereign AI Master Orchestrator",
        "lnn_bio_simulation.py": "Liquid Neural Networks (LNN) Fluidic Engine",
        "snn_biosensor.py": "Neuromorphic Computing & SNN Transducers",
        "ais_memory_engine.py": "Agentic AI Swarm Protocols & Immune Memory"
    }
    
    for filename, desc in core_modules.items():
        if os.path.exists(filename):
            yield add_text(f"  --> [{filename}] {desc} ... ", "white")
            yield add_text("ONLINE\n", "green")
        else:
            yield add_text(f"  --> [{filename}] {desc} ... ", "white")
            yield add_text("STANDBY\n", "yellow")
        time.sleep(0.4)
    
    time.sleep(1)
    
    # 3. Güvenlik ve Hata Mesajları
    yield add_text("\n[!] SYSTEM HALT: Modules P1 through P105 are RESTRICTED.\n", "yellow")
    yield add_text("[!] Commercial IP Vault is locked by cryptographically sealed hash.\n", "yellow")
    time.sleep(1)
    
    yield add_text("\n[X] ACCESS DENIED to Phase 2-13 Modules. Symbiotic License required.\n", "red")
    yield add_text("[i] Please contact hasanayhanozcan9@gmail.com for enterprise integration.\n", "cyan")
    time.sleep(1)
    
    yield add_text("\n[+] System entering autonomous idle state. Listening for node connections...\n", "green")
    
    # 4. ARAYÜZÜ KİLİTLEMEYEN GERÇEK SONSUZ DÖNGÜ (Mesh Network Taraması)
    base_log = log
    while True:
        yield format_html(base_log + '<span style="color: #00FF00">Biokernel Active: Monitoring local biological mesh network...</span>')
        time.sleep(0.8)
        yield format_html(base_log + '<span style="color: #00FF00">Biokernel Active: Monitoring local biological mesh network.  </span>')
        time.sleep(0.8)
        yield format_html(base_log + '<span style="color: #00FF00">Biokernel Active: Monitoring local biological mesh network.. </span>')
        time.sleep(0.8)

# --- WEB ARAYÜZÜNÜN TASARIMI ---
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🧬 BIOKERNEL: THE SOVEREIGN BIO-DIGITAL ECOSYSTEM")
    gr.Markdown("**AUTHOR:** HASAN AYHAN ÖZCAN")
    gr.Markdown("---")
    
    # Başlatma Butonu
    btn = gr.Button("🚀 INITIATE BOOT SEQUENCE", variant="primary")
    
    # Siyah Ekran Kutusu
    terminal_output = gr.HTML(
        value='<div style="background-color: #0c0c0c; color: #cccccc; padding: 20px; font-family: \'Courier New\', monospace; font-size: 16px; border-radius: 8px; border: 1px solid #333; min-height: 400px;">System Ready. Waiting for initialization trigger...</div>'
    )
    
    # Butona basılınca run_demo fonksiyonunu çalıştır
    btn.click(fn=run_demo, inputs=[], outputs=[terminal_output])

# Sunucuyu başlat
if __name__ == "__main__":
    demo.launch()
