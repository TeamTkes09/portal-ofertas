import streamlit as st
import feedparser
import urllib.parse
import requests
import datetime

# 1. CONFIGURACIÓN DE SEGURIDAD GLOBAL
st.set_page_config(page_title="TechFlash Global 🛡️", page_icon="⚖️", layout="wide")

# --- CREDENCIALES ---
MI_PAYPAL_USER = "TechFlash780"
AMZ_TAG = "unlimited0f3-20" 

# --- CSS: ESTILO CORPORATIVO Y SECCIONES DE ADVERTENCIA ---
st.html(f'''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        .stApp {{ background: #020408; color: #cbd5e1; font-family: 'Inter', sans-serif; }}
        
        .legal-notice {{
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid #ef4444;
            color: #fca5a5;
            padding: 15px;
            border-radius: 10px;
            font-size: 12px;
            margin-bottom: 25px;
        }}
        
        .global-footer {{
            background: #000;
            padding: 60px 20px;
            margin-top: 100px;
            border-top: 2px solid #1e293b;
            font-size: 11px;
            color: #94a3b8;
            line-height: 1.8;
        }}

        .investment-card {{
            background: #ffffff; color: #000; border-radius: 15px;
            padding: 20px; margin-bottom: 20px;
            border-bottom: 5px solid #22c55e;
        }}
    </style>
''')

# 2. DETECCIÓN DE REGIÓN (Para aplicar leyes locales)
@st.cache_data
def get_global_context():
    try:
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        mapa = {"ES": ".es", "MX": ".com.mx", "US": ".com", "AR": ".com.be", "CL": ".cl", "CO": ".com.co"}
        return {
            "pais": r.get('country_name', 'Internacional'),
            "suffix": mapa.get(r.get('country_code'), ".com"),
            "ip": r.get('ip', 'Oculta')
        }
    except: return {"pais": "Internacional", "suffix": ".com", "ip": "0.0.0.0"}

ctx = get_global_context()

# 3. ADVERTENCIA DE ENTRADA (Mandatorio legal)
st.markdown(f'''
    <div class="legal-notice">
        <strong>⚠️ AVISO LEGAL INTERNACIONAL:</strong> Al navegar en TechFlash desde <b>{ctx['pais']}</b>, usted acepta que el uso de esta información es bajo su propio riesgo. TechFlash780 no se responsabiliza por aranceles aduaneros, impuestos locales o restricciones de reventa en su jurisdicción.
    </div>
''', unsafe_allow_html=True)

# 4. CONTENIDO DE NEGOCIOS
st.title("💹 TechFlash: Arbitraje Global")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f'''
        <div class="investment-card">
            <h3>📦 Lote Reventa Tech Pro</h3>
            <p>Inversión estimada para {ctx['pais']}</p>
            <h2 style="color:#16a34a;">ROI +45%</h2>
            <a href="https://www.amazon{ctx['suffix']}/s?k=wholesale+tech&tag={AMZ_TAG}" target="_blank" 
               style="background:#111; color:#fff; display:block; text-align:center; padding:10px; text-decoration:none; border-radius:5px; font-weight:bold;">
               REVISAR EN AMAZON {ctx['suffix'].upper()}
            </a>
            <p style="font-size:9px; color:#666; margin-top:10px;">* El precio final incluye impuestos de Amazon pero no aranceles de importación locales.</p>
        </div>
    ''', unsafe_allow_html=True)

# 5. EL "BLINDAJE" LEGAL DEFINITIVO (Footer Multinacional)
st.markdown(f'''
    <div class="global-footer">
        <div style="max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
            <div>
                <strong>1. DESCARGO DE AFILIACIÓN (FTC & EU COMPLIANCE)</strong><br>
                TechFlash780 declara que este sitio web contiene enlaces de afiliados. Si usted realiza una compra a través de estos enlaces, recibimos una comisión sin costo adicional para usted. Este sitio no es propiedad de Amazon ni está avalado por Amazon Inc.<br><br>
                <strong>2. NO ASESORAMIENTO FINANCIERO</strong><br>
                El contenido de TechFlash tiene fines exclusivamente educativos e informativos. No constituye asesoramiento financiero, legal o fiscal. Los cálculos de ganancias son proyecciones hipotéticas basadas en datos históricos.
            </div>
            <div>
                <strong>3. JURISDICCIÓN Y LEY APLICABLE</strong><br>
                Este sitio web opera bajo la premisa de "Safe Harbor". El usuario es el único responsable de cumplir con las leyes de su país de residencia, incluyendo pero no limitado a: regulaciones de importación, impuestos sobre la renta (IVA/IGIC/ISR) y normativas de comercio electrónico locales.<br><br>
                <strong>4. LIMITACIÓN DE RESPONSABILIDAD GLOBAL</strong><br>
                Bajo ninguna circunstancia TechFlash780 será responsable de pérdidas directas o indirectas derivadas del uso de esta plataforma. La disponibilidad de ofertas se muestra "tal cual" (As-Is) según la API de terceros al momento {datetime.datetime.now().strftime("%H:%M UTC")}.
            </div>
        </div>
        <hr style="border: 0; border-top: 1px solid #334155; margin: 30px 0;">
        <center>
            <small>TechFlash780 Intelligence System © {datetime.datetime.now().year}. Todos los derechos reservados a nivel mundial.</small>
        </center>
    </div>
''', unsafe_allow_html=True)

# 6. SOPORTE
st.link_button("☕ Apoyar este Nodo de Inteligencia (PayPal)", f"https://www.paypal.me/{MI_PAYPAL_USER}", use_container_width=True)
