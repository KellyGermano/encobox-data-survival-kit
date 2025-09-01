from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard Operativo – Última Milla", layout="wide")

@st.cache_data
def load_data():
    path = Path(__file__).resolve().parents[1] / "data" / "processed" / "tasks_clean.csv"
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, parse_dates=["fecha"])

df = load_data()

st.title("Dashboard Operativo – Última Milla (Datos Sintéticos)")
st.caption("KPIs diarios de pedidos, tiempos y zonas. Proyecto de portafolio.")

if df.empty:
    st.error("No hay datos procesados. Ejecuta: python etl/01_extract.py && python etl/02_clean.py")
else:
    daily = df.groupby("fecha", as_index=False).agg(
        pedidos=("task_id", "count"),
        tiempo_entrega=("tiempo_entrega", "mean"),
        importe=("importe", "sum")
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Pedidos (total)", int(daily["pedidos"].sum()))
    c2.metric("Tiempo medio entrega", f"{daily['tiempo_entrega'].mean():.1f} min")
    c3.metric("Ingresos (total)", f"{daily['importe'].sum():.0f} €")

    st.subheader("Pedidos por día")
    st.line_chart(daily.set_index("fecha")[["pedidos"]])

    st.subheader("Tiempo medio de entrega")
    st.line_chart(daily.set_index("fecha")[["tiempo_entrega"]])

    st.subheader("Ingresos diarios (€)")
    st.bar_chart(daily.set_index("fecha")[["importe"]])

    st.caption("Nota: datos 100% sintéticos.")
