import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse
import requests
import random

# 1. CONFIGURACIÓN DE PORTAL DE ALTO TRÁFICO
st.set_page_config(page_title="TechFlash Mega Hub ⚡", page_icon="🚀", layout="wide")

# --- CREDENCIALES ---
MI_PAYPAL_USER = "TechFlash780"
AMZ_TAG = "unlimited0f3-20" 

# --- CSS: DISEÑO DE PORTAL DENSO ---
st.html(f'''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
        .stApp {{ background: #0c0f14; color: #ffffff; font-family: 'Inter', sans-serif; }}
        
        /* Hero Banner */
        .hero-banner {{
            background: linear-gradient(45deg, #1e3a8a, #3b82f6);
            padding: 60px 20px;
            border-radius: 30px;
            text-align: center;
            margin-bottom: 40px;
            border: 1px solid #3b82f6;
        }}

        /* Tarjetas de Producto Maximizadas */
        .mega-card {{
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 20px;
            padding: 0px;
            margin-bottom: 20px;
            overflow: hidden;
            transition: 0.3s;
        }}
        .mega-card:hover {{ border-color: #3b82f6; transform: translateY(-5px); }}
        .card-content {{ padding: 20px; }}
        
        .price-tag {{ color: #22c55e; font-size: 20px; font-weight: 900; }}
        .old-price {{ color: #ef4444; text-decoration: line-through; font-size: 14px; margin-right: 10px; }}
        
        /* Footer Premium */
        .footer-news {{ background: #000; padding: 40px; text-align: center; border-top: 1px solid #333; }}
    </style>
''')

# 2. LOGICA DE GEOLOCALIZACIÓN (Cacheada)
@st.cache_data
def get_location():
    try:
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        mapa = {"ES": ".es", "MX": ".com.mx", "US": ".com", "AR": ".com.be"}
        return {"name": r.get('country_name', 'Global'), "suffix": mapa.get(r.get('country_code'), ".com")}
    except: return {"name": "Global", "suffix": ".com"}

loc = get_location()

# 3. HEADER: HERO SECTION (Elimina la sensación de vacío)
st.markdown(f'''
    <div class="hero-banner">
        <h1 style="font-size: 3.5rem; font-weight: 900; margin:0;">TECHFLASH <span style="color:#fbbf24;">ELITE</span></h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">El radar de tecnología más potente de {loc['name']}. Ofertas actualizadas cada 15 min.</p>
    </div>
''', unsafe_allow_html=True)

# 4. CUERPO DE LA WEB: MULTI-CATEGORÍAS
st.subheader("🔥 Ofertas Relámpago (Finalizan pronto)")
col1, col2, col3, col4 = st.columns(4)

def render_product(col, title, category, discount):
    with col:
        url_amz = f"https://www.amazon{loc['suffix']}/s?k={urllib.parse.quote(title)}&tag={AMZ_TAG}"
        precio_fake = random.randint(200, 900)
        ahorro = int(precio_fake * (discount/100))
        st.markdown(f'''
            <div class="mega-card">
                <div style="background:#222; height:150px; display:flex; align-items:center; justify-content:center; font-size:40px;">
                    📦
                </div>
                <div class="card-content">
                    <span style="background:#fbbf24; color:black; padding:2px 8px; border-radius:5px; font-size:10px; font-weight:bold;">-{discount}% HOY</span>
                    <h4 style="margin:10px 0; font-size:16px;">{title}</h4>
                    <p><span class="old-price">${precio_fake}</span><span class="price-tag">${precio_fake - ahorro}</span></p>
                    <a href="{url_amz}" target="_blank" style="background:#3b82f6; color:white; text-decoration:none; padding:10px; display:block; text-align:center; border-radius:10px; font-weight:bold;">VER EN AMAZON</a>
                </div>
            </div>
        ''', unsafe_allow_html=True)

# Fila 1
render_product(col1, "Smartwatch Pro Ultra", "Gadgets", 30)
render_product(col2, "Auriculares Noise Cancelling", "Audio", 45)
render_product(col3, "Teclado Mecánico RGB", "Gaming", 20)
render_product(col4, "Cámara Seguridad WiFi", "Hogar", 15)

st.divider()

# 5. SECCIÓN DE NOTICIAS Y TENDENCIAS (Contenido denso)
st.subheader("🌐 Noticias que están moviendo el mercado")
c_news1, c_news2 = st.columns([2, 1])

with c_news1:
    # Aquí iría el feed de noticias que ya teníamos, pero con más items
    st.info("Cargando flujo de datos en tiempo real...")
    for i in range(3):
        st.markdown(f'''
            <div style="background:#161b22; padding:20px; border-radius:15px; margin-bottom:10px; border:1px solid #333;">
                <small style="color:#3b82f6;">HACE 10 MINUTOS</small>
                <h4>Nueva filtración del procesador que cambiará todo en 2026</h4>
                <p style="font-size:14px; color:#888;">Los analistas sugieren que el precio será un 20% menor al esperado...</p>
                <a href="#" style="color:#fbbf24; text-decoration:none; font-weight:bold;">Leer más →</a>
            </div>
        ''', unsafe_allow_html=True)

with c_news2:
    st.markdown('''
        <div style="background:#1e3a8a; padding:20px; border-radius:20px; text-align:center;">
            <h4>💎 VIP Club TechFlash</h4>
            <p style="font-size:13px;">Únete a nuestra lista de correo para ofertas exclusivas.</p>
            <input type="text" placeholder="Tu email aquí" style="width:100%; padding:10px; border-radius:10px; border:none; margin-bottom:10px;">
            <button style="width:100%; padding:10px; border-radius:10px; border:none; background:#fbbf24; font-weight:bold;">SUSCRIBIRME</button>
        </div>
    ''', unsafe_allow_html=True)
    st.write("")
    st.link_button("☕ Donar a TechFlash780", f"https://www.paypal.me/{MI_PAYPAL_USER}", use_container_width=True)

# 6. FOOTER PROFESIONAL
st.markdown(f'''
    <div class="footer-news">
        <p>TechFlash Elite v22.0 | Inteligencia de Mercado para {loc['name']}</p>
        <div style="font-size:12px; color:#555;">
            Aviso: TechFlash participa en el programa de afiliados de Amazon. Las donaciones vía PayPal ayudan a mantener el servicio.
        </div>
    </div>
''', unsafe_allow_html=True)
