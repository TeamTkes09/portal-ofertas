import streamlit as st
from utils import geo_logic
from data import products  # Importamos la base de datos central
from components import header, news_feed, business_cards, business_table, footer

# 1. Configuración de página
st.set_page_config(
    page_title="TechFlash Pro | Arbitraje de Hardware y IA 2026",
    page_icon="⚡",
    layout="wide"
)

# 2. Cargar contexto y datos
market = geo_logic.get_market_context()
suffix = market['s']
oportunidades = products.get_all_products()
# En app.py, después de cargar los productos:
oportunidades = products.get_all_products()

# ORDENAR POR ROI (De mayor a menor)
oportunidades = sorted(
    oportunidades, 
    key=lambda x: ((x['v'] - x['c']) / x['c']), 
    reverse=True
)
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
        # Usamos la lógica de tarjetas (ya filtrada internamente por tu business_cards)
        business_cards.render_investment_section(suffix)
    else:
        # Usamos la nueva vista de tabla interactiva
        business_table.render_data_table(oportunidades, suffix)

with tab_news:
    news_feed.render_news_section(suffix=suffix)

# 5. Footer
footer.render_legal_bunker("TechFlash780")
