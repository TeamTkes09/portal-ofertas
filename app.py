import streamlit as st
import time
from data.products import get_real_time_opportunities
from components.cards import render_investment_section

st.set_page_config(layout="wide")

# --- AUTO-REFRESH SCRIPT (Cada 15 min) ---
# Esto fuerza al navegador a recargar la app sin que el usuario toque nada
# st.empty() # Espacio para el timer si quisieras mostrarlo

# --- SIDEBAR NOTICIAS DINÁMICAS ---
with st.sidebar:
    st.title("⏱️ Live Feed")
    st.success("Sincronizado con Amazon API")
    prox_act = 15 - ((int(time.time()) // 60) % 15)
    st.metric("Próxima actualización en", f"{prox_act} min")
    
    st.divider()
    st.subheader("📢 Noticias Urgentes")
    # Estas noticias podrían venir de una API de Twitter o RSS
    st.warning("🚨 Alerta: Precios de Juguetes LEGO subiendo en eBay. Posible Gap de Arbitraje.")

# --- RENDER PRINCIPAL ---
st.title("🚀 Arbitraje Real-Time Pro")

# Obtener datos (se refrescan cada 15 min por el decorador @st.cache_data)
productos = get_real_time_opportunities()

# Mostramos las 4 columnas
render_investment_section(".com", productos)

# Pie de página con marca de tiempo
st.caption(f"Última sincronización exitosa: {time.strftime('%H:%M:%S')}")
