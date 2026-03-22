import streamlit as st

st.set_page_config(
    page_title="Sistema de Arbitraje Multisectorial 2026",
    page_icon="🚀",
    layout="wide"
)

# Título común para todas las páginas (opcional)
st.sidebar.title("🧭 Navegación")
st.sidebar.info("Selecciona una sección para operar.")

# Mensaje de bienvenida en el Sidebar
st.sidebar.markdown("---")
st.sidebar.caption("Datos en tiempo real via API")
