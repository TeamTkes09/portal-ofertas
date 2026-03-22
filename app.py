import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
from pytrends.request import TrendReq
import pandas as pd

# 1. CONFIGURACIÓN ESTRATÉGICA (SEO Y DISEÑO)
st.set_page_config(
    page_title="LIVE Tech Trends ⚡ Ofertas Globales",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- VERIFICACIÓN DE PROPIEDAD DE GOOGLE (No borrar) ---
st.html('<meta name="google-site-verification" content="CkizRa_NBKko8N9KiS28aUkjKGkJbHlS3YI9htgLRRM" />')

# Estilos CSS Premium para Amazon/Tech
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; background-color: #FF9900; color: white; border: none; border-radius: 5px; font-weight: bold; height: 45px; }
    .stButton>button:hover { background-color: #e68a00; color: white; }
    .trend-card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin-bottom: 25px; border-top: 5px solid #ff4b4b; }
    .badge { background-color: #ff4b4b; color: white; padding: 4px 10px; border-radius: 50px; font-size: 11px; font-weight: bold; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

# 2. BARRA LATERAL: CONFIGURACIÓN MUNDIAL
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3858/3858693.png", width=80)
    st.header("🌐 Configuración Global")
    
    # Idioma del contenido
    idioma_nombre = st.selectbox("Idioma / Language", ["Español", "English", "Português", "Français", "Deutsch"])
    lang_map = {"Español": "es", "English": "en", "Português": "pt", "Français": "fr", "Deutsch": "de"}
    lang_code = lang_map[idioma_nombre]

    # Tienda de Amazon según país
    pais = st.selectbox("Tienda Amazon", ["USA (.com)", "España (.es)", "México (.com.mx)", "UK (.co.uk)"])
    suffix_map = {"USA (.com)": ".com", "España (.es)": ".es", "México (.com.mx)": ".com.mx", "UK (.co.uk)": ".co.uk"}
    amazon_suffix = suffix_map[pais]
    
    # Tu ID de Afiliado
    afiliado_id = "unlimited0f3-20"
    
    st.divider()
    st.info("Esta web detecta lo que el mundo busca en este segundo para ofrecerte las mejores ofertas.")

# 3. MOTORES DE BÚSQUEDA (TENDENCIAS Y NOTICIAS)
@st.cache_data(ttl=600) # Se actualiza cada 10 minutos
def obtener_tendencias_vivas():
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        # Obtenemos tendencias de búsqueda de EE.UU. (el mercado más fuerte)
        df = pytrends.trending_searches(pn='united_states')
        return df[0].tolist()
    except:
        # Fallback si Google Trends está saturado
        return ["iPhone 17", "Nvidia Blackwell", "PlayStation 6", "Amazon Prime Deals", "Smart Home Tech"]

def buscar_noticias_y_ofertas(keyword, target_lang):
    translator = GoogleTranslator(source='auto', target=target_lang)
    # Buscamos en Google News la tendencia + tech deals
    rss_url = f"https://news.google.com/rss/search?q={keyword}+technology+deals&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    
    items = []
    for entry in feed.entries[:2]: # 2 noticias potentes por tendencia
        try:
            titulo_original = entry.title.split(' - ')[0]
            titulo_traducido = translator.translate(titulo_original)
            # Link de Amazon optimizado para la tendencia
            link_amazon = f"https://www.amazon{amazon_suffix}/s?k={keyword}&tag={afiliado_id}"
            
            items.append({
                "titulo": titulo_traducido,
                "link_noticia": entry.link,
                "link_amazon": link_amazon,
                "keyword": keyword
            })
        except:
            continue
    return items

# 4. CUERPO PRINCIPAL DE LA WEB
st.title("🚀 TechFlash: Tendencias al Segundo")
st.markdown(f"Mostrando resultados para: **{pais}** en **{idioma_nombre}**")

# Capturar tendencias del momento
tendencias = obtener_tendencias_vivas()

# Layout de 2 columnas para noticias
col1, col2 = st.columns(2)

# Procesar las tendencias
for index, trend in enumerate(tendencias[:10]): # Analizamos las 10 principales
    noticias_trend = buscar_noticias_y_ofertas(trend, lang_code)
    
    with (col1 if index % 2 == 0 else col2):
        for noticia in noticias_trend:
            st.markdown(f"""
            <div class="trend-card">
                <span class="badge">Trending Now: {trend}</span>
                <h3 style="margin-top:10px;">{noticia['titulo']}</h3>
                <p style="color: #555; font-size: 0.9em;">Detectado en buscadores hace unos segundos.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Botones de acción
            btn_noticia, btn_amazon = st.columns(2)
            btn_noticia.link_button("📰 Ver Detalles", noticia['link_noticia'])
            btn_amazon.link_button("🛒 Ver en Amazon", noticia['link_amazon'])
            st.write("")

# Pie de página SEO
st.divider()
st.caption(f"© 2026 TechFlash Global. Optimizada para indexación instantánea en Google. Tienda: {pais}.")
