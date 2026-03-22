import streamlit as st
import pandas as pd
import time
from data.products import get_real_time_opportunities, get_news_events, get_crypto_opportunities
from components.cards import render_investment_section, render_crypto_section

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Arbitraje 360 Pro - v2026",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 🛡️ BLINDAJE DE RESPONSABILIDAD (DIÁLOGO OBLIGATORIO) ---
if 'legal_accepted' not in st.session_state:
    @st.dialog("⚖️ Términos y Blindaje de Responsabilidad")
    def show_legal():
        st.error("AVISO CRÍTICO PARA EL OPERADOR")
        st.write("""
        Esta herramienta proporciona datos estimados basados en APIs de terceros. 
        - **Volatilidad:** Los precios pueden cambiar en segundos.
        - **Responsabilidad:** No nos hacemos responsables por pérdidas de capital o bloqueos de cuenta (Gating).
        - **Costos:** Los márgenes mostrados son brutos; use el calculador lateral para netos.
        """)
        if st.button("He leído y acepto los riesgos de mercado"):
            st.session_state.legal_accepted = True
            st.rerun()
    show_legal()

# --- 🎨 ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .block-container { padding: 1rem 2rem; }
    .news-box { background: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #22c55e; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { font-weight: bold; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- ⚙️ SIDEBAR: CONFIGURACIÓN Y CALCULADORA ---
with st.sidebar:
    st.title("⚙️ Operaciones")
    
    # Selección de País y Lenguaje
    col_l, col_p = st.columns(2)
    with col_l:
        idioma = st.selectbox("Idioma", ["ES", "EN"])
    with col_p:
        pais = st.selectbox("Mercado", [".com", ".es", ".mx", ".co"])
    
    st.divider()
    
    # CALCULADOR DE COSTO ESTIMADO (Arbitraje Entero)
    st.subheader("🧮 Calculador de Costos")
    costo_compra = st.number_input("Precio Compra ($)", min_value=0.0, value=100.0)
    
    with st.expander("Detalle de Gastos FBA/Prep", expanded=False):
        tax = st.slider("Sales Tax / IVA (%)", 0, 21, 7)
        prep = st.number_input("Prep Center (Etiqueta/Bolsa)", value=1.50)
        envio_fba = st.number_input("Envío a Amazon (Inbound)", value=0.80)
        comision_amz = st.slider("Comisión Amazon (%)", 8, 15, 15)
        fba_fee = st.number_input("Tarifa Logística (Fulfillment)", value=5.50)

    # Cálculo Final
    total_gastos = (costo_compra * (tax/100)) + prep + envio_fba + fba_fee + (costo_compra * (comision_amz/100))
    costo_total_operativo = costo_compra + total_gastos
    
    st.metric("Inversión Total Estimada", f"${costo_total_operativo:.2f}")
    st.caption("Incluye compra, logística y fees de venta.")
    
    st.divider()
    st.info(f"⏱️ Próximo refresco: {15 - ((int(time.time()) // 60) % 15)} min")

# --- 🚀 CUERPO PRINCIPAL ---
st.title("🚀 Centro de Mando de Arbitraje")
st.caption(f"Sincronizado con APIs de Amazon, Keepa y Exchanges • {time.strftime('%d/%m/%Y %H:%M')}")

# PESTAÑAS
tab_news, tab_prod, tab_crypto = st.tabs([
    "📰 Noticias y Eventos", 
    "📦 Catálogo General (FBA)", 
    "₿ Arbitraje Crypto (Exchanges)"
])

# --- PESTAÑA 1: NOTICIAS OPERATIVAS ---
with tab_news:
    st.subheader("🔥 Oportunidades por Eventos de Mercado")
    noticias_eventos = get_news_events() # Carga noticias vinculadas a productos
    
    for ev in noticias_eventos:
        col_n, col_p = st.columns([1, 2])
        with col_n:
            st.markdown(f"""
                <div class="news-box">
                    <small style="color:#94a3b8;">{ev['fuente']} • Hace {ev['hace']}</small>
                    <h4 style="margin:5px 0;">{ev['titulo']}</h4>
                    <p style="font-size:0.85rem;">{ev['descripcion']}</p>
                    <span style="background:#064e3b; color:#4ade80; padding:2px 8px; border-radius:10px; font-size:0.7rem;">
                        Impacto: {ev['impacto']}
                    </span>
                </div>
            """, unsafe_allow_html=True)
        with col_p:
            render_investment_section(pais, ev['productos_asociados'])
        st.divider()

# --- PESTAÑA 2: PRODUCTOS FÍSICOS (CATÁLOGO)
