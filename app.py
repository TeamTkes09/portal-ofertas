import streamlit as st
from utils import geo_logic
from components import header, news_feed, business_cards, footer

# 1. Configuración inicial
st.set_page_config(page_title="TechFlash780 Elite", page_icon="💎", layout="wide")

# 2. Obtener contexto de mercado
market = geo_logic.get_market_context()

# 3. Renderizar Header
header.render_hero(market['n'])

# 4. Pestañas
tab_biz, tab_news = st.tabs(["💰 NEGOCIOS", "🌐 NOTICIAS"])

with tab_biz:
    # LLAMADA LIMPIA: Aquí es donde se ejecutan las tarjetas
    business_cards.render_investment_section(market['s'])

with tab_news:
    news_feed.render_news_section()

# 5. Footer
footer.render_legal_bunker("TechFlash780")
