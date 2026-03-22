import streamlit as st
import time
from data.products import get_crypto_opportunities, buscar_ciclo_infinito, ejecutar_ruta_dinamica

st.set_page_config(page_title="Radar de Arbitraje N-Puntas", layout="wide")

st.title("₿ Arbitraje Inteligente de Ciclo Infinito")
st.caption("Algoritmo de Grafos Bellman-Ford detectando ineficiencias en tiempo real.")

# --- SIDEBAR: CONFIGURACIÓN DE API ---
with st.sidebar:
    st.header("🔑 Configuración Binance")
    api_key = st.text_input("API Key", type="password")
    secret_key = st.text_input("Secret Key", type="password")
    st.divider()
    monto_operar = st.number_input("Capital USDT a utilizar", min_value=15.0, value=80.0, step=5.0)
    min_roi_exec = st.slider("ROI Mínimo para Auto-Trade (%)", 0.1, 2.0, 0.5)
    st.info("💡 Asegúrate de tener BNB en tu cuenta para reducir comisiones a 0.075%.")

# --- BLOQUE 1: MONITOR DE MERCADO (TOP 200) ---
st.subheader("📊 Monitor de Spreads Directos")
data_200 = get_crypto_opportunities()
if data_200:
    df = pd.DataFrame(data_200)
    st.dataframe(df.head(10), use_container_width=True, hide_index=True)

st.divider()

# --- BLOQUE 2: ESCÁNER DE N-PUNTAS ---
st.header("🕸️ Buscador de Ciclos Indefinidos")

col1, col2 = st.columns([1, 2])

with col1:
    if st.button("🔍 ESCANEAR GRAFO DE BINANCE", use_container_width=True):
        if not api_key or not secret_key:
            st.warning("⚠️ Ingresa tus llaves API en el menú lateral.")
        else:
            with st.spinner("Analizando miles de combinaciones..."):
                res = buscar_ciclo_infinito(api_key, secret_key)
                
                if res['status'] == 'success':
                    st.session_state['ultima_ruta'] = res['ruta']
                    st.session_state['ultimo_roi'] = res['roi']
                    
                    st.metric("Mejor ROI Hallado", f"{res['roi']:.3f}%", 
                              delta="Rentable" if res['roi'] > 0 else "Pérdida")
                    
                    ruta_str = " ➡️ ".join(res['ruta'])
                    st.code(f"RUTA: {ruta_str}", language="text")
                else:
                    st.info("No se hallaron ciclos rentables en este segundo.")

with col2:
    if 'ultima_ruta' in st.session_state:
        st.write("### ⚡ Ejecución Instantánea")
        st.write(f"Ruta cargada: **{len(st.session_state['ultima_ruta'])} saltos**")
        
        if st.button("🔥 DISPARAR OPERACIÓN", type="primary", use_container_width=True):
            with st.status("Ejecutando saltos en Binance API...", expanded=True) as status:
                inicio = time.time()
                ejecucion = ejecutar_ruta_dinamica(
                    api_key, secret_key, 
                    st.session_state['ultima_ruta'], 
                    monto_operar
                )
                fin = time.time()
                
                if ejecucion['status'] == 'success':
                    status.update(label=f"✅ ¡Éxito! Ciclo completado en {fin-inicio:.2f}s", state="complete")
                    st.balloons()
                    st.success(f"Finalizado con {ejecucion['final']} USDT")
                else:
                    status.update(label="❌ Error en la cadena", state="error")
                    st.error(ejecucion['message'])

# --- MODO CENTINELA (AUTO-SCAN) ---
st.divider()
st.subheader("🤖 Modo Centinela")
auto_scan = st.toggle("Activar escaneo automático cada 10 segundos")

if auto_scan:
    if not api_key:
        st.error("Necesitas API Key para el modo Centinela.")
    else:
        st.toast("Modo Centinela Activo. Buscando brechas...")
        # Aquí podrías usar un loop de tiempo (time.sleep) pero Streamlit 
        # prefiere st.rerun() o fragmentos. Por ahora, úsalo manual para seguridad.
