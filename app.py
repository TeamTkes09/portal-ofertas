# app.py
import streamlit as st
from data.products import get_all_products
from components.cards import render_investment_section

st.set_page_config(page_title="Arbitrage Pro", layout="wide")

# Inicializar sesión
if 'data' not in st.session_state:
    st.session_state.data = get_all_products()

# Filtros sencillos
st.title("🚀 Panel de Arbitraje 2026")
query = st.text_input("Buscar producto...", "").lower()

# Filtrado
final_list = [p for p in st.session_state.data if query in p['n'].lower()]

# Mostrar
if final_list:
    render_investment_section(".com", final_list)
else:
    st.warning("No hay resultados.")
