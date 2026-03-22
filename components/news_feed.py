import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse

def render_news_section():
    st.subheader("🌐 TechFlash Live")
    temas = ["IA", "Hardware"]
    cols = st.columns(len(temas))
    
    for i, tema in enumerate(temas):
        with cols[i]:
            st.write(f"**🔥 {tema}**")
            # Simulación simple para evitar errores de red mientras testeamos
            st.info(f"Cargando noticias de {tema}...")

@st.cache_data(ttl=600)
def fetch_data(query):
    # Lógica de noticias...
    return []
