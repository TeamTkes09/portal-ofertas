import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
from pytrends.request import TrendReq
import urllib.parse
import random
import requests
import time

# 1. CONFIGURACIÓN DE SEGURIDAD Y PÁGINA
st.set_page_config(
    page_title="TechFlash Viral 🚀 Global",
    page_icon="📢",
    layout="wide"
)

# --- CAPA DE SEGURIDAD Y ANTI-CLON ---
st.html('''
    <meta name="google-site-verification" content="CkizRa_NBKko8N9KiS28aUkjKGkJbHlS3YI9htgLRRM" />
    <style>
        body { -webkit-user-select: none; user-select: none; }
        .share-btn { 
            display: inline-flex; align-items: center; justify-content: center;
            padding: 8px 12px; border-radius: 8px; color: white; 
            text-decoration: none; font-size: 14px; font-weight: bold; margin-right: 5px;
        }
        .whatsapp { background-color: #25D366; }
        .telegram { background-color: #0088cc; }
        .twitter { background-color: #1DA1F2; }
    </style>
''')

# 2. SISTEMA DE ACCESO (PROTECCIÓN)
if 'access_granted' not in st.session_state:
    st.session_state.access_granted = False

if not st.session_state.access_granted:
    st.title("🛡️ Portal de Tendencias Seguras")
    st.write("Verificando conexión segura... Haz clic para entrar.")
    if st.button("🔓 Acceder ahora"):
        st.session_state.access_granted = True
        st.rerun()
    st.stop()

# 3. BASE DE DATOS DE PAÍSES
PAISES_CONFIG = {
    "AR": {"name": "🇦🇷 Argentina", "pn": "argentina", "lang": "es", "amz": ".com.be"},
    "ES": {"name": "🇪🇸 España", "pn": "spain", "lang": "es", "amz": ".es"},
    "MX": {"name": "🇲🇽 México", "pn": "mexico", "lang": "es", "amz": ".com.mx"},
    "US": {"name": "🇺🇸 USA / Global", "pn": "united_states", "lang": "en", "amz": ".com"},
    "DEFAULT": {"name": "🇺🇸 Global", "pn": "united_states", "lang": "en", "amz": ".com"}
}

# 4. AUTODETECCIÓN DE IP
@st.cache_data(ttl=3600)
def detectar_ip_segura():
    try:
        res = requests.get('https://ipapi.co/json/', timeout=3).json()
        return PAISES_CONFIG.get(res.get('country_code'), PAISES_CONFIG["DEFAULT"])
    except: return PAISES_CONFIG["DEFAULT"]

if 'config' not in st.session_state:
    st.session_state.config = detectar_ip_segura()

# 5. SIDEBAR
with st.sidebar:
    st.title("🚀 Viral Panel")
    modo = st.radio("Tema", ["Oscuro", "Claro"])
    nombres = [v["name"] for v in PAISES_CONFIG.values()]
    idx = nombres.index(st.session_state.config["name"]) if st.session_state.config["name"] in nombres else 0
    seleccion = st.selectbox("Región:", nombres, index=idx)
    st.session_state.config = next(v for v in PAISES_CONFIG.values() if v["name"] == seleccion)
    st.divider()
    st.write("📢 ¡Comparte la web para crecer!")

# Colores dinámicos
card_bg = "#1d2129" if modo == "Oscuro" else "#f8f9fa"
txt_color = "#e0e0e0" if modo == "Oscuro" else "#1a1a1a"

# 6. MOTOR DE CONTENIDO (CON CACHE)
@st.cache_data(ttl=900)
def get_viral_data(conf):
    try:
        pytrends = TrendReq(hl=conf['lang'], tz=360)
        trends = pytrends.trending_searches(pn=conf['pn'])[0].tolist()[:6]
    except: trends = ["Tecnología", "Gadgets", "Ofertas"]

    results = []
    translator = GoogleTranslator(source='auto', target=conf['lang'])
    for t in trends:
        kw_enc = urllib.parse.quote(t)
        rss = f"https://news.google.com/rss/search?q={kw_enc}+deals&hl={conf['lang']}"
        feed = feedparser.parse(rss)
        if feed.entries:
            try:
                titulo = translator.translate(feed.entries[0].title.split(' - ')[0])
                results.append({
                    "titulo": titulo,
                    "url": feed.entries[0].link,
                    "amz": f"https://www.amazon{conf['amz']}/s?k={kw_enc}&tag=unlimited0f3-20",
                    "trend": t
                })
            except: continue
    return results

# 7. RENDERIZADO Y BOTONES VIRALES
st.title("⚡ TechFlash Viral")
st.caption(f"📍 Detectado en: {st.session_state.config['name']}")

data = get_viral_data(st.session_state.config)

for i, item in enumerate(data):
    st.markdown(f"""
    <div style="background:{card_bg}; padding:20px; border-radius:15px; border-left:6px solid #FF9900; margin-bottom:10px;">
        <small style="color:#888;">🔥 Tendencia: {item['trend']}</small>
        <h3 style="color:{txt_color};">{item['titulo']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Fila 1: Botones de Acción
    c1, c2 = st.columns(2)
    c1.link_button("📰 Leer Noticia", item['url'], use_container_width=True)
    c2.link_button("🛒 Ver Oferta", item['amz'], use_container_width=True)
    
    # Fila 2: Botones de Compartir (Viralización)
    st.write("📢 **Compartir esta oferta:**")
    
    # Preparar textos para compartir
    texto_share = urllib.parse.quote(f"¡Mira esta oferta de {item['trend']} en TechFlash! ⚡\n\n{item['titulo']}\n\nVer aquí: ")
    link_web = urllib.parse.quote("https://app-ofertas.streamlit.app/") # Cambia por tu link real
    
    share_col1, share_col2, share_col3, share_col4 = st.columns(4)
    
    with share_col1:
        st.markdown(f'<a href="https://wa.me/?text={texto_share}{link_web}" target="_blank" class="share-btn whatsapp">WhatsApp</a>', unsafe_allow_html=True)
    with share_col2:
        st.markdown(f'<a href="https://t.me/share/url?url={link_web}&text={texto_share}" target="_blank" class="share-btn telegram">Telegram</a>', unsafe_allow_html=True)
    with share_col3:
        st.markdown(f'<a href="https://twitter.com/intent/tweet?text={texto_share}&url={link_web}" target="_blank" class="share-btn twitter">X (Twitter)</a>', unsafe_allow_html=True)
    with share_col4:
        # Copiar link (Botón nativo de Streamlit)
        if st.button("🔗 Link", key=f"copy_{i}"):
            st.toast("¡Enlace listo para compartir!")
            st.code(f"https://app-ofertas.streamlit.app/")

    st.write("---")

st.caption("Sistema Viral Activo. © 2026 TechFlash Security.")
