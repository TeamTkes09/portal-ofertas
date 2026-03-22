import streamlit as st
from data.products import get_real_time_opportunities
from components.cards import render_investment_section

st.title("📦 Arbitraje Retail FBA")
st.write("Detección de productos tecnológicos subvaluados en Amazon vs eBay.")

productos = get_real_time_opportunities()
render_investment_section(".com", productos)
