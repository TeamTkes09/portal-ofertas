import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse

def render_news_section():
    st.subheader("🌐 TechFlash Live: Noticias al Instante")
    
    # Definimos los temas de interés para que no se repitan
    temas = ["inteligencia artificial", "lanzamientos hardware", "gaming tech"]
    
    cols = st.columns(len(temas))
    
    for i, tema in enumerate(temas):
        with cols[i]:
            st.markdown(f"**🔥 {tema.upper()}**")
            noticias = fetch_data(tema)
            for n in noticias:
                st.markdown(f'''
                    <div style="background: #111827; padding: 15px; border-radius: 10px; border: 1px solid #1f2937; margin-bottom: 10px;">
                        <small style="color: #3b82f6;">{n['fuente']}</small>
                        <p style="margin: 5px 0; font-size: 14px; font-weight: 600;">{n['titulo']}</p>
                        <a href="{n['link']}" target="_blank" style="color: #fbbf24; text-decoration: none; font-size: 12px;">Ver noticia →</a>
                    </div>
                ''', unsafe_allow_html=True)

@st.cache_data(ttl=600) # Actualiza noticias cada 10 minutos
def fetch_data(query):
    try:
        translator = GoogleTranslator(source='auto', target='es')
        rss_url = f"https://news.google.com/rss/search?q={urllib.parse.quote(query)}&hl=es"
        feed = feedparser.parse(rss_url)
        
        resultados = []
        for entry in feed.entries[:3]: # Solo las 3 mejores de cada tema
            titulo_es = translator.translate(entry.title.split(' - ')[0])
            resultados.append({
                "titulo": titulo_es,
                "link": entry.link,
                "fuente": entry.source.get('title', 'Fuente Tech')
            })
        return resultados
    except:
        return []
 target_col.markdown(html_card, unsafe_allow_html=True)
