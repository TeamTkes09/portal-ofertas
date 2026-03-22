import streamlit as st
# Importamos nuestros módulos locales
from data.products import get_all_products
from components.business_cards import render_investment_section

# 1. Configuración de la ventana del navegador
st.set_page_config(
    page_title="Arbitrage Tracker Pro 2026",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos CSS personalizados para mejorar la interfaz
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
    }
    stCaption {
        color: #94a3b8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Inicialización de Datos (Session State)
# Esto evita que la app recargue los datos cada vez que haces un clic
if 'oportunidades' not in st.session_state:
    raw_data = get_all_products()
    # Ordenamos por ROI por defecto: (Venta - Costo) / Costo
    st.session_state.oportunidades = sorted(
        raw_data, 
        key=lambda x: (x['v'] - x['c']) / x['c'], 
        reverse=True
    )

# 4. Barra Lateral (Sidebar) - Filtros y Configuración
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998614.png", width=80)
    st.title("Panel de Control")
    st.divider()
    
    search_query = st.text_input("🔍 Buscar activo (ej: SSD, DDR5)", "").lower()
    
    filtro_riesgo = st.multiselect(
        "Nivel de Riesgo",
        options=["BAJO", "MEDIO", "ALTO"],
        default=["BAJO", "MEDIO", "ALTO"]
    )
    
    st.divider()
    st.info("📅 Última actualización: Marzo 2026")

# 5. Cuerpo Principal de la App
st.title("🚀 Arbitraje de Hardware 2026")
st.subheader("Oportunidades de alta rentabilidad detectadas")

# 6. Lógica de Filtrado
productos_filtrados = [
    p for p in st.session_state.oportunidades 
    if (search_query in p['n'].lower() or search_query in p['cat'].lower())
    and p['r'] in filtro_riesgo
]

# 7. Renderizado de Componentes
if productos_filtrados:
    # Llamamos a la función de tarjetas que creamos en components/business_cards.py
    render_investment_section(".com", productos_filtrados)
else:
    st.warning("⚠️ No se encontraron activos que coincidan con tu búsqueda.")

# 8. Pie de página legal
st.divider()
st.caption("© 2026 Arbitrage Tracker Pro. Los precios mostrados son estimaciones de mercado y pueden variar según la disponibilidad.")
