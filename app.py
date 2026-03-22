import streamlit as st
from data.products import get_real_time_opportunities, get_news_events, get_crypto_opportunities
from components.cards import render_investment_section, render_crypto_section

st.set_page_config(page_title="Arbitraje Pro", layout="wide")

with st.sidebar:
    st.title("⚙️ Opciones")
    pais = st.selectbox("País", [".com", ".es", ".mx"])
    st.info("Actualización: Cada 15 min")

st.title("🚀 Sistema de Arbitraje 2026")

t1, t2, t3 = st.tabs(["📰 Noticias", "📦 Productos FBA", "₿ Criptomonedas"])

with t1:
    for n in get_news_events():
        col_n, col_p = st.columns([1, 2])
        col_n.info(f"**{n['titulo']}**\n\n{n['descripcion']}")
        with col_p: render_investment_section(pais, n['productos_asociados'])

with t2:
    render_investment_section(pais, get_real_time_opportunities())

with t3:
    render_crypto_section(get_crypto_opportunities())
