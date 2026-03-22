import streamlit as st
from components import header, news_feed, business_cards, footer
from utils import geo_logic

# 1. Configuración Base
st.set_page_config(page_title="TechFlash780 Elite", layout="wide")

# 2. Cargar Inteligencia de Mercado (País/Amazon)
market = geo_logic.get_market_context()

# 3. Renderizar Header (Con aviso legal sutil arriba)
header.render_hero(market['n'])

# 4. Organización por Pestañas (Para que no falte nada)
tab1, tab2, tab3 = st.tabs(["💰 Arbitraje & Inversión", "🌐 Noticias Tech", "📊 Comparativas"])

with tab1:
    business_cards.render_investment_section(market['s'])

with tab2:
    news_feed.render_news_section()

with tab3:
    # Aquí puedes ir sumando tablas comparativas sin borrar lo anterior
    st.subheader("Tablas de Rendimiento")

# 5. Renderizar Footer (Blindaje Legal Total)
footer.render_legal_bunker()
