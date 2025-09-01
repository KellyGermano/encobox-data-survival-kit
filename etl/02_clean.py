from pathlib import Path
import pandas as pd
import sys

BASE = Path(__file__).resolve().parents[1]
INTERIM = BASE / "data" / "interim"
PROCESSED = BASE / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

def read_csv_safe(name):
    p = INTERIM / name
    if not p.exists():
        print(f"⚠️ Falta: {name}")
        return pd.DataFrame()
    df = pd.read_csv(p)
    print(f"✔ {name}: {len(df)} filas")
    return df

def main():
    tasks = read_csv_safe("tasks_raw.csv")
    if tasks.empty:
        print("❌ tasks_raw.csv vacío. Ejecuta 01_extract primero (y revisa los .xlsx).")
        sys.exit(1)

    tasks["fecha"] = pd.to_datetime(tasks["fecha"], errors="coerce")
    tasks = tasks.dropna(subset=["fecha"]).drop_duplicates(subset=["task_id"]).reset_index(drop=True)

    out = PROCESSED / "tasks_clean.csv"
    tasks.to_csv(out, index=False)
    print(f"✅ Guardado: {out} ({len(tasks)} filas)")

if __name__ == "__main__":
    main()
