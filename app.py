# app.py
import streamlit as st
from data.products import get_all_products
from components.cards import render_investment_section
from components.table_view import render_table_section # Nueva importación
from styles.legal_templates import get_legal_disclaimer

# Configuración
st.set_page_config(page_title="Arbitrage Pro 2026", layout="wide")

# Carga de datos
if 'data' not in st.session_state:
    st.session_state.data = get_all_products()

# Encabezado
st.title("🚀 Portal de Arbitraje de Hardware")

# --- SECCIÓN DE FILTROS ---
col_search, col_risk = st.columns([2, 1])
with col_search:
    search_query = st.text_input("🔍 Buscar activo:", placeholder="Ej: SSD, DDR5...").lower()
with col_risk:
    filtro_riesgo = st.multiselect("Nivel de Riesgo:", ["BAJO", "MEDIO", "ALTO"], default=["BAJO", "MEDIO", "ALTO"])

# Lógica de Filtrado
productos_filtrados = [
    p for p in st.session_state.data 
    if (search_query in p['n'].lower() or search_query in p['cat'].lower())
    and (p['r'] in filtro_riesgo)
]

# --- SELECTOR DE VISTA (Tabs) ---
tab_cards, tab_table = st.tabs(["🎴 Vista de Tarjetas", "📑 Vista de Excel"])

with tab_cards:
    if productos_filtrados:
        render_investment_section(".com", productos_filtrados)
    else:
        st.warning("No hay resultados.")

with tab_table:
    if productos_filtrados:
        render_table_section(productos_filtrados)
    else:
        st.warning("No hay resultados para mostrar en la tabla.")

# Blindaje Legal
st.markdown(get_legal_disclaimer(), unsafe_allow_html=True)
