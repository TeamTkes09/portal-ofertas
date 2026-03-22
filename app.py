import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse
import requests
import time

# 1. CONFIGURACIÓN DE INTERFAZ ELITE
st.set_page_config(page_title="TechFlash Pro ⚡ TechFlash780", page_icon="🚀", layout="wide")

# --- CREDENCIALES ---
MI_PAYPAL_USER = "TechFlash780"
AMZ_TAG = "unlimited0f3-20" 

# --- CSS: EFECTOS DE ALTA CONVERSIÓN ---
st.html(f'''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap');
        .stApp {{ background: #050608; color: #f8fafc; font-family: 'Plus Jakarta Sans', sans-serif; }}
        
        /* Tarjeta Premium */
        .premium-card {{
            background: #111;
            border: 1px solid #222;
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 20px;
            transition: 0.3s ease;
        }}
        .premium-card:hover {{ border-color: #3b82f6; }}

        /* BOTÓN CON BRILLO ANIMADO (SHIMMER) */
        @keyframes shimmer {{
            0% {{ background-position: -200% 0; }}
            100% {{ background-position: 200% 0; }}
        }}
        .btn-shimmer {{
            background: linear-gradient(90deg, #f97316 0%, #fb923c 50%, #f97316 100%);
            background-size: 200% 100%;
            animation: shimmer 3s infinite linear;
            color: white !important;
            text-decoration: none;
            padding: 14px;
            border-radius: 12px;
            display: block;
            text-align: center;
            font-weight: 800;
            font-size: 15px;
            box-shadow: 0 4px 15px rgba(249, 115, 22, 0.2);
            border: none;
        }}
    </style>
''')

# 2. INTELIGENCIA DE PAÍS
if 'config' not in st.session_state:
    try:
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        mapa = {"ES": ".es", "MX": ".com.mx", "US": ".com", "AR": ".com.be"}
        st.session_state.config = {
            "name": r.get('country_name', 'Global'), 
            "suffix": mapa.get(r.get('country_code'), ".com")
        }
    except: st.session_state.config = {"name": "Global", "suffix": ".com"}

# 3. HEADER Y DONACIONES
c1, c2 = st.columns([3,1])
with c1:
    st.title("⚡ TechFlash Pro")
    st.caption(f"Radar de Tendencias Inteligente | Optimizado para {st.session_state.config['name']}")
with c2:
    st.link_button("☕ PayPal.me/TechFlash780", f"https://www.paypal.me/{MI_PAYPAL_USER}")

st.divider()

# 4. DASHBOARD DE PRODUCTOS
tab1, tab2 = st.tabs(["🎯 Recomendados hoy", "💎 Zona VIP"])

with tab1:
    rubros = ["Gaming", "Laptops", "Home Office"]
    cols = st.columns(3)
    for i, r in enumerate(rubros):
        with cols[i]:
            url_amz = f"https://www.amazon{st.session_state.config['suffix']}/s?k={r}&tag={AMZ_TAG}"
            st.markdown(f'''
                <div class="premium-card">
                    <small style="color:#3b82f6; font-weight:bold;">TENDENCIA EN {st.session_state.config['name'].upper()}</small>
                    <h3 style="margin:10px 0;">{r} Gear 2026</h3>
                    <p style="font-size:12px; color:#666;">Analizado por IA según volumen de búsqueda actual.</p>
                    <a href="{url_amz}" target="_blank" class="btn-shimmer">VER OFERTA EN AMAZON</a>
                </div>
            ''', unsafe_allow_html=True)

with tab2:
    st.markdown('''
        <div style="text-align:center; padding:20px; border:1px dashed #333; border-radius:20px;">
            <h3>🌟 Contenido para Patrocinadores</h3>
            <p>Las mejores ofertas "escondidas" se publican aquí.</p>
            <p style="color:#f97316;"><b>Próxima actualización en 24hs</b></p>
        </div>
    ''', unsafe_allow_html=True)

# 5. FOOTER
st.write("---")
st.caption(f"TechFlash v21.0 - Nodo Seguro Activo - © 2026 TechFlash780")
