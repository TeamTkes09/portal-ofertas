# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    st.markdown(f"### 🎯 Oportunidades en Amazon{suffix}")
    
    cols = st.columns(3) # 3 columnas para que la tabla sea legible

    for i, op in enumerate(lista_productos):
        with cols[i % 3]:
            # Cálculos automáticos que recuperamos
            margen = op['v'] - op['c']
            roi = int((margen / op['c']) * 100)
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # Construcción de la tabla de comparación
            filas_html = ""
            for item in op.get('comparativa', []):
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #1e293b; font-size: 11px;">
                    <span style="color: #94a3b8;">{item['sitio']}</span>
                    <a href="{item['url']}" target="_blank" style="color: #60a5fa; text-decoration: none; font-weight: bold;">${item['precio']} ↗</a>
                </div>
                """
            
            # Unimos todo usando el template
            html_final = get_card_template(op, roi, margen, amz_url, filas_html)
            st.markdown(html_final, unsafe_allow_html=True)
