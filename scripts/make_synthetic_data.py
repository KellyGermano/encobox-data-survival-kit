from pathlib import Path
import numpy as np, pandas as pd
from faker import Faker

BASE = Path(__file__).resolve().parents[1]
RAW  = BASE / "data" / "raw_synth"
RAW.mkdir(parents=True, exist_ok=True)

np.random.seed(42)
fake = Faker("es_ES")

dias = 90
fechas = pd.date_range(end=pd.Timestamp.today().normalize(), periods=dias)
zonas = ["Centro","Norte","Sur","Este","Oeste"]

merchants = pd.DataFrame({
    "merchant_id":[f"M{str(i).zfill(3)}" for i in range(1,21)],
    "nombre":[f"Tienda_{i}" for i in range(1,21)],
    "categoria": np.random.choice(["Restaurante","Tienda","Supermercado"], size=20)
})
merchants.to_excel(RAW/"Merchant List – Synthetic.xlsx", index=False)

users = pd.DataFrame({
    "user_id":[f"U{str(i).zfill(3)}" for i in range(1,101)],
    "nombre":[fake.first_name()+" "+fake.last_name() for _ in range(100)],
    "zona": np.random.choice(zonas, size=100),
    "activo": np.random.choice([True, False], size=100, p=[0.85,0.15])
})
users.to_excel(RAW/"User List – Synthetic.xlsx", index=False)

rows=[]; task_id=1
for f in fechas:
    demanda = np.random.poisson(lam=120)
    for z in zonas:
        share = np.random.uniform(0.15,0.30)
        pedidos = max(0, int(demanda*share + np.random.normal(0,5)))
        for _ in range(pedidos):
            estado = np.random.choice(["Entregado","Reintento","Fallido"], p=[0.92,0.05,0.03])
            rows.append({
                "task_id": task_id,
                "fecha": f.date(),
                "zona": z,
                "cliente_id": f"C{np.random.randint(1,51):03d}",
                "repartidor_id": f"U{np.random.randint(1,101):03d}",
                "merchant_id": f"M{np.random.randint(1,21):03d}",
                "tiempo_entrega": int(np.clip(np.random.normal(45,12), 15, 120)),
                "importe": round(np.clip(np.random.normal(15,6), 4, 60), 2),
                "estado": estado
            })
            task_id += 1
tasks = pd.DataFrame(rows)
tasks.to_excel(RAW/"Task List – Synthetic.xlsx", index=False)
print("✔ Datos sintéticos generados en data/raw_synth/")
