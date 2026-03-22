import streamlit as st
from data.products import get_crypto_opportunities, get_optimized_routes
from components.cards import render_crypto_section, render_optimized_selector

st.title("₿ Arbitraje Crypto & Redes")

# 1. Obtener datos reales de las 200 monedas
with st.spinner("Conectando con exchanges..."):
    data_200 = get_crypto_opportunities()
    rutas_opt = get_optimized_routes()

# 2. Renderizar la tabla principal
if data_200:
    render_crypto_section(data_200)
else:
    st.error("No se pudo cargar el Top 200. Revisa tu conexión.")

# 3. Renderizar el selector de 2, 3 y 4 puntas
st.divider()
render_optimized_selector(rutas_opt)

# 4. Guía de Arbitraje (El botón de más información que pediste)
with st.expander("❓ Guía: Cómo realizar el Loop de 4 puntas"):
    st.markdown("""
    1. **Identificación**: Busca rutas con ROI > 0.5% en el selector de arriba.
    2. **Fondeo**: Asegúrate de tener saldo en la moneda inicial (ej. USDT).
    3. **Ejecución**: Realiza los 4 intercambios dentro del mismo exchange.
    4. **Resultado**: El capital final regresa a USDT automáticamente sin pagar fees de retiro.
    """)
