import streamlit as st
import time
# Verificamos importaciones
from data.products import get_real_time_opportunities, get_news_events, get_crypto_opportunities
from components.cards import render_investment_section, render_crypto_section

st.set_page_config(page_title="Arbitraje 360", layout="wide")

# SIDEBAR: CALCULADORA RETAIL
with st.sidebar:
    st.title("⚙️ Configuración")
    pais = st.selectbox("Mercado", [".com", ".es", ".mx"])
    st.divider()
    st.subheader("📊 Costo Arbitraje Físico")
    c_compra = st.number_input("Inversión Producto", value=100.0)
    st.caption("Usa esto para medir el margen neto vs el catálogo.")

# CUERPO
st.title("🚀 Sistema de Arbitraje en Tiempo Real")

tab1, tab2, tab3 = st.tabs(["📰 Noticias Hot", "📦 Productos FBA", "₿ Arbitraje Crypto"])

with tab1:
    noticias = get_news_events()
    for n in noticias:
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.warning(f"**{n['titulo']}**")
            st.write(n['descripcion'])
            st.caption(f"Fuente: {n['fuente']} | {n['hace']}")
        with col_b:
            render_investment_section(pais, n['productos_asociados'])
        st.divider()

with tab2:
    render_investment_section(pais, get_real_time_opportunities())

with tab3:
    render_crypto_section(get_crypto_opportunities())
