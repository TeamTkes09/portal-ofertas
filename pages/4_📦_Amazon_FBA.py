import streamlit as st
from data.products import get_real_time_opportunities
from components.cards import render_investment_section

st.title("📦 Arbitraje Amazon FBA - Tecnología")
st.write("Comparativa de precios entre Amazon y mercados secundarios.")

pais = st.selectbox("Mercado", [".com", ".es", ".mx"])
productos = get_real_time_opportunities()

if productos:
    render_investment_section(pais, productos)
