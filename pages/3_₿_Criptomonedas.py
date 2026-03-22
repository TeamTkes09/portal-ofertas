import streamlit as st
import pandas as pd  # <--- ESTA ERA LA LÍNEA QUE FALTABA
import time
from data.products import get_crypto_opportunities, buscar_ciclo_infinito, ejecutar_ruta_dinamica

st.set_page_config(page_title="Radar de Arbitraje N-Puntas", layout="wide")

# --- INICIALIZAR LOG DE AUDITORÍA (PERSISTENTE EN LA SESIÓN) ---
if 'audit_log' not in st.session_state:
    st.session_state['audit_log'] = []

st.title("₿ Arbitraje Inteligente de Ciclo Infinito")
st.caption("Algoritmo de Grafos Bellman-Ford detectando ineficiencias en tiempo real.")

# --- SIDEBAR: CONFIGURACIÓN DE API ---
with st.sidebar:
    st.header("🔑 Configuración Binance")
    api_key = st.text_input("API Key", type="password")
    secret_key = st.text_input("Secret Key", type="password")
    st.divider()
    monto_operar = st.number_input("Capital USDT a utilizar", min_value=15.0, value=80.0, step=5.0)
    st.info("💡 Recuerda: El descuento de BNB (0.075%) es vital para rutas largas.")

# --- BLOQUE 1: MONITOR DE MERCADO (TOP 200) ---
st.subheader("📊 Monitor de Spreads Directos")
data_200 = get_crypto_opportunities()
if data_200:
    df = pd.DataFrame(data_200)
    st.dataframe(df.head(10), use_container_width=True, hide_index=True)
else:
    st.warning("No se pudieron cargar datos del monitor. Reintentando...")

st.divider()

# --- BLOQUE 2: ESCÁNER DE N-PUNTAS ---
st.header("🕸️ Buscador de Ciclos Indefinidos")

col1, col2 = st.columns([1, 2])

with col1:
    if st.button("🔍 ESCANEAR GRAFO DE BINANCE", use_container_width=True):
        if not api_key or not secret_key:
            st.warning("⚠️ Ingresa tus llaves API en el menú lateral.")
        else:
            with st.spinner("Analizando matrices de liquidez..."):
                res = buscar_ciclo_infinito(api_key, secret_key)
                
                if res['status'] == 'success':
                    st.session_state['ultima_ruta'] = res['ruta']
                    st.session_state['ultimo_roi'] = res['roi']
                    
                    st.metric("Mejor ROI Hallado", f"{res['roi']:.3f}%", 
                              delta="Rentable" if res['roi'] > 0.05 else "Bajo Margen")
                    
                    ruta_str = " ➡️ ".join(res['ruta'])
                    st.code(f"RUTA SUGERIDA: {ruta_str}", language="text")
                else:
                    st.info("No se hallaron ciclos rentables en este escaneo.")

with col2:
    if 'ultima_ruta' in st.session_state:
        st.write("### ⚡ Panel de Ejecución")
        st.write(f"Nodos en ruta: **{len(st.session_state['ultima_ruta'])}**")
        
        if st.button("🔥 EJECUTAR TRADE ATÓMICO", type="primary", use_container_width=True):
            with st.status("Lanzando órdenes al motor de Binance...", expanded=True) as status:
                inicio = time.time()
                ejecucion = ejecutar_ruta_dinamica(
                    api_key, secret_key, 
                    st.session_state['ultima_ruta'], 
                    monto_operar
                )
                fin = time.time()
                
                if ejecucion['status'] == 'success':
                    ganancia = float(ejecucion['final']) - monto_operar
                    status.update(label=f"✅ ¡Ciclo Completado en {fin-inicio:.2f}s!", state="complete")
                    st.balloons()
                    
                    # Guardar en el Log
                    st.session_state['audit_log'].append({
                        "Hora": time.strftime("%H:%M:%S"),
                        "Ruta": " -> ".join(st.session_state['ultima_ruta']),
                        "ROI %": f"{st.session_state['ultimo_roi']:.3f}%",
                        "Resultado": f"{ganancia:.4f} USDT"
                    })
                else:
                    status.update(label="❌ Fallo en ejecución", state="error")
                    st.error(ejecucion['message'])

# --- BLOQUE 3: REGISTRO DE OPERACIONES ---
st.divider()
st.subheader("📜 Log de Auditoría (Sesión Actual)")
if st.session_state['audit_log']:
    st.table(pd.DataFrame(st.session_state['audit_log']))
else:
    st.caption("Aún no se han ejecutado operaciones en esta sesión.")
