import streamlit as st
import feedparser
from deep_translator import GoogleTranslator

# Configuración de la página Pro Global
st.set_page_config(page_title="TechFlash Global ⚡", page_icon="🌐", layout="wide")

# Estilo CSS para que se vea premium
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; background-color: #FF9900; color: white; border-radius: 8px; font-weight: bold; }
    .news-card { padding: 20px; border-radius: 15px; background: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; border-left: 5px solid #FF9900; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL: CONFIGURACIÓN MUNDIAL ---
with st.sidebar:
    st.header("🌐 Configuración Global")
    
    # Selector de Idioma
    idioma = st.selectbox("Selecciona tu idioma / Select Language", 
                         ["Español", "English", "Português", "Français", "Deutsch"])
    lang_code = {"Español": "es", "English": "en", "Português": "pt", "Français": "fr", "Deutsch": "de"}[idioma]

    # Selector de Tienda Amazon (Aquí podés poner tus IDs de cada país)
    pais = st.selectbox("Tienda Amazon / Amazon Store", ["Amazon USA (.com)", "Amazon España (.es)", "Amazon México (.com.mx)"])
    amazon_suffix = {"Amazon USA (.com)": ".com", "Amazon España (.es)": ".es", "Amazon México (.com.mx)": ".com.mx"}[pais]
    
    # Tu ID de afiliado (Podes usar el mismo para empezar o diferentes si tenés)
    afiliado_id = "unlimited0f3-20" 

st.title("⚡ TechFlash Global News")
st.subheader(f"Las mejores noticias y ofertas en {idioma}")

# --- FUNCIÓN DE TRADUCCIÓN Y NOTICIAS ---
@st.cache_data(ttl=3600)
def get_global_news(target_lang):
    # Usamos el RSS de Google News Tech para tener variedad mundial
    rss_url = f"https://news.google.com/rss/search?q=technology+deals&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    translator = GoogleTranslator(source='auto', target=target_lang)
    noticias = []
    
    for entry in feed.entries[:12]: # Tomamos las 12 más frescas
        try:
            titulo_traducido = translator.translate(entry.title)
            # Limpiamos el título para la búsqueda en Amazon
            busqueda_amazon = entry.title.split('-')[0].strip()
            link_amazon = f"https://www.amazon{amazon_suffix}/s?k={busqueda_amazon}&tag={afiliado_id}"
            
            noticias.append({
                "titulo": titulo_traducido,
                "link_original": entry.link,
                "link_amazon": link_amazon,
                "fecha": entry.published
            })
        except:
            continue
    return noticias

# --- MOSTRAR NOTICIAS EN GRILLA ---
news = get_global_news(lang_code)

col1, col2 = st.columns(2)

for i, item in enumerate(news):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
        <div class="news-card">
            <h4>{item['titulo']}</h4>
            <p style="font-size: 0.8rem; color: gray;">{item['fecha']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("📰 Leer Noticia", item['link_original'])
        with c2:
            st.link_button("🛒 Ver Oferta Amazon", item['link_amazon'])
        st.write("---")

st.caption("TechFlash Global © 2026 - Generando ingresos automáticos en todo el mundo.")
