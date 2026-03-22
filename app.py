import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
from pytrends.request import TrendReq
import urllib.parse
import random
import requests  # Para la geolocalización

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="TechFlash AI 🤖 Autodetect",
    page_icon="📡",
    layout="wide"
)

# --- VERIFICACIÓN DE GOOGLE ---
st.html('<meta name="google-site-verification" content="CkizRa_NBKko8N9KiS28aUkjKGkJbHlS3YI9htgLRRM" />')

# 2. BASE DE DATOS DE PAÍSES
PAISES_CONFIG = {
    "AR": {"name": "🇦🇷 Argentina", "pn": "argentina", "lang": "es", "amz": ".com.be"},
    "ES": {"name": "🇪🇸 España", "pn": "spain", "lang": "es", "amz": ".es"},
    "MX": {"name": "🇲🇽 México", "pn": "mexico", "lang": "es", "amz": ".com.mx"},
    "US": {"name": "🇺🇸 USA / Global", "pn": "united_states", "lang": "en", "amz": ".com"},
    "BR": {"name": "🇧🇷 Brasil", "pn": "brazil", "lang": "pt", "amz": ".com.br"},
    "DEFAULT": {"name": "🇺🇸 Global", "pn": "united_states", "lang": "en", "amz": ".com"}
}

# 3. FUNCIÓN DE AUTODETECCIÓN (Mágica ✨)
def detectar_usuario():
    try:
        # Consultamos la IP del visitante (Servicio gratuito ipapi)
        response = requests.get('https://ipapi.co/json/', timeout=3).json()
        pais_code = response.get('country_code', 'US')
        idioma_pc = response.get('languages', 'en').split(',')[0][:2] # Ej: "es-AR" -> "es"
        
        # Si el país no está en nuestra lista, usamos Global
        config_sugerida = PAISES_CONFIG.get(pais_code, PAISES_CONFIG["DEFAULT"])
        return config_sugerida, idioma_pc
    except:
        return PAISES_CONFIG["DEFAULT"], "en"

# Inicializar sesión para que no se resetee al navegar
if 'user_config' not in st.session_state:
    st.session_state.user_config, st.session_state.user_lang = detectar_usuario()

# 4. SIDEBAR (Para cambios manuales)
with st.sidebar:
    st.title("Ajustes Inteligentes ⚙️")
    st.caption("Hemos detectado tu ubicación automáticamente, pero puedes cambiarla aquí:")
    
    # Buscamos el índice del país detectado para ponerlo por defecto
    lista_nombres = [v["name"] for v in PAISES_CONFIG.values()]
    try:
        idx_defecto = lista_nombres.index(st.session_state.user_config["name"])
    except:
        idx_defecto = 3 # USA por defecto si falla
        
    nuevo_pais_nombre = st.selectbox("Tu Región:", lista_nombres, index=idx_defecto)
    
    # Actualizar config si el usuario cambia el selectbox
    config = next(v for v in PAISES_CONFIG.values() if v["name"] == nuevo_pais_nombre)
    
    st.divider()
    modo = st.radio("Tema", ["Oscuro", "Claro"])

# Colores
bg = "#0e1117" if modo == "Oscuro" else "#ffffff"
card = "#1d2129" if modo == "Oscuro" else "#f8f9fa"
txt = "#e0e0e0" if modo == "Oscuro" else "#1a1a1a"

st.markdown(f"<style>.stApp {{ background-color: {bg}; color: {txt}; }} .trend-card {{ background: {card}; padding: 20px; border-radius: 15px; margin-bottom: 10px; border-left: 6px solid #FF9900; }}</style>", unsafe_allow_html=True)

# 5. MOTOR DE DATOS (LOCALIZADO)
@st.cache_data(ttl=900)
def obtener_data(pn_code, lang, suffix):
    try:
        pytrends = TrendReq(hl=lang, tz=360)
        trends = pytrends.trending_searches(pn=pn_code)[0].tolist()
        
        noticias_finales = []
        translator = GoogleTranslator(source='auto', target=lang)
        
        for t in trends[:6]:
            kw_enc = urllib.parse.quote(t)
            rss = f"https://news.google.com/rss/search?q={kw_enc}+deals&hl={lang}&gl={pn_code.upper()}"
            feed = feedparser.parse(rss)
            if feed.entries:
                entry = feed.entries[0]
                titulo = translator.translate(entry.title.split(' - ')[0])
                noticias_finales.append({
                    "titulo": titulo, "url": entry.link, 
                    "amz": f"https://www.amazon{suffix}/s?k={kw_enc}&tag=unlimited0f3-20",
                    "trend": t
                })
        return noticias_finales
    except:
        return []

# 6. RENDERIZADO
st.title("⚡ TechFlash AI")
st.subheader(f"Bienvenido. Hemos configurado tu edición de {config['name']} 🌎")

noticias = obtener_data(config['pn'], config['lang'], config['amz'])

if not noticias:
    st.warning("Estamos actualizando las tendencias. Por favor, refresca en unos segundos.")

for i, n in enumerate(noticias):
    with st.container():
        st.markdown(f"""
        <div class="trend-card">
            <small>🔥 Tendencia en tu zona: {n['trend']}</small>
            <h3>{n['titulo']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.link_button("📰 Leer Noticia", n['url'], use_container_width=True)
        c2.link_button("🛒 Oferta en Amazon", n['amz'], use_container_width=True)
        
        with st.expander("💬 Comunidad local"):
            st.feedback("stars", key=f"s_{i}")
            st.text_input("Deja un comentario:", key=f"t_{i}")
        st.write("---")

st.caption(f"Detección automática activa. IP Localizada. Edición: {config['name']}")
