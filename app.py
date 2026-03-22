import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
from pytrends.request import TrendReq
import pandas as pd
import urllib.parse

# 1. CONFIGURACIÓN DE PÁGINA Y SEO
st.set_page_config(
    page_title="TechFlash Global ⚡ Tendencias",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- VERIFICACIÓN DE GOOGLE (No tocar) ---
st.html('<meta name="google-site-verification" content="CkizRa_NBKko8N9KiS28aUkjKGkJbHlS3YI9htgLRRM" />')

# 2. SELECTOR DE MODO (Día/Noche) Y CONFIGURACIÓN MUNDIAL EN SIDEBAR
with st.sidebar:
    st.title("Settings ⚙️")
    modo = st.radio("Modo de Visibilidad", ["☀️ Claro", "🌙 Oscuro"])
    
    st.divider()
    idioma_nombre = st.selectbox("Idioma / Language", ["Español", "English", "Português", "Français", "Deutsch"])
    pais = st.selectbox("Tienda Amazon", ["USA (.com)", "España (.es)", "México (.com.mx)", "UK (.co.uk)"])
    
    lang_map = {"Español": "es", "English": "en", "Português": "pt", "Français": "fr", "Deutsch": "de"}
    suffix_map = {"USA (.com)": ".com", "España (.es)": ".es", "México (.com.mx)": ".com.mx", "UK (.co.uk)": ".co.uk"}
    
    lang_code = lang_map[idioma_nombre]
    amazon_suffix = suffix_map[pais]
    afiliado_id = "unlimited0f3-20"

# 3. ESTILOS ADAPTATIVOS (PC Y MÓVIL) + MODO OSCURO
bg_color = "#ffffff" if modo == "☀️ Claro" else "#0e1117"
card_bg = "#f8f9fa" if modo == "☀️ Claro" else "#1d2129"
text_color = "#1a1a1a" if modo == "☀️ Claro" else "#e0e0e0"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; color: {text_color}; }}
    
    /* Estilo de Tarjetas Adaptativas */
    .trend-card {{
        background: {card_bg};
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 6px solid #FF9900;
        transition: transform 0.2s;
    }}
    
    /* Optimización para Celulares */
    @media (max-width: 640px) {{
        .trend-card {{ padding: 10px; margin-bottom: 15px; }}
        h3 {{ font-size: 1.1rem !important; }}
        .stButton>button {{ height: 50px !important; font-size: 16px !important; }}
    }}

    .badge {{ background-color: #ff4b4b; color: white; padding: 3px 8px; border-radius: 10px; font-size: 10px; font-weight: bold; }}
    h3 {{ color: {text_color}; }}
    </style>
""", unsafe_allow_html=True)

# 4. FUNCIONES DE DATOS
@st.cache_data(ttl=600)
def obtener_tendencias():
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        df = pytrends.trending_searches(pn='united_states')
        return df[0].tolist()
    except:
        return ["AI Tech", "Smartphones 2026", "Gaming Gear", "Home Automation"]

def buscar_noticias(keyword, target_lang):
    keyword_encoded = urllib.parse.quote(keyword)
    translator = GoogleTranslator(source='auto', target=target_lang)
    rss_url = f"https://news.google.com/rss/search?q={keyword_encoded}+tech+deals&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    items = []
    for entry in feed.entries[:2]:
        try:
            titulo = translator.translate(entry.title.split(' - ')[0])
            link_amz = f"https://www.amazon{amazon_suffix}/s?k={keyword_encoded}&tag={afiliado_id}"
            items.append({"titulo": titulo, "url": entry.link, "amazon": link_amz, "trend": keyword})
        except: continue
    return items

# 5. RENDERIZADO DE LA WEB
st.title("⚡ TechFlash Global")
st.write(f"🌍 **Región:** {pais} | 🗣️ **Idioma:** {idioma_nombre}")

tendencias = obtener_tendencias()

# Usamos contenedores para que Streamlit maneje el responsive automáticamente
for index, trend in enumerate(tendencias[:12]):
    noticias = buscar_noticias(trend, lang_code)
    
    for noticia in noticias:
        with st.container():
            st.markdown(f"""
            <div class="trend-card">
                <span class="badge">🔥 TOP TREND: {noticia['trend']}</span>
                <h3>{noticia['titulo']}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Botones en formato 1 columna para móvil y 2 para PC
            col_btn1, col_btn2 = st.columns([1, 1])
            with col_btn1:
                st.link_button("📖 Leer Noticia", noticia['url'])
            with col_btn2:
                st.link_button("🛒 Ver Oferta", noticia['amazon'])
            st.write("")

st.divider()
st.caption("Optimizada para dispositivos móviles y escritorio. © 2026 TechFlash.")
