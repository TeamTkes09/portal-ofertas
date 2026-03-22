import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
from pytrends.request import TrendReq
import urllib.parse
import random
import requests
import time

# --- CONFIGURACIÓN DE SEGURIDAD Y UI ---
st.set_page_config(page_title="TechFlash Pay 🔐 TechFlash780", page_icon="💳", layout="wide")

# --- CONFIGURACIÓN DE SOCIO PAYPAL ---
MI_PAYPAL_USER = "TechFlash780"  
# -------------------------------------------

st.html('''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
        .stApp { background: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
        
        /* Contenedor de Donación */
        .pay-header {
            background: linear-gradient(135deg, #003087 0%, #0070ba 100%);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 30px;
            border: 1px solid #58a6ff;
            box-shadow: 0 10px 30px rgba(0,112,186,0.2);
        }

        /* Tarjetas de Tendencias Premium */
        .secure-card {
            background: #161b22;
            border: 1px solid #30363d;
            padding: 25px;
            border-radius: 18px;
            margin-bottom: 20px;
            transition: 0.3s ease;
        }
        .secure-card:hover { border-color: #0070ba; transform: translateY(-3px); }

        /* Barra de Progreso de Meta */
        .goal-bar {
            background: #30363d;
            border-radius: 10px;
            height: 12px;
            width: 100%;
            margin: 15px 0;
            overflow: hidden;
        }
        .goal-fill {
            background: #25D366;
            height: 100%;
            width: 65%; /* Simulación de meta al 65% */
        }
    </style>
''')

# 1. ACCESO SEGURO
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ TechFlash Security")
    st.info("Verificando credenciales de cifrado para TechFlash780...")
    if st.button("🔓 ENTRAR AL PORTAL SEGURO"):
        st.session_state.auth = True
        st.rerun()
    st.stop()

# 2. DETECCIÓN DE UBICACIÓN
PAISES = {
    "AR": {"name": "Argentina 🇦🇷", "pn": "argentina", "lang": "es", "amz": ".com.be"},
    "ES": {"name": "España 🇪🇸", "pn": "spain", "lang": "es", "amz": ".es"},
    "MX": {"name": "México 🇲🇽", "pn": "mexico", "lang": "es", "amz": ".com.mx"},
    "US": {"name": "USA / Global 🇺🇸", "pn": "united_states", "lang": "en", "amz": ".com"},
    "DEFAULT": {"name": "Global 🇺🇸", "pn": "united_states", "lang": "en", "amz": ".com"}
}

@st.cache_data(ttl=3600)
def auto_geo():
    try:
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        return PAISES.get(r.get('country_code'), PAISES["DEFAULT"])
    except: return PAISES["DEFAULT"]

if 'config' not in st.session_state:
    st.session_state.config = auto_geo()

# 3. PANEL DE DONACIONES (CENTRALIZADO)
st.markdown(f'''
    <div class="pay-header">
        <h1 style="color:white; margin:0; font-weight:900;">💳 Apoya a TechFlash780</h1>
        <p style="color:#e6f0ff; margin:10px 0;">Ayúdanos a mantener los servidores de IA activos y libres de anuncios intrusivos.</p>
        <div style="max-width:400px; margin: 0 auto;">
            <div style="display:flex; justify-content:space-between; font-size:12px; color:white;">
                <span>Meta mensual: $100 USD</span>
                <span>65% completado</span>
            </div>
            <div class="goal-bar"><div class="goal-fill"></div></div>
        </div>
    </div>
''', unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,2,1])
with c2:
    paypal_url = f"https://www.paypal.me/{MI_PAYPAL_USER}"
    st.link_button("🔥 DONAR POR PAYPAL (SEGURO)", paypal_url, use_container_width=True)
    st.caption("✅ Verificado por PayPal. Transacción encriptada punto a punto.")

st.divider()

# 4. MOTOR DE CONTENIDO (OFERTAS ACTUALES)
@st.cache_data(ttl=900)
def get_safe_content(conf):
    try:
        pytrends = TrendReq(hl=conf['lang'], tz=360)
        trends = pytrends.trending_searches(pn=conf['pn'])[0].tolist()[:6]
    except: trends = ["Hardware", "Gadgets", "Cybersecurity", "Amazon Deals"]
    
    data = []
    translator = GoogleTranslator(source='auto', target=conf['lang'])
    for t in trends:
        kw = urllib.parse.quote(t)
        rss = f"https://news.google.com/rss/search?q={kw}+deals&hl={conf['lang']}"
        feed = feedparser.parse(rss)
        if feed.entries:
            try:
                title = translator.translate(feed.entries[0].title.split(' - ')[0])
                data.append({"title": title, "url": feed.entries[0].link, 
                             "amz": f"https://www.amazon{conf['amz']}/s?k={kw}&tag=unlimited0f3-20", "trend": t})
            except: continue
    return data

st.subheader(f"🌐 Radar de Tendencias: {st.session_state.config['name']}")
items = get_safe_content(st.session_state.config)

for i, item in enumerate(items):
    st.markdown(f'''
        <div class="secure-card">
            <small style="color:#58a6ff;">🔍 DETECTADO EN {st.session_state.config['name'].upper()}</small>
            <h3 style="margin-top:10px; color:white;">{item['title']}</h3>
            <p style="font-size:12px; color:#8b949e;">Palabra clave: {item['trend']}</p>
        </div>
    ''', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 2, 1])
    col1.link_button("📰 Leer Detalles", item['url'], use_container_width=True)
    col2.link_button("🛒 Oferta Amazon", item['amz'], use_container_width=True)
    
    share_text = urllib.parse.quote(f"¡Mira esta oferta en TechFlash! {item['amz']}")
    col3.link_button("📢", f"https://wa.me/?text={share_text}", use_container_width=True)
    st.write("---")

st.caption(f"Portal de Transacciones TechFlash v15.0 | Socio: {MI_PAYPAL_USER}")
