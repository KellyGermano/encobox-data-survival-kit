# Encobox Data Survival Kit

Este proyecto nace a partir de mi experiencia en **Encobox**, una empresa de logística de última milla.  
El objetivo es recrear un flujo de datos completo (ETL → análisis → visualización → predicción) usando **datos sintéticos**, de modo que el proyecto sea reproducible y público sin comprometer información real.

## Objetivos del proyecto

- Construir un pipeline **end-to-end** de datos operativos de logística.
- Practicar y mostrar en portafolio:
  - Extracción y limpieza de datos.
  - Análisis exploratorio (EDA).
  - Dashboards interactivos con KPIs.
  - Automatización de reportes.
  - Primeros modelos de predicción de demanda.

## Fases del proyecto

1. **ETL (Extracción y Limpieza)**  
   - Scripts para cargar datos desde ficheros Excel sintéticos.
   - Normalización de tipos, eliminación de duplicados y nulos.
   - Generación de un dataset limpio para análisis.

2. **EDA (Exploratory Data Analysis)**  
   - Identificación de clientes principales, zonas de mayor demanda y horas pico.
   - Primeras visualizaciones descriptivas.

3. **Dashboard BI**  
   - Creación de un dashboard interactivo con **Streamlit**.
   - KPIs: volumen de pedidos, tiempo medio de entrega, ingresos, incidencias.

4. **Automatización de reportes**  
   - Generación de informes periódicos (CSV/PDF) a partir de los datos procesados.

5. **Predicción de demanda (PoC)**  
   - Baselines de forecasting con series temporales.

---



## Estructura del proyecto



## Instalación

Clonar el repositorio y crear un entorno virtual:

```bash
git clone https://github.com/KellyGermano/encobox_data_survival_kit.git
cd encobox_data_survival_kit
python3 -m venv .venv
source .venv/bin/activate   # en Mac/Linux
.\.venv\Scripts\activate    # en Windows
pip install -r requirements.txt


⸻

Uso
	1.	Generar los datos sintéticos:

python scripts/make_synthetic_data.py


	2.	Ejecutar el pipeline ETL:

python etl/01_extract.py
python etl/02_clean.py


	3.	Lanzar el dashboard:

streamlit run dashboard/app.py



El dashboard se abrirá en http://localhost:8501.

⸻

Capturas

KPIs principales

Evolución de pedidos

Ingresos diarios


⸻

Demo online

Próximamente: desplegado en Streamlit Cloud.

⸻

Notas
	•	Los datos son 100% sintéticos, generados con librerías como numpy y faker.
	•	Este proyecto es parte de mi portafolio personal como Analista de Datos.
	•	Inspirado en mi trabajo en Encobox, pero sin exponer información sensible.

---

### Autora
**Kelly Santos Germano**  
[LinkedIn](https://www.linkedin.com/in/kellygermano) | [Portfolio](https://www.kellygermano.com)
