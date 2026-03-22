import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
from pytrends.request import TrendReq
import pandas as pd

# Configuración SEO Pro
st.set_page_config(
    page_title="LIVE Tech Trends ⚡ Ofertas al Segundo",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SISTEMA DE CAPTACIÓN DE TENDENCIAS EN TIEMPO REAL ---
@st.cache_data(ttl=300) # Se actualiza cada 5 minutos para no ser bloqueado
def obtener_tendencias_mundo():
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        # Captura las 20 tendencias de búsqueda que están explotando AHORA
        df = pytrends.trending_searches(pn='united_states') 
        return df[0].tolist()
    except:
        return ["iPhone 17", "Nvidia RTX", "Amazon Deals", "Tech Sales"]

# --- GENERADOR DE NOTICIAS BASADO EN TENDENCIAS ---
def buscar_noticias_tendencia(keyword, lang):
    translator = GoogleTranslator(source='auto', target=lang)
    # Buscamos en Google News específicamente la tendencia del segundo
    url = f"https://news.google.com/rss/search?q={keyword}+tech+deals&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    
    resultados = []
    for entry in feed.entries[:3]: # 3 noticias por cada tendencia
        try:
            titulo = translator.translate(entry.title)
            link_amazon = f"https://www.amazon.com/s?k={keyword}&tag=unlimited0f3-20"
            resultados.append({"titulo": titulo, "url": entry.link, "amazon": link_amazon})
        except:
            continue
    return resultados

# --- DISEÑO VISUAL ---
st.markdown("""
    <style>
    .trend-badge { background-color: #ff4b4b; color: white; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; margin-right: 5px; }
    .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 4px solid #ff4b4b; }
    </style>
""", unsafe_allow_html=True)

st.title("🔥 Tendencias Globales en Tiempo Real")
st.write("Esta página se auto-optimiza con lo que el mundo está buscando en este segundo.")

# 1. Mostrar las tendencias actuales (SEO Keywords)
tendencias = obtener_tendencias_mundo()
st.write("🚀 **Buscado ahora:** " + " ".join([f'<span class="trend-badge">{t}</span>' for t in tendencias[:8]]), unsafe_allow_html=True)

st.divider()

# 2. Mostrar noticias y ofertas de esas tendencias
col1, col2 = st.columns(2)
idioma_usuario = st.sidebar.selectbox("Idioma", ["es", "en", "pt", "fr"])

for i, trend in enumerate(tendencias[:10]):
    noticias = buscar_noticias_tendencia(trend, idioma_usuario)
    with (col1 if i % 2 == 0 else col2):
        for n in noticias:
            with st.container():
                st.markdown(f'<div class="card"><h3>{n["titulo"]}</h3><p>Tendencia detectada: <b>{trend}</b></p></div>', unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                c1.link_button("📰 Leer más", n['url'])
                c2.link_button("🛒 Oferta en Amazon", n['amazon'])
                st.write("")

st.caption("Optimizando para Google Bot... Indexación en curso.")
