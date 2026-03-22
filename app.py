import streamlit as st
import pandas as pd
import time
from data.products import get_real_time_opportunities, get_news_events, get_crypto_opportunities
from components.cards import render_investment_section, render_crypto_section

st.set_page_config(page_title="Arbitraje Pro 2026", layout="wide", initial_sidebar_state="expanded")

# --- 🛡️ BLINDAJE DE RESPONSABILIDAD ---
if 'legal_accepted' not in st.session_state:
    @st.dialog("⚖️ Términos y Blindaje de Responsabilidad")
    def show_legal():
        st.error("AVISO DE RIESGO DE CAPITAL")
        st.write("Esta herramienta es para análisis de arbitraje. Los precios fluctúan cada 15 min. No garantizamos ganancias fijas.")
        if st.button("Acepto los términos y riesgos"):
            st.session_state.legal_accepted = True
            st.rerun()
    show_legal()

# --- ⚙️ SIDEBAR: CONFIGURACIÓN Y CALCULADORA ---
with st.sidebar:
    st.title("⚙️ Panel de Control")
    pais = st.selectbox("Mercado Amazon", [".com", ".es", ".mx"], index=0)
    
    st.divider()
    st.subheader("🧮 Calculador de Costos")
    precio_c = st.number_input("Precio Compra ($)", value=100.0)
    with st.expander("Detalles Operativos", expanded=False):
        tax = st.slider("Impuestos (%)", 0, 21, 7)
        prep = st.number_input("Prep Center/Pack", value=1.50)
        amz_fee = st.slider("Comisión AMZ (%)", 8, 15, 15)
        fba_ship = st.number_input("Fulfillment Fee", value=5.50)
    
    total_costo = precio_c + (precio_c * (tax/100)) + prep + fba_ship + (precio_c * (amz_fee/100))
    st.metric("Costo Total Operativo", f"${total_costo:.2f}")
    st.caption("Usa este dato para comparar con el precio de venta local.")

# --- 🚀 CUERPO PRINCIPAL ---
st.title("🚀 Centro de Mando de Arbitraje 2026")

tab1, tab2, tab3 = st.tabs(["📰 Noticias y Oportunidades", "📦 Catálogo FBA", "₿ Arbitraje Crypto"])

with tab1:
    st.subheader("🔥 Eventos de Mercado")
    noticias = get_news_events()
    for ev in noticias:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.markdown(f"""
                <div style="background:#1e293b; padding:15px; border-radius:10px; border-left:5px solid #22c55e;">
                    <small>{ev['fuente']} • {ev['hace']}</small>
                    <h4>{ev['titulo']}</h4>
                    <p style="font-size:0.85rem;">{ev['descripcion']}</p>
                    <small>Impacto: <b>{ev['impacto']}</b></small>
                </div>""", unsafe_allow_html=True)
        with c2:
            render_investment_section(pais, ev['productos_asociados'])
        st.divider()

with tab2:
    prods = get_real_time_opportunities()
    render_investment_section(pais, prods)

with tab3:
    st.subheader("₿ Spreads entre Exchanges")
    cryptos = get_crypto_opportunities()
    render_crypto_section(cryptos)
