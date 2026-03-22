import streamlit as st
from utils import geo_logic
import data.products as products  # Importación centralizada
from components import header, news_feed, business_cards, business_table, footer

# 1. Configuración de página
st.set_page_config(
    page_title="TechFlash Pro | Arbitraje 2026",
    page_icon="⚡",
    layout="wide"
)

# 2. Gestión de Datos y Memoria de Sesión (Session State)
market = geo_logic.get_market_context()
suffix = market['s']

# Cargamos y ordenamos los datos una sola vez por sesión
if 'oportunidades' not in st.session_state:
    raw_data = products.get_all_products()
    # Ordenamos por ROI de mayor a menor: (Venta - Costo) / Costo
    st.session_state.oportunidades = sorted(
        raw_data, 
        key=lambda x: ((x['v'] - x['c']) / x['c']), 
        reverse=True
    )

# Control de cuántos productos mostrar (Lazy Load)
if 'items_to_show' not in st.session_state:
    st.session_state.items_to_show = 12  # Cantidad inicial

# 3. Renderizar Cabecera
header.render_hero(market['n'])

# 4. Sistema de Navegación por Pestañas
tab_biz, tab_news = st.tabs(["💰 OPORTUNIDADES DE NEGOCIO", "🌐 ACTUALIDAD TECNOLÓGICA"])

with tab_biz:
    # --- SELECTOR DE VISTA ---
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
        # Extraemos solo la porción de productos según el Lazy Load
        productos_visibles = st.session_state.oportunidades[:st.session_state.items_to_show]
        
        # Renderizamos las tarjetas pasándole la lista filtrada
        business_cards.render_investment_section(suffix, productos_visibles)
        
        # BOTÓN LAZY LOAD: Solo aparece si hay más productos que mostrar
        if st.session_state.items_to_show < len(st.session_state.oportunidades):
            st.markdown("<br>", unsafe_allow_html=True)
            col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 2, 1])
            with col_btn_2:
                if st.button("➕ MOSTRAR MÁS OPORTUNIDADES", use_container_width=True):
                    st.session_state.items_to_show += 12
                    st.rerun() # Refresca para mostrar los nuevos items
    else:
        # En la Vista Pro (Tabla), mostramos el 100% para facilitar el análisis profundo
        business_table.render_data_table(st.session_state.oportunidades, suffix)

with tab_news:
    # Las noticias se mantienen fijas o con su propia lógica
    news_feed.render_news_section(suffix=suffix)

# 5. Footer Profesional
footer.render_legal_bunker("TechFlash780")
