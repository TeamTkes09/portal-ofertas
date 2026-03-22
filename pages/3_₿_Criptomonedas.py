import streamlit as st
from data.products import get_crypto_opportunities, get_optimized_routes
from components.cards import render_crypto_section, render_optimized_selector

st.title("₿ Arbitraje Crypto & Redes")

# Ejecutamos el monitor general
data_200 = get_crypto_opportunities()
render_crypto_section(data_200)

# Ejecutamos el selector de rutas inteligentes
rutas_opt = get_optimized_routes()
render_optimized_selector(rutas_opt)
