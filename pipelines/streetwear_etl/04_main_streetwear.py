import subprocess
import sys
import time
from pathlib import Path

# Directorio donde reside este script: .../pipelines/streetwear_etl
SCRIPTS_DIR = Path(__file__).resolve().parent

# Raíz del proyecto: sube dos niveles (streetwear_etl -> pipelines -> etl_commerce_pro)
PROJECT_ROOT = SCRIPTS_DIR.parent.parent

def run_step(step_name: str, script_name: str) -> None:
    script_path = SCRIPTS_DIR / script_name
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
    print(f"Ruta scripts : {SCRIPTS_DIR}")
    print(f"Raíz proyecto: {PROJECT_ROOT}")
    print("=" * 60)

    pipeline_steps = [
        ("Capa Bronze (Extracción)", "01_extract.py"),
        ("Capa Silver (Transformación)", "02_transform.py"),
        ("Capa Gold (Analítica y Load)", "03_streetwear_analytics.py")
    ]

    for name, script_name in pipeline_steps:
        run_step(name, script_name)

    total_duration = round(time.time() - total_start, 2)
    print("\n" + "=" * 60)
    print(f"PIPELINE COMPLETADO CON ÉXITO en {total_duration}s")
    print("=" * 60)