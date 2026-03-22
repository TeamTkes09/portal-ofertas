# app.py
import streamlit as st
from data.products import get_all_products
from components.cards import render_investment_section

# Configuración inicial
st.set_page_config(page_title="Arbitrage Tracker Pro", layout="wide")

# Carga de datos en estado de sesión
if 'data' not in st.session_state:
    st.session_state.data = get_all_products()

# Interfaz de usuario
st.title("🚀 Panel de Arbitraje de Hardware")
st.caption("Comparativa de precios en tiempo real para reventa estratégica.")

# Buscador simple
search_query = st.text_input("🔍 Buscar activo por nombre...", "").lower()

# Filtrado lógico
productos_finales = [
    p for p in st.session_state.data 
    if search_query in p['n'].lower() or search_query in p['cat'].lower()
]

# Renderizado final
if productos_finales:
    render_investment_section(".com", productos_finales)
else:
    st.warning("No se encontraron activos con ese nombre.")
