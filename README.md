# superstore-dashboard
# Superstore Sales Dashboard Interactivo 

**Análisis completo de +2.3M$ en ventas (2014-2017)**  
Dashboard 100 % interactivo con filtros en tiempo real, KPIs y visualizaciones avanzadas.

Live Demo → https://superstore-dashboard-xgigiknvsvafvn6fytxawx.streamlit.app/

![Dashboard preview](https://github.com/albertordguez-loren/superstore-dashboard/blob/main/preview.gif?raw=true)

### Características principales
- KPIs en tiempo real (ventas, profit, órdenes, margen)
- Filtros por Año / Región / Categoría
- Ventas y Profit por región
- Evolución mensual de ventas
- Top 10 productos estrella (scatter con tamaño = cantidad)
- Descarga de datos filtrados en CSV

### Tecnologías utilizadas
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

### Cómo ejecutarlo localmente
```bash
git clone https://github.com/albertordguez-loren/superstore-dashboard.git
cd superstore-dashboard
pip install -r requirements.txt
streamlit run app.py
