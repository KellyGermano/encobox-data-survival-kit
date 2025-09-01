# Encobox Data Survival Kit

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Proyecto de análisis y visualización de datos operativos.  
Incluye un pipeline ETL en Python para extracción y limpieza de datos, notebooks para exploración y modelos, y un dashboard en Streamlit para monitorizar KPIs.

## Estructura del Proyecto
encobox_data_survival_kit/
├── dashboard/              # App Streamlit para visualización
├── data/                   # Carpeta de datos (raw, interim, processed)
├── etl/                    # Scripts ETL iniciales
├── notebooks/              # Exploración y modelado
├── reports/                # Documentación y reportes
├── scripts/                # Utilidades varias (synthetic data, etc.)
├── src/                    # Código principal (ETL, modelos, visualización)
├── requirements.txt        # Dependencias del proyecto
├── .env.example            # Variables de entorno de ejemplo
└── README.md
## Instalación

```bash
git clone git@github.com:KellyGermano/encobox-data-survival-kit.git
cd encobox-data-survival-kit

python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows

pip install -r requirements.txt
Configuración

Copia el archivo .env.example a .env y completa las variables necesarias:
cp .env.example .env
Uso
python etl/01_extract.py
python etl/02_clean.py
streamlit run dashboard/app.py
Licencia

Este proyecto está bajo la licencia MIT.
