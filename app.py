import streamlit as st
from data.products import get_all_products
from components.cards import render_investment_section

# 1. CONFIGURACIÓN DE PANTALLA (OBLIGATORIO AL PRINCIPIO)
st.set_page_config(
    page_title="Arbitraje Pro 2026",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo para eliminar márgenes laterales sobrantes de Streamlit
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 0rem; padding-left: 2rem; padding-right: 2rem; }
    </style>
    """, unsafe_content_id=True)

st.title("🚀 Portal de Arbitraje 2026")

# 2. CARGA DE DATOS
productos = get_all_products()

# 3. FILTROS SIMPLES
cat_seleccionada = st.selectbox("Seleccionar Categoría", ["TODAS", "TECNOLOGÍA", "HOGAR", "BELLEZA", "HERRAMIENTAS"])

if cat_seleccionada != "TODAS":
    productos_filtrados = [p for p in productos if p['cat'] == cat_seleccionada]
else:
    productos_filtrados = productos

# 4. RENDERIZADO
render_investment_section(".com", productos_filtrados)
