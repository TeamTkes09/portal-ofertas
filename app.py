import streamlit as st
from tools.market_monitor import get_binance_tickers
from tools.binance_engine import buscar_n_puntas

st.set_page_config(page_title="Arbitraje Pro", layout="wide")

# Ocultar el menú lateral original para estética horizontal
st.markdown("""<style>[data-testid="stSidebarNav"] {display: none;}</style>""", unsafe_allow_html=True)

st.title("🚀 Sistema de Arbitraje Dinámico")
st.divider()

# --- PESTAÑAS HORIZONTALES ---
tab1, tab2, tab3 = st.tabs(["📊 MONITOR DE MERCADO", "🕸️ ESCÁNER N-PUNTAS", "⚙️ CONFIGURACIÓN"])

with tab1:
    st.subheader("Precios Directos de Binance (USDT)")
    df_precios = get_binance_tickers()
    
    if df_precios is not None:
        st.dataframe(df_precios, use_container_width=True, hide_index=True)
    else:
        st.error("Error de conexión con Binance API. Verifica tu internet.")

with tab2:
    st.subheader("Buscador de Rutas de Ciclo Infinito")
    if 'key' not in st.session_state or not st.session_state['key']:
        st.warning("⚠️ Configura tus llaves API en la pestaña de Configuración.")
    else:
        if st.button("🔍 Iniciar Escaneo de Grafo"):
            res = buscar_n_puntas(st.session_state['key'], st.session_state['secret'])
            st.json(res)

with tab3:
    st.subheader("Configuración de Seguridad")
    st.session_state['key'] = st.text_input("Binance API Key", type="password")
    st.session_state['secret'] = st.text_input("Binance Secret Key", type="password")
    st.info("Las llaves se mantienen en la memoria de la sesión actual.")
