import streamlit as st
import urllib.parse
import random

def render_investment_section(suffix):
    st.subheader("💰 Oportunidades de Arbitraje y Reventa")
    
    # 1. Definimos los datos de las tarjetas
    oportunidades = [
        {
            "nombre": "Bundle: Smart Home Starter Kit",
            "costo": 85, "reventa": 155, "riesgo": "BAJO", "color": "#22c55e", 
            "tag": "ALTA ROTACIÓN", "query": "smart home bundle alexa"
        },
        {
            "nombre": "Lote x5: Auriculares Gaming Pro",
            "costo": 120, "reventa": 210, "riesgo": "MEDIO", "color": "#facc15", 
            "tag": "TENDENCIA", "query": "gaming headset wholesale"
        }
    ]

    # 2. Creamos las columnas en Streamlit
    col1, col2 = st.columns(2)

    for i, op in enumerate(oportunidades):
        # Elegimos en qué columna poner la tarjeta
        target_col = col1 if i % 2 == 0 else col2
        
        # Cálculos de rentabilidad
        ganancia = op['reventa'] - op['costo']
        roi = int((ganancia / op['costo']) * 100)
        amz_url = f"https://www.amazon{suffix}/s?k={urllib.parse.quote(op['query'])}&tag=unlimited0f3-20"
        ref_id = f"TF-{random.randint(100,999)}"

        # 3. Generamos el HTML como una cadena de texto limpia
        html_card = f"""
        <div style="background-color: white; color: #111; padding: 25px; border-radius: 20px; border-top: 10px solid {op['color']}; margin-bottom: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 10px; font-weight: 800; color: {op['color']}; border: 1px solid {op['color']}; padding: 2px 8px; border-radius: 5px; text-transform: uppercase;">RIESGO {op['riesgo']}</span>
                <span style="font-size: 10px; color: #666; font-weight: bold;">REF: {ref_id}</span>
            </div>
            
            <h3 style="margin: 0 0 5px 0; font-size: 1.2rem; color: #111; line-height: 1.2;">{op['nombre']}</h3>
            <p style="font-size: 11px; color: #555; margin: 0 0 15px 0; font-weight: 600;">Estrategia: {op['tag']}</p>
            
            <div style="background-color: #f8fafc; padding: 15px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #e2e8f0;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="color: #64748b; font-size: 13px;">Costo Amazon:</span>
                    <span style="font-weight: 700; color: #1e293b;">${op['costo']}</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="color: #64748b; font-size: 13px;">Venta Sugerida:</span>
                    <span style="font-weight: 700; color: #1d4ed8;">${op['reventa']}</span>
                </div>
                <hr style="margin: 10px 0; border: 0; border-top: 1px solid #e2e8f0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 800; color: #0f172a; font-size: 14px;">GANANCIA:</span>
                    <span style="font-weight: 800; color: #15803d; font-size: 18px;">+${ganancia} ({roi}%)</span>
                </div>
            </div>
            
            <a href="{amz_url}" target="_blank" style="background-color: #fbbf24; color: #000; text-decoration: none; display: block; text-align: center; padding: 12px; border-radius: 10px; font-weight: 800; font-size: 14px; border-bottom: 3px solid #d97706;">
                ADQUIRIR EN AMAZON*
            </a>
            
            <p style="font-size: 9px; color: #94a3b8; margin-top: 12px; line-height: 1.3; font-style: italic;">
                *Valores estimados. La rentabilidad final depende de las comisiones de su plataforma de reventa y aranceles locales.
            </p>
        </div>
        """
        
        # 4. PASO CRUCIAL: Inyectar el HTML en la columna de Streamlit
        target_col.markdown(html_card, unsafe_allow_html=True)
