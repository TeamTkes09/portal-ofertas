import streamlit as st

def render_hero(pais_nombre):
    # Aviso sutil superior (Legal Stealth)
    st.markdown('<p style="font-size:10px; color:#475569; text-align:right; margin-bottom:-20px;">Contenido Patrocinado & Inteligencia de Mercado</p>', unsafe_allow_html=True)
    
    # Banner Principal
    st.markdown(f'''
        <div style="background: linear-gradient(135deg, #1e3a8a 0%, #020617 100%); padding: 40px; border-radius: 20px; text-align: center; margin-bottom: 25px; border: 1px solid #1e40af;">
            <h1 style="font-size: 2.8rem; font-weight: 800; margin:0; color: white;">TECHFLASH <span style="color:#3b82f6;">PRO</span></h1>
            <p style="color: #94a3b8; font-size: 1.1rem;">Nodo de Arbitraje y Tendencias Tech | <b>{pais_nombre.upper()}</b></p>
        </div>
        <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #fca5a5; padding: 10px; border-radius: 10px; font-size: 11px; text-align: center; margin-bottom: 20px;">
            ⚠️ <b>DIVULGACIÓN:</b> TechFlash780 utiliza enlaces de afiliados. Las proyecciones de ROI son informativas; el riesgo es del usuario.
        </div>
    ''', unsafe_allow_html=True)
