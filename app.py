import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse
import requests

# 1. CONFIGURACIÓN DE MONETIZACIÓN
st.set_page_config(page_title="TechFlash Ads & Shop 💸", page_icon="📈", layout="wide")

# --- TUS CREDENCIALES (DINERO) ---
MI_PAYPAL_USER = "TechFlash780"
AMZ_TAG = "unlimited0f3-20"  # Asegúrate de que este sea tu ID de Amazon Afiliados
GOOGLE_ADS_ID = "ca-pub-XXXXXXXXXXXXXXXX" # Aquí iría tu ID de Google Adsense

# --- CSS: DISEÑO ORIENTADO A CLICS ---
st.html(f'''
    <style>
        .stApp {{ background: #0a0a0a; color: #e5e7eb; }}
        .ad-space {{
            background: #1a1a1a;
            border: 1px dashed #444;
            color: #888;
            padding: 10px;
            text-align: center;
            border-radius: 8px;
            margin: 20px 0;
            font-size: 12px;
        }}
        .product-box {{
            background: #111827;
            border: 1px solid #374151;
            padding: 20px;
            border-radius: 15px;
            transition: 0.3s;
        }}
        .product-box:hover {{ border-color: #10b981; transform: translateY(-3px); }}
        .btn-amazon {{
            background: #ff9900;
            color: black !important;
            font-weight: bold;
            text-decoration: none;
            padding: 12px;
            border-radius: 8px;
            display: block;
            text-align: center;
            margin-top: 10px;
        }}
    </style>
''')

# 2. ESPACIO PARA PUBLICIDAD SUPERIOR (Google Ads)
st.markdown('<div class="ad-space">ESPACIO PUBLICITARIO (Google Adsense Banner)</div>', unsafe_allow_html=True)
# Nota: Aquí insertarías el script de Google Adsense real

# 3. LÓGICA DE PAÍS
if 'config' not in st.session_state:
    try:
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        suffix_map = {"ES": ".es", "MX": ".com.mx", "US": ".com", "AR": ".com.be"}
        st.session_state.config = {"name": r.get('country_name'), "suffix": suffix_map.get(r.get('country_code'), ".com")}
    except: st.session_state.config = {"name": "Global", "suffix": ".com"}

# 4. CONTENIDO PRINCIPAL
st.title("💸 TechFlash Monetized")
st.write(f"Ofertas verificadas para **{st.session_state.config['name']}**")

# Simulamos 3 rubros calientes
categorias = ["Laptops", "Gaming", "Smart Home"]
cols = st.columns(3)

for i, cat in enumerate(categorias):
    with cols[i]:
        st.markdown(f'''
            <div class="product-box">
                <span style="color:#10b981; font-weight:bold;">HOT DEAL</span>
                <h3>Tendencias {cat}</h3>
                <p style="font-size:0.8rem; color:#9ca3af;">Actualizado hace 5 minutos</p>
            </div>
        ''', unsafe_allow_html=True)
        
        # Link de Amazon con tu Comisión
        url_amz = f"https://www.amazon{st.session_state.config['suffix']}/s?k={cat}&tag={AMZ_TAG}"
        st.markdown(f'<a href="{url_amz}" target="_blank" class="btn-amazon">🛒 VER PRECIOS EN AMAZON</a>', unsafe_allow_html=True)

# 5. PUBLICIDAD LATERAL O INFERIOR
st.divider()
col_inf1, col_inf2 = st.columns([2,1])
with col_inf2:
    st.markdown('<div class="ad-space" style="height:250px;">ANUNCIO LATERAL (Google Ads)</div>', unsafe_allow_html=True)
with col_inf1:
    st.subheader("💎 Apoya al Creador")
    st.write("Si te ahorramos dinero con nuestras ofertas, considera una pequeña donación.")
    st.link_button(f"Donar a TechFlash780", f"https://www.paypal.me/{MI_PAYPAL_USER}")

st.markdown('<div class="ad-space">FOOTER ADSENSE - 728x90</div>', unsafe_allow_html=True)
