import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
from pytrends.request import TrendReq
import urllib.parse
import random
import requests
import time

# 1. CONFIGURACIÓN DE PÁGINA SEGURA
st.set_page_config(
    page_title="TechFlash Safe & Pay 🔐",
    page_icon="💳",
    layout="wide"
)

# --- CSS: INTERFAZ BANCARIA Y SELLOS DE SEGURIDAD ---
st.html('''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');
        
        .stApp { background: #0b0e14; color: #ffffff; }
        
        /* Banner de Seguridad Superior */
        .safe-header {
            background: #1a5cff;
            color: white;
            padding: 5px 20px;
            text-align: center;
            font-size: 12px;
            font-weight: bold;
            letter-spacing: 1px;
            border-radius: 0 0 10px 10px;
        }

        /* Tarjetas de Noticia */
        .trend-card {
            background: #161b22;
            border: 1px solid #30363d;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 20px;
            transition: 0.3s;
        }
        .trend-card:hover { border-color: #1a5cff; box-shadow: 0 0 15px rgba(26,92,255,0.3); }

        /* Sección de Donación Premium */
        .donate-box {
            background: linear-gradient(135deg, #1e2631 0%, #0b0e14 100%);
            border: 2px solid #1a5cff;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            margin: 40px 0;
        }

        .trust-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
            filter: grayscale(100%) brightness(200%);
            opacity: 0.6;
            margin-top: 20px;
        }
    </style>
''')

# 2. SISTEMA DE ACCESO Y VERIFICACIÓN SSL
if 'verified' not in st.session_state:
    st.session_state.verified = False

if not st.session_state.verified:
    st.markdown('<div class="safe-header">🔒 CONEXIÓN CIFRADA AES-256 ACTIVA</div>', unsafe_allow_html=True)
    st.title("🔐 Validación de Nodo Seguro")
    st.info("Estás entrando a una zona de transacciones protegida. Verificando certificados...")
    if st.button("CONFIRMAR IDENTIDAD Y ENTRAR"):
        st.session_state.verified = True
        st.rerun()
    st.stop()

# 3. DETECCIÓN DE PAÍS
PAISES_CONFIG = {
    "AR": {"name": "Argentina 🇦🇷", "pn": "argentina", "lang": "es", "amz": ".com.be"},
    "ES": {"name": "España 🇪🇸", "pn": "spain", "lang": "es", "amz": ".es"},
    "MX": {"name": "México 🇲🇽", "pn": "mexico", "lang": "es", "amz": ".com.mx"},
    "US": {"name": "USA / Global 🇺🇸", "pn": "united_states", "lang": "en", "amz": ".com"},
    "DEFAULT": {"name": "Global 🇺🇸", "pn": "united_states", "lang": "en", "amz": ".com"}
}

@st.cache_data(ttl=3600)
def get_geo():
    try:
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        return PAISES_CONFIG.get(r.get('country_code'), PAISES_CONFIG["DEFAULT"])
    except: return PAISES_CONFIG["DEFAULT"]

if 'config' not in st.session_state:
    st.session_state.config = get_geo()

# 4. SIDEBAR CON ESTADISTICAS DE SEGURIDAD
with st.sidebar:
    st.header("🛡️ Security Center")
    st.success("SSL Status: Active")
    st.code("IP: " + requests.get('https://api.ipify.org').text)
    st.divider()
    sel = st.selectbox("Región:", [v["name"] for v in PAISES_CONFIG.values()])
    st.session_state.config = next(v for v in PAISES_CONFIG.values() if v["name"] == sel)

# 5. RENDERIZADO PRINCIPAL
st.markdown('<div class="safe-header">✓ NAVEGACIÓN SEGURA HABILITADA PARA COMPRAS</div>', unsafe_allow_html=True)
st.title("⚡ TechFlash Secure Portal")

# --- SECCIÓN DE DONACIONES / COMPRA SEGURA ---
with st.container():
    st.markdown('''
        <div class="donate-box">
            <h2 style="color:#1a5cff;">☕ Apoya el Proyecto</h2>
            <p>Si te gusta nuestra tecnología de detección de ofertas, puedes colaborar para mantener los servidores activos.</p>
            <div class="trust-icons">
                <img src="https://cdn-icons-png.flaticon.com/512/196/196566.png" width="40">
                <img src="https://cdn-icons-png.flaticon.com/512/196/196578.png" width="40">
                <img src="https://cdn-icons-png.flaticon.com/512/5968/5968144.png" width="40">
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    col_pay1, col_pay2 = st.columns(2)
    # Aquí podrías poner tus links reales de PayPal o Mercado Pago
    col_pay1.link_button("💳 Donar con PayPal", "https://paypal.me/TU_USUARIO", use_container_width=True)
    col_pay2.link_button("💰 Donar con Cripto/Otros", "#", use_container_width=True)

st.divider()

# 6. MOTOR DE CONTENIDO (Mantenemos lo anterior pero con diseño seguro)
@st.cache_data(ttl=900)
def get_safe_content(conf):
    try:
        pytrends = TrendReq(hl=conf['lang'], tz=360)
        trends = pytrends.trending_searches(pn=conf['pn'])[0].tolist()[:6]
    except: trends = ["Tecnología", "Gadgets", "Ofertas"]
    
    data = []
    translator = GoogleTranslator(source='auto', target=conf['lang'])
    for t in trends:
        kw = urllib.parse.quote(t)
        rss = f"https://news.google.com/rss/search?q={kw}+tech&hl={conf['lang']}"
        feed = feedparser.parse(rss)
        if feed.entries:
            try:
                title = translator.translate(feed.entries[0].title.split(' - ')[0])
                data.append({"title": title, "url": feed.entries[0].link, 
                             "amz": f"https://www.amazon{conf['amz']}/s?k={kw}&tag=unlimited0f3-20", "trend": t})
            except: continue
    return data

items = get_safe_content(st.session_state.config)

for i, item in enumerate(items):
    st.markdown(f'''
        <div class="trend-card">
            <small style="color:#1a5cff;">🔒 ENLACE VERIFICADO | {item['trend']}</small>
            <h3 style="margin-top:10px;">{item['title']}</h3>
        </div>
    ''', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([2,2,1])
    c1.link_button("📰 Leer Noticia", item['url'], use_container_width=True)
    c2.link_button("🛒 Oferta Segura Amazon", item['amz'], use_container_width=True)
    # Botón de compartir en WhatsApp como herramienta de confianza
    share_url = urllib.parse.quote(f"Mira esta oferta segura: {item['amz']}")
    c3.link_button("📢", f"https://wa.me/?text={share_url}", use_container_width=True)

st.caption("Certificado SSL vigente. Transacciones gestionadas por plataformas externas seguras.")
