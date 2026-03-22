import streamlit as st

st.set_page_config(
    page_title="Sistema de Arbitraje 2026",
    page_icon="🚀",
    layout="wide"
)

# Esto es lo que ves ahora
with st.sidebar:
    st.title("🧭 Navegación")
    st.info("Selecciona una sección arriba para operar.")
    st.divider()
    st.caption("🚀 Datos en tiempo real via API")

st.title("Bienvenido al Sistema de Arbitraje Pro")
st.write("👈 Selecciona una pestaña en el menú de la izquierda para comenzar.")
