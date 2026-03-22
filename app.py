import streamlit as st
from utils import geo_logic
from components import header, news_feed, business_cards, footer

# 1. Configuración de página (Debe ser la primera instrucción)
st.set_page_config(
    page_title="TechFlash780 Elite",
    page_icon="💎",
    layout="wide"
)

# 2. Cargar contexto de mercado (País y Amazon)
market = geo_logic.get_market_context()

# 3. Renderizar Cabecera y Aviso Legal Superior
header.render_hero(market['n'])

# 4. Sistema de Navegación por Pestañas
tab_biz, tab_news = st.tabs(["💰 OPORTUNIDADES DE NEGOCIO", "🌐 ACTUALIDAD TECNOLÓGICA"])

with tab_biz:
    # Renderiza las tarjetas de inversión con el sufijo de Amazon detectado
    business_cards.render_investment_section(market['s'])

with tab_news:
    # Renderiza el motor de noticias en tiempo real
    news_feed.render_news_section()

# 5. Renderizar Footer y Blindaje Legal Final
footer.render_legal_bunker("TechFlash780")
