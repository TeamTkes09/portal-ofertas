# app.py
import streamlit as st
from data.products import get_all_products
from components.cards import render_investment_section
from styles.legal_templates import get_legal_disclaimer # Importamos el blindaje

# Configuración inicial
st.set_page_config(page_title="Arbitrage Pro 2026", layout="wide", initial_sidebar_state="expanded")

# 1. Carga de datos
if 'data' not in st.session_state:
    st.session_state.data = get_all_products()

# 2. Barra Lateral (Filtros)
with st.sidebar:
    st.title("🛡️ Filtros Pro")
    search_query = st.text_input("🔍 Buscar activo:", "").lower()
    filtro_riesgo = st.multiselect("Riesgo:", ["BAJO", "MEDIO", "ALTO"], default=["BAJO", "MEDIO", "ALTO"])
    st.divider()
    st.info("Actualizado: 22 Marzo 2026")

# 3. Lógica de Filtrado
productos_filtrados = [
    p for p in st.session_state.data 
    if (search_query in p['n'].lower()) and (p['r'] in filtro_riesgo)
]

# 4. Renderizado de Interfaz
st.title("🚀 Portal de Arbitraje de Hardware")

if productos_filtrados:
    render_investment_section(".com", productos_filtrados)
else:
    st.warning("No se encontraron activos.")

# 5. INYECCIÓN DEL BLINDAJE LEGAL (Al final de todo)
st.markdown(get_legal_disclaimer(), unsafe_allow_html=True)
