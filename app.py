import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse
import requests
import datetime

# 1. CONFIGURACIÓN
st.set_page_config(page_title="TechFlash Elite 🛡️", page_icon="💎", layout="wide")

# --- CREDENCIALES ---
MI_PAYPAL_USER = "TechFlash780"
AMZ_TAG = "unlimited0f3-20" 

# --- CSS: MINIMALISMO LEGAL ---
st.html(f'''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        .stApp {{ background: #05070a; color: #cbd5e1; font-family: 'Inter', sans-serif; }}
        
        /* El "Aviso Sutil" de arriba */
        .top-disclaimer {{
            font-size: 10px;
            color: #475569;
            text-align: right;
            margin-bottom: 10px;
            letter-spacing: 0.5px;
        }}

        /* El Footer Legal "Letra Chica" */
        .stealth-footer {{
            background: #000;
            padding: 30px;
            margin-top: 80px;
            font-size: 9px; /* Tamaño mínimo legal */
            color: #334155;
            text-align: justify;
            border-top: 1px solid #0f172a;
            line-height: 1.4;
        }}

        .hero-banner {{
            background: linear-gradient(135deg, #1e3a8a 0%, #020617 100%);
            padding: 40px; border-radius: 20px; text-align: center; margin-bottom: 20px;
        }}

        .btn-amz {{
            background: #fbbf24; color: #000 !important; font-weight: 800; padding: 10px;
            border-radius: 8px; text-decoration: none; display: block; text-align: center;
        }}
    </style>
''')

# 2. HEADER Y AVISO MINIMALISTA SUPERIOR
st.markdown('<p class="top-disclaimer">Contenido Patrocinado & Proyecciones de Negocio</p>', unsafe_allow_html=True)

st.markdown(f'''
    <div class="hero-banner">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin:0;">TECHFLASH <span style="color:#3b82f6;">PRO</span></h1>
        <p style="opacity:0.8;">Inteligencia de Arbitraje y Tecnología</p>
    </div>
''', unsafe_allow_html=True)

# 3. CONTENIDO (Resumen para no perder la estructura)
tab1, tab2 = st.tabs(["💰 Oportunidades", "🌐 Noticias"])

with tab1:
    col1, col2 = st.columns(2)
    # Ejemplo de tarjeta con link de afiliado
    with col1:
        st.markdown(f'''
            <div style="background:#111827; padding:20px; border-radius:15px; border:1px solid #1e293b;">
                <h4 style="margin:0;">Lote Resell: Smart-Tech Bundle</h4>
                <p style="color:#22c55e; font-weight:bold;">ROI Est. +40%</p>
                <a href="https://www.amazon.com/s?k=wholesale+tech&tag={AMZ_TAG}" target="_blank" class="btn-amz">Ver en Amazon*</a>
            </div>
        ''', unsafe_allow_html=True)

# 4. EL "BUNKER" LEGAL (LO MÁS CHICO Y AL FINAL POSIBLE)
st.markdown(f'''
    <div class="stealth-footer">
        <strong>AVISO LEGAL Y DIVULGACIÓN DE AFILIADOS:</strong><br>
        En cumplimiento con las directrices de la FTC y normativas de comercio electrónico internacionales, se informa que TechFlash780 participa en programas de marketing de afiliados (incluyendo Amazon Associates). Esto significa que recibimos comisiones por ventas derivadas de los enlaces salientes, sin costo adicional para el usuario. 
        Las "Proyecciones de Inversión", "ROI" y "Ganancias Estimadas" son cálculos teóricos basados en datos de mercado volátiles; no garantizan resultados reales y no constituyen asesoramiento financiero profesional. 
        El riesgo de pérdida de capital en actividades de reventa es responsabilidad exclusiva del usuario. TechFlash780 no se hace responsable por cambios de precio, disponibilidad de stock o políticas de aduanas en el país de destino. 
        Al utilizar este sitio, usted libera a TechFlash780 de cualquier responsabilidad legal derivada de sus decisiones comerciales.
        <br><br>
        <center>© {datetime.datetime.now().year} TechFlash780 Intelligence System. Todos los derechos reservados.</center>
    </div>
''', unsafe_allow_html=True)

# 5. SOPORTE
st.link_button("☕ Support", f"https://www.paypal.me/{MI_PAYPAL_USER}", use_container_width=True)
