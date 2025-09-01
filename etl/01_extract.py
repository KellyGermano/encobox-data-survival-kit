from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "raw_synth"
INTERIM = BASE / "data" / "interim"
INTERIM.mkdir(parents=True, exist_ok=True)

def read_xlsx(name):
    p = RAW / name
    if not p.exists():
        print(f"⚠️ No existe: {p.name}")
        return pd.DataFrame()
    df = pd.read_excel(p)
    df["__source_file"] = p.name
    print(f"✔ {p.name}: {df.shape[0]} filas, {df.shape[1]} cols")
    return df

def main():
    tasks     = read_xlsx("Task List – Synthetic.xlsx")
    merchants = read_xlsx("Merchant List – Synthetic.xlsx")
    users     = read_xlsx("User List – Synthetic.xlsx")

    if not tasks.empty:
        (INTERIM/"tasks_raw.csv").write_text(tasks.to_csv(index=False))
    if not merchants.empty:
        (INTERIM/"merchants_raw.csv").write_text(merchants.to_csv(index=False))
    if not users.empty:
        (INTERIM/"users_raw.csv").write_text(users.to_csv(index=False))

if __name__ == "__main__":
    main()
