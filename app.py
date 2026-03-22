import streamlit as st
import feedparser
from deep_translator import GoogleTranslator
import urllib.parse
import requests
import datetime
import random

# 1. CONFIGURACIÓN DE ALTO NIVEL
st.set_page_config(page_title="TechFlash780 Elite Hub 🛡️", page_icon="💎", layout="wide")

# --- CREDENCIALES UNIFICADAS ---
MI_PAYPAL_USER = "TechFlash780"
AMZ_TAG = "unlimited0f3-20" 

# --- CSS: ARQUITECTURA VISUAL PREMIUM (HÍBRIDA) ---
st.html(f'''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
        .stApp {{ background: #05070a; color: #e2e8f0; font-family: 'Plus Jakarta Sans', sans-serif; }}
        
        /* Hero & Banners */
        .hero-banner {{
            background: linear-gradient(135deg, #1e3a8a 0%, #020617 100%);
            padding: 50px; border-radius: 30px; text-align: center; border: 1px solid #1e40af; margin-bottom: 30px;
        }}
        
        /* News Cards */
        .news-card {{
            background: #111827; padding: 20px; border-radius: 15px; margin-bottom: 15px; border: 1px solid #1f2937;
        }}

        /* Business Cards */
        .biz-card {{
            background: #ffffff; color: #000; border-radius: 20px; padding: 25px; 
            margin-bottom: 25px; border-top: 10px solid #22c55e; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        
        /* Table & Buttons */
        .comp-table {{ width: 100%; background: #0f172a; border-radius: 15px; overflow: hidden; margin-bottom: 30px; }}
        .comp-table th {{ background: #1e40af; padding: 15px; }}
        .comp-table td {{ padding: 15px; border-bottom: 1px solid #1e293b; text-align: center; }}
        
        .btn-amz {{
            background: #fbbf24; color: #000 !important; font-weight: 800; padding: 12px;
            border-radius: 10px; text-decoration: none; display: block; text-align: center;
        }}
        
        .legal-notice {{ background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; padding: 15px; border-radius: 10px; font-size: 11px; margin-bottom: 20px; }}
        .footer-legal {{ background: #000; padding: 50px; font-size: 10px; color: #64748b; line-height: 1.6; border-top: 1px solid #1e293b; }}
    </style>
''')

# 2. MOTORES DINÁMICOS (Noticias y Localización)
@st.cache_data(ttl=600)
def fetch_news(query):
    try:
        translator = GoogleTranslator(source='auto', target='es')
        rss = f"https://news.google.com/rss/search?q={urllib.parse.quote(query)}&hl=es"
        feed = feedparser.parse(rss)
        return [{"t": translator.translate(e.title.split(' - ')[0]), "l": e.link, "s": e.source.get('title')} for e in feed.entries[:3]]
    except: return []

@st.cache_data
def get_geo():
    try:
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        suffixes = {"ES": ".es", "MX": ".com.mx", "US": ".com", "AR": ".com.be", "CL": ".cl", "CO": ".com.co"}
        return {"n": r.get('country_name', 'Global'), "s": suffixes.get(r.get('country_code'), ".com")}
    except: return {"n": "Global", "s": ".com"}

ctx = get_geo()

# 3. HEADER & BLINDAJE INICIAL
st.markdown(f'''
    <div class="hero-banner">
        <h1 style="font-size: 3rem; font-weight: 800; margin:0;">TECHFLASH <span style="color:#3b82f6;">PRO</span></h1>
        <p>Inteligencia de Mercado y Arbitraje para <b>{ctx['n']}</b></p>
    </div>
    <div class="legal-notice">
        <b>⚠️ AVISO:</b> TechFlash780 utiliza enlaces de afiliados y proyecciones de inversión. El riesgo comercial es responsabilidad del usuario.
    </div>
''', unsafe_allow_html=True)

# 4. TABLA COMPARATIVA (EL IMÁN DE CLICS)
st.subheader("📊 Comparativa de Rendimiento 2026")
st.markdown(f'''
    <table class="comp-table">
        <tr><th>PRODUCTO</th><th>CATEGORÍA</th><th>VALORACIÓN</th><th>ACCIÓN</th></tr>
        <tr><td>💻 MacBook Air M3</td><td>Laptop Pro</td><td>⭐⭐⭐⭐⭐</td><td><a href="https://www.amazon{ctx['s']}/s?k=MacBook+Air+M3&tag={AMZ_TAG}" style="color:#fbbf24;">Ver Precio</a></td></tr>
        <tr><td>🎮 RTX 4070 Super</td><td>Hardware</td><td>⭐⭐⭐⭐.9</td><td><a href="https://www.amazon{ctx['s']}/s?k=RTX+4070&tag={AMZ_TAG}" style="color:#fbbf24;">Ver Precio</a></td></tr>
        <tr><td>📱 Galaxy S24 Ultra</td><td>Smartphone</td><td>⭐⭐⭐⭐.8</td><td><a href="https://www.amazon{ctx['s']}/s?k=S24+Ultra&tag={AMZ_TAG}" style="color:#fbbf24;">Ver Precio</a></td></tr>
    </table>
''', unsafe_allow_html=True)

# 5. CONTENIDO DUAL (NOTICIAS + NEGOCIOS)
tab1, tab2, tab3 = st.tabs(["🌐 Noticias Real-Time", "💰 Arbitraje de Reventa", "📦 Combos de Inversión"])

with tab1:
    cols_n = st.columns(2)
    temas = ["inteligencia artificial", "hardware gaming"]
    for i, tema in enumerate(temas):
        noticias = fetch_news(tema)
        with cols_n[i]:
            st.subheader(f"Últimas en {tema.title()}")
            for n in noticias:
                st.markdown(f'''
                    <div class="news-card">
                        <small style="color:#3b82f6;">{n['s'].upper()}</small>
                        <h4 style="margin:5px 0;">{n['t']}</h4>
                        <a href="{n['l']}" target="_blank" style="color:#fbbf24; text-decoration:none; font-size:12px;">Leer más →</a>
                    </div>
                ''', unsafe_allow_html=True)

with tab2:
    st.subheader("Arbitraje: Amazon vs Marketplace")
    c1, c2 = st.columns(2)
    ops = [{"n": "Smartwatch Ultra", "c": 40, "v": 75}, {"n": "Auriculares ANC", "c": 95, "v": 160}]
    for i, op in enumerate(ops):
        target = c1 if i==0 else c2
        ganancia = op['v'] - op['c']
        with target:
            st.markdown(f'''
                <div class="biz-card">
                    <span style="background:#dcfce7; color:#166534; padding:3px 8px; border-radius:5px; font-size:10px; font-weight:bold;">ROI +{int((ganancia/op['c'])*100)}%</span>
                    <h3 style="margin:10px 0;">{op['n']}</h3>
                    <p style="margin:0; font-size:14px;">Costo: ${op['c']} | Reventa: ${op['v']}</p>
                    <div style="background:#1e293b; color:#fff; padding:10px; border-radius:10px; margin-top:10px; text-align:center;">
                        GANANCIA: +${ganancia} USD
                    </div>
                    <a href="https://www.amazon{ctx['s']}/s?k={op['n']}&tag={AMZ_TAG}" target="_blank" class="btn-amz" style="margin-top:10px;">COMPRAR LOTE</a>
                </div>
            ''', unsafe_allow_html=True)

with tab3:
    st.subheader("Bundles Estratégicos (Scroll Infinito)")
    bundles = ["Smart Home Kit", "Streamer Setup", "Crypto Mining Pack", "Office Clean Desk"]
    for b in bundles:
        st.markdown(f'''
            <div style="background:#161b22; padding:20px; border-radius:20px; border-left:10px solid #3b82f6; margin-bottom:15px;">
                <span style="color:#22c55e; font-weight:bold;">🚥 SEMÁFORO: ALTA DEMANDA</span>
                <h3>{b} - Inversión Sugerida</h3>
                <p style="color:#94a3b8;">Compra conjunta de 3+ productos para maximizar margen de reventa.</p>
                <a href="https://www.amazon{ctx['s']}/s?k={b}&tag={AMZ_TAG}" target="_blank" style="color:#fbbf24; font-weight:bold;">Analizar Combo en Amazon →</a>
            </div>
        ''', unsafe_allow_html=True)
    if st.button("CARGAR MÁS OPORTUNIDADES..."):
        st.rerun()

# 6. BLINDAJE LEGAL FINAL (FOOTER)
st.markdown(f'''
    <div class="footer-legal">
        <div style="max-width:1100px; margin:0 auto;">
            <strong>TECHFLASH780 - ACUERDO LEGAL GLOBAL {datetime.datetime.now().year}</strong><br><br>
            1. AFILIACIÓN: Como asociados de Amazon, percibimos ingresos por compras calificadas (Tag: {AMZ_TAG}).<br>
            2. RESPONSABILIDAD: La información se entrega "As-Is". No somos asesores financieros. El usuario asume riesgos aduaneros en {ctx['n']}.<br>
            3. PRECIOS: La última actualización fue a las {datetime.datetime.now().strftime("%H:%M")}. Los precios de Amazon prevalecen sobre cualquier cálculo aquí mostrado.<br>
            <center style="margin-top:20px;">© TechFlash780 Intelligence System. Protegido por cláusulas de Puerto Seguro (Safe Harbor).</center>
        </div>
    </div>
''', unsafe_allow_html=True)

st.link_button("☕ Apoyar Mantenimiento (PayPal)", f"https://www.paypal.me/{MI_PAYPAL_USER}", use_container_width=True)
