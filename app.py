import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse
import requests
import random

# 1. CONFIGURACIÓN DE PORTAL DINÁMICO
st.set_page_config(page_title="TechFlash Real-Time 🚀", page_icon="⚡", layout="wide")

# --- CREDENCIALES ---
MI_PAYPAL_USER = "TechFlash780"
AMZ_TAG = "unlimited0f3-20" 

# --- CSS: DISEÑO DE PORTAL (CONSERVAMOS EL ESTILO ELITE) ---
st.html('''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
        .stApp { background: #0c0f14; color: #ffffff; font-family: 'Inter', sans-serif; }
        .hero-banner {
            background: linear-gradient(45deg, #1e3a8a, #3b82f6);
            padding: 40px 20px; border-radius: 25px; text-align: center; margin-bottom: 30px;
        }
        .news-card {
            background: #161b22; padding: 20px; border-radius: 15px; 
            margin-bottom: 15px; border: 1px solid #30363d; transition: 0.3s;
        }
        .news-card:hover { border-color: #fbbf24; background: #1c2128; }
        .badge-live { background: #ef4444; color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; animation: blink 2s infinite; }
        @keyframes blink { 0% {opacity: 1;} 50% {opacity: 0.5;} 100% {opacity: 1;} }
    </style>
''')

# 2. MOTOR DE CONTENIDO REAL (Google News API via RSS)
@st.cache_data(ttl=600) # Se actualiza cada 10 minutos automáticamente
def obtener_noticias_reales(query, lang="es"):
    translator = GoogleTranslator(source='auto', target=lang)
    rss_url = f"https://news.google.com/rss/search?q={urllib.parse.quote(query)}&hl={lang}"
    feed = feedparser.parse(rss_url)
    noticias = []
    for entry in feed.entries[:4]: # Tomamos las 4 más frescas
        try:
            texto_limpio = entry.title.split(' - ')[0]
            noticias.append({
                "titulo": translator.translate(texto_limpio),
                "link": entry.link,
                "fuente": entry.source.get('title', 'Tech News')
            })
        except: continue
    return noticias

# 3. HEADER
st.markdown(f'''
    <div class="hero-banner">
        <h1 style="margin:0;">TECHFLASH <span style="color:#fbbf24;">LIVE</span></h1>
        <p>Noticias y Ofertas Reales filtradas por IA</p>
    </div>
''', unsafe_allow_html=True)

# 4. CUERPO: SECCIÓN HÍBRIDA
col_main, col_side = st.columns([2, 1])

with col_main:
    st.subheader("🌐 Última Hora en Tecnología")
    # Buscamos noticias reales de diferentes temas para que NO se repitan
    temas = ["inteligencia artificial", "nuevos lanzamientos tech", "hardware gaming"]
    
    for tema in temas:
        noticias_reales = obtener_noticias_reales(tema)
        if noticias_reales:
            n = noticias_reales[0] # Tomamos la mejor de cada tema
            st.markdown(f'''
                <div class="news-card">
                    <span class="badge-live">LIVE</span> 
                    <small style="color:#888; margin-left:10px;">Fuente: {n['fuente']}</small>
                    <h3 style="margin:10px 0; font-size:1.2rem;">{n['titulo']}</h3>
                    <a href="{n['link']}" target="_blank" style="color:#fbbf24; text-decoration:none; font-weight:bold;">Leer noticia completa →</a>
                </div>
            ''', unsafe_allow_html=True)

with col_side:
    st.subheader("🛒 Ofertas del Momento")
    # Aquí conectamos con Amazon basado en tendencias
    ofertas_queries = ["procesador", "teclado gamer", "monitor"]
    for q in ofertas_queries:
        url_amz = f"https://www.amazon.com/s?k={q}&tag={AMZ_TAG}"
        st.markdown(f'''
            <div style="background:#1e293b; padding:15px; border-radius:15px; margin-bottom:10px; border:1px solid #3b82f6;">
                <p style="margin:0; font-size:14px; font-weight:bold;">Mejor precio en: {q.capitalize()}</p>
                <a href="{url_amz}" target="_blank" style="display:block; margin-top:10px; background:#fbbf24; color:black; text-align:center; padding:8px; border-radius:8px; text-decoration:none; font-weight:bold; font-size:12px;">VER EN AMAZON</a>
            </div>
        ''', unsafe_allow_html=True)
    
    st.divider()
    st.link_button("☕ Donar a TechFlash780", f"https://www.paypal.me/{MI_PAYPAL_USER}", use_container_width=True)

st.caption("© 2026 TechFlash Real-Time Engine. Los datos se actualizan cada 10 minutos.")
