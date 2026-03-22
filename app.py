import streamlit as st
# IMPORTANTE: Verifica que los nombres coincidan exactamente
try:
    from data.products import get_real_time_opportunities, get_news_events, get_crypto_opportunities
    from components.cards import render_investment_section, render_crypto_section
except Exception as e:
    st.error(f"Error de Importación: {e}")

st.title("Portal de Arbitraje")

tab1, tab2, tab3 = st.tabs(["Noticias", "Productos", "Crypto"])

with tab1:
    evs = get_news_events()
    st.write(evs[0]['titulo'])
    render_investment_section(".com", evs[0]['productos_asociados'])

with tab2:
    prods = get_real_time_opportunities()
    render_investment_section(".com", prods)

with tab3:
    cryptos = get_crypto_opportunities()
    render_crypto_section(cryptos)
