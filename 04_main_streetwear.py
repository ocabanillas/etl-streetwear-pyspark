import subprocess
import sys
import time
from pathlib import Path

# Directorio raíz del proyecto (donde residen los scripts y la carpeta data/)
PROJECT_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = PROJECT_ROOT

def run_step(step_name: str, script_name: str) -> None:
    script_path = SCRIPTS_DIR / script_name
    
    if not script_path.exists():
        print(f"\n[ERROR] No se encontró el script requerido: {script_path}")
        sys.exit(1)
        
    print(f"\n---> Iniciando paso: {step_name} ({script_path.name})")
    start_time = time.time()
    
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT
    )
    
    if result.returncode != 0:
        print(f"\n[ERROR] El paso '{step_name}' falló con código de salida {result.returncode}.")
        sys.exit(1)
        
    duration = round(time.time() - start_time, 2)
    print(f"[OK] {step_name} finalizado en {duration} segundos.")

if __name__ == "__main__":
    total_start = time.time()
    print("=" * 60)
    print("INICIANDO PIPELINE: STREETWEAR_ETL")
    print(f"Raíz proyecto: {PROJECT_ROOT}")
    print("=" * 60)

    # Asegúramos que coincidan los nombres y rutas
    
    pipeline_steps = [
        ("Capa Bronze (Extracción)", "01_streetwear_extract.py"),
        ("Capa Silver (Transformación)", "02_streetwear_transform.py"),
        ("Capa Gold (Analítica y Load)", "03_streetwear_analytics.py")
    ]

    for name, script_name in pipeline_steps:
        run_step(name, script_name)

    total_duration = round(time.time() - total_start, 2)
    print("\n" + "=" * 60)
    print(f"PIPELINE COMPLETADO CON ÉXITO en {total_duration}s")
    print("=" * 60)