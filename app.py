# app.py
import streamlit as st
from data.products import get_all_products
from components.cards import render_investment_section
from styles.legal_templates import get_legal_disclaimer

# 1. Configuración de pantalla
st.set_page_config(page_title="Arbitrage Pro 2026", layout="wide")

# 2. Carga de datos
if 'data' not in st.session_state:
    st.session_state.data = get_all_products()

# 3. Encabezado Impactante
st.title("🚀 Portal de Arbitraje de Hardware")
st.markdown("---")

# 4. SECCIÓN DE FILTROS (Ahora en el cuerpo principal, no en el sidebar)
# Usamos columnas para que el buscador y el filtro de riesgo estén en la misma línea
col_search, col_risk = st.columns([2, 1])

with col_search:
    search_query = st.text_input("🔍 ¿Qué activo estás buscando hoy?", placeholder="Ej: SSD, DDR5, Corsair...", help="Busca por nombre o categoría").lower()

with col_risk:
    filtro_riesgo = st.multiselect(
        "Filtrar por Riesgo:",
        options=["BAJO", "MEDIO", "ALTO"],
        default=["BAJO", "MEDIO", "ALTO"]
    )

st.markdown("---")

# 5. Lógica de Filtrado
productos_filtrados = [
    p for p in st.session_state.data 
    if (search_query in p['n'].lower() or search_query in p['cat'].lower())
    and (p['r'] in filtro_riesgo)
]

# 6. Renderizado de resultados
if productos_filtrados:
    st.caption(f"Se han detectado {len(productos_filtrados)} activos con oportunidad de ganancia real.")
    render_investment_section(".com", productos_filtrados)
else:
    st.warning("⚠️ No hay activos que coincidan con tu búsqueda actual.")

# 7. Blindaje Legal al final
st.markdown(get_legal_disclaimer(), unsafe_allow_html=True)
