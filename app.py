import streamlit as st
from utils import geo_logic
from components import header, news_feed, business_cards, footer

# 1. Configuración obligatoria (debe ser la primera línea)
st.set_page_config(page_title="TechFlash780 Elite", page_icon="💎", layout="wide")

# 2. Cargar datos del mercado
market = geo_logic.get_market_context()

# 3. Renderizar Header
header.render_hero(market['n'])

# 4. Organización por Pestañas
tab_biz, tab_news = st.tabs(["💰 OPORTUNIDADES DE NEGOCIO", "🌐 ACTUALIDAD TECNOLÓGICA"])

with tab_biz:
    # Aquí llamamos a la función. 
    # Asegúrate de que business_cards.py use st.markdown(..., unsafe_allow_html=True)
    business_cards.render_investment_section(market['s'])

with tab_news:
    news_feed.render_news_section()

# 5. Footer Legal
footer.render_legal_bunker("TechFlash780")
 target_col.markdown(html_card, unsafe_allow_html=True)
