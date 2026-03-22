import streamlit as st
import urllib.parse
import random

def render_card(nombre, costo, reventa, riesgo, query):
    ganancia = reventa - costo
    roi = int((ganancia/costo)*100)
    st.subheader("💰 Oportunidades de Arbitraje y Reventa")
    
    # Lista de productos preconfigurados (puedes añadir más aquí)
    oportunidades = [
        {
            "nombre": "Bundle: Smart Home Starter Kit",
            "costo": 85,
            "reventa": 155,
            "riesgo": "BAJO",
            "color": "#22c55e", # Verde
            "tag": "ALTA ROTACIÓN",
            "query": "smart home bundle alexa"
        },
        {
            "nombre": "Lote x5: Auriculares Gaming Pro",
            "costo": 120,
            "reventa": 210,
            "riesgo": "MEDIO",
            "color": "#facc15", # Amarillo
            "tag": "TENDENCIA",
            "query": "gaming headset wholesale"
        },
        {
            "nombre": "Dron 4K Plegable (Oportunidad)",
            "costo": 290,
            "reventa": 450,
            "riesgo": "ALTO",
            "color": "#ef4444", # Rojo
            "tag": "ALTO MARGEN",
            "query": "4k drone professional"
        }
    ]

    col1, col2 = st.columns(2)

    for i, op in enumerate(oportunidades):
        target_col = col1 if i % 2 == 0 else col2
        ganancia = op['reventa'] - op['costo']
        roi = int((ganancia / op['costo']) * 100)
        amz_url = f"https://www.amazon{suffix}/s?k={urllib.parse.quote(op['query'])}&tag=unlimited0f3-20"

        with target_col:
            st.markdown(f'''
                <div style="background: white; color: #111; padding: 25px; border-radius: 20px; border-top: 10px solid {op['color']}; margin-bottom: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 10px; font-weight: 800; color: {op['color']}; border: 1px solid {op['color']}; padding: 2px 8px; border-radius: 5px;">
                            RIESGO {op['riesgo']}
                        </span>
                        <span style="font-size: 10px; color: #666;">REF: TF-{random.randint(100,999)}</span>
                    </div>
                    
                    <h3 style="margin: 15px 0 5px 0; font-size: 1.2rem;">{op['nombre']}</h3>
                    <p style="font-size: 12px; color: #444; margin-bottom: 15px;">Estrategia: {op['tag']}</p>
                    
                    <div style="background: #f1f5f9; padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                        <div style="display: flex; justify-content: space-between;">
                            <span>Costo Amazon:</span>
                            <span style="font-weight: bold;">${op['costo']}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>Venta Sugerida:</span>
                            <span style="font-weight: bold; color: #1e40af;">${op['reventa']}</span>
                        </div>
                        <hr style="margin: 10px 0; border: 0; border-top: 1px solid #cbd5e1;">
                        <div style="display: flex; justify-content: space-between; font-size: 1.1rem;">
                            <span style="font-weight: 800;">GANANCIA:</span>
                            <span style="font-weight: 800; color: #16a34a;">+${ganancia} ({roi}%)</span>
                        </div>
                    </div>
                    
                    <a href="{amz_url}" target="_blank" style="background: #fbbf24; color: black; text-decoration: none; display: block; text-align: center; padding: 12px; border-radius: 10px; font-weight: 800; font-size: 14px;">
                        ADQUIRIR EN AMAZON*
                    </a>
                    
                    <p style="font-size: 9px; color: #94a3b8; margin-top: 10px; line-height: 1.2;">
                        *Valores estimados. La rentabilidad final depende de las comisiones de su plataforma de reventa y aranceles locales.
                    </p>
                </div>
            ''', unsafe_allow_html=True)
