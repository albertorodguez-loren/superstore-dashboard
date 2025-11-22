import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Superstore Dashboard", layout="wide")
st.title("Superstore Sales Dashboard Interactivo")
st.markdown("**Análisis 2014-2017** – Proyecto portfolio Data Science")

df = pd.read_csv("superstore_clean.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sidebar
year = st.sidebar.multiselect("Año", options=sorted(df['Year'].unique()), default=sorted(df['Year'].unique()))
region = st.sidebar.multiselect("Región", df['Region'].unique(), df['Region'].unique())
category = st.sidebar.multiselect("Categoría", df['Category'].unique(), df['Category'].unique())

data = df[(df['Year'].isin(year)) & (df['Region'].isin(region)) & (df['Category'].isin(category))]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Ventas Totales", f"${data['Sales'].sum():,.0f}")
c2.metric("Profit Total", f"${data['Profit'].sum():,.0f}")
c3.metric("Órdenes", f"{data['Order ID'].nunique():,}")
c4.metric("Margen", f"{data['Profit'].sum()/data['Sales'].sum()*100:.1f}%")

col1, col2 = st.columns(2)
with col1:
    fig1 = px.bar(data.groupby('Region').agg({'Sales':'sum','Profit':'sum'}).reset_index(),
                  x='Region', y=['Sales','Profit'], title="Ventas y Profit por Región")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    monthly = data.groupby([data['Order Date'].dt.year, data['Order Date'].dt.month_name()], 
                          sort=False)['Sales'].sum().reset_index()
    fig2 = px.line(monthly, x='Order Date', y='Sales', color='Order Date', 
                   title="Evolución Mensual")
    st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(px.scatter(data.groupby('Product Name').agg({'Sales':'sum','Profit':'mean','Quantity':'sum'})
                          .nlargest(10,'Sales').reset_index(),
                          x='Sales', y='Profit', size='Quantity', color='Product Name',
                          title="Top 10 Productos"), use_container_width=True)
