import streamlit as st
from tools.market_monitor import get_binance_prices
from tools.binance_engine import find_n_path_cycle, execute_trade_cycle

# Configuración de página (Esto debe ser lo primero)
st.set_page_config(page_title="Crypto Radar Pro", layout="wide")

# --- TÍTULO PRINCIPAL ---
st.title("🚀 Portal de Arbitraje Inteligente")
st.caption("Conexión directa con Binance API | Algoritmo N-Puntas")

# --- NAVEGACIÓN HORIZONTAL ---
# Aquí definimos las pestañas que antes estaban a la izquierda
tab1, tab2, tab3 = st.tabs(["📊 Monitor de Mercado", "🕸️ Escáner N-Puntas", "📜 Historial de Trades"])

# --- CONTENIDO DE LAS PESTAÑAS ---

with tab1:
    st.header("Precios en Tiempo Real (Binance)")
    # Llamamos a la lógica que antes estaba en la página de Cripto
    prices = get_binance_prices()
    if prices:
        st.dataframe(prices, use_container_width=True)

with tab2:
    st.header("Buscador de Ciclos Infinitos")
    col_api, col_exec = st.columns([1, 2])
    
    with col_api:
        key = st.text_input("API Key", type="password")
        secret = st.text_input("Secret Key", type="password")
        monto = st.number_input("Inversión (USDT)", value=80.0)

    if st.button("🔍 Escanear Grafo"):
        with st.spinner("Buscando rutas rentables..."):
            # Lógica del motor de grafos
            res = find_n_path_cycle(key, secret)
            st.write(res)

with tab3:
    st.header("Registro de Operaciones")
    # Aquí mostramos el log de auditoría
    if 'audit_log' in st.session_state:
        st.table(st.session_state['audit_log'])
    else:
        st.info("No hay operaciones registradas en esta sesión.")
