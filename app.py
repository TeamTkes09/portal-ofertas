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
    
    # Verificamos si las llaves existen antes de mostrar el botón
    if 'key' not in st.session_state or not st.session_state['key']:
        st.warning("⚠️ Configura tus llaves API en la pestaña de Configuración.")
    else:
        # LÍNEA 30: El inicio del bloque
        if st.button("🔍 Iniciar Escaneo de Grafo"):
            # LÍNEA 31: DEBE tener una sangría (4 espacios) respecto al 'if'
            with st.spinner("Analizando 500 nodos de liquidez..."):
                res = buscar_n_puntas(st.session_state['key'], st.session_state['secret'])
                
                if res['status'] == 'success':
                    st.success(f"🔥 ¡Oportunidad Detectada! ROI: {res['roi']}%")
                    st.info(f"Ruta: {' ➡️ '.join(res['ruta'])}")
                    st.session_state['ruta_activa'] = res['ruta']
                elif res['status'] == 'no_path':
                    st.info("Mercado eficiente. No se hallaron brechas rentables.")
                else:
                    st.error(f"Error: {res['message']}")
with tab3:
    st.subheader("Configuración de Seguridad")
    # Usamos on_change para asegurar que se guarde el estado inmediatamente
    st.text_input("Binance API Key", type="password", key='key_input')
    st.text_input("Binance Secret Key", type="password", key='secret_input')
    
    if st.button("Guardar y Validar Llaves"):
        st.session_state['key'] = st.session_state['key_input']
        st.session_state['secret'] = st.session_state['secret_input']
        st.success("Llaves vinculadas a la sesión.")
        st.cache_data.clear() # Limpiamos caché para forzar nueva conexión
    
    st.divider()
    st.subheader("🛠️ Diagnóstico de Conexión")
    # ... (Tu código de diagnóstico aquí)
