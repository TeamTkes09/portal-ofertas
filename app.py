import streamlit as st
from utils import geo_logic
import data.products as products  # Importación segura
from components import header, news_feed, business_cards, business_table, footer

# 1. Configuración de página
st.set_page_config(
    page_title="TechFlash Pro | Arbitraje 2026",
    page_icon="⚡",
    layout="wide"
)

# 2. Cargar y Ordenar Datos por ROI (Rendimiento)
market = geo_logic.get_market_context()
suffix = market['s']

# Cargamos y ordenamos una sola vez al inicio
if 'oportunidades' not in st.session_state:
    raw_data = products.get_all_products()
    # Ordenar por ROI: (Venta - Costo) / Costo
    st.session_state.oportunidades = sorted(
        raw_data, 
        key=lambda x: ((x['v'] - x['c']) / x['c']), 
        reverse=True
    )

# 3. Control de Lazy Load
if 'items_to_show' not in st.session_state:
    st.session_state.items_to_show = 12  # Empezamos con 12 tarjetas

# 4. Renderizar Cabecera
header.render_hero(market['n'])

# 5. Sistema de Navegación
tab_biz, tab_news = st.tabs(["💰 OPORTUNIDADES DE NEGOCIO", "🌐 ACTUALIDAD TECNOLÓGICA"])

with tab_biz:
    col_v, col_spacer = st.columns([1, 2])
    with col_v:
        vista = st.radio(
            "Visualización:", 
            ["🎴 Tarjetas", "📑 Tabla Excel"], 
            horizontal=True,
            label_visibility="collapsed"
        )
    st.divider()

    if vista == "🎴 Tarjetas":
        # Solo mostramos la tajada (slice) actual del Lazy Load
        visibles = st.session_state.oportunidades[:st.session_state.items_to_show]
        
        # IMPORTANTE: Asegúrate de que business_cards acepte la lista 'visibles'
        business_cards.render_investment_section(suffix, visibles)
        
        # Botón Cargar Más (Solo si hay más productos para mostrar)
        if st.session_state.items_to_show < len(st.session_state.oportunidades):
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➕ MOSTRAR MÁS OPORTUNIDADES", use_container_width=True):
                st.session_state.items_to_show += 12
                st.rerun()
    else:
        # La tabla siempre muestra el 100% (es más eficiente para análisis)
        business_table.render_data_table(st.session_state.oportunidades, suffix)

with tab_news:
    news_feed.render_news_section(suffix=suffix)

footer.render_legal_bunker("TechFlash780")
