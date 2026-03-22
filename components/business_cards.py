import streamlit as st
import urllib.parse
import random

def render_investment_section(suffix):
    st.subheader("💰 Oportunidades de Arbitraje y Reventa")
    
    oportunidades = [
        {"nombre": "Smart Home Kit", "costo": 85, "reventa": 155, "riesgo": "BAJO", "color": "#22c55e", "query": "smart home alexa"},
        {"nombre": "Gaming Headset x5", "costo": 120, "reventa": 210, "riesgo": "MEDIO", "color": "#facc15", "query": "gaming headset wholesale"}
    ]

    col1, col2 = st.columns(2)

    for i, op in enumerate(oportunidades):
        # 4 espacios de sangría para entrar al 'for'
        target_col = col1 if i % 2 == 0 else col2
        ganancia = op['reventa'] - op['costo']
        roi = int((ganancia / op['costo']) * 100)
        amz_url = f"https://www.amazon{suffix}/s?k={urllib.parse.quote(op['query'])}&tag=unlimited0f3-20"
        
        # El bloque HTML debe estar alineado con 'target_col'
        html_card = f'''
        <div style="background:white; color:black; padding:20px; border-radius:15px; border-top:10px solid {op['color']}; margin-bottom:20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin-top:0;">{op['nombre']}</h3>
            <p style="font-weight:bold; color:#16a34a;">GANANCIA: +${ganancia} ({roi}%)</p>
            <a href="{amz_url}" target="_blank" style="background:#fbbf24; color:black; text-decoration:none; display:block; text-align:center; padding:10px; border-radius:8px; font-weight:bold;">VER EN AMAZON</a>
        </div>
        '''
        
        # ESTA LÍNEA DEBE TENER LA MISMA SANGRÍA QUE 'target_col'
        target_col.markdown(html_card, unsafe_allow_html=True)
