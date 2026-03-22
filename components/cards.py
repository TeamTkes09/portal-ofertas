# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    st.markdown("### 🎯 Oportunidades de Arbitraje Verificadas")
    cols = st.columns(3)

    for i, op in enumerate(lista_productos):
        with cols[i % 3]:
            margen_neto = op['v'] - op['c']
            roi = int((margen_neto / op['c']) * 100)
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            filas_comparativa = ""
            for item in op.get('comparativa', []):
                filas_comparativa += f"""
                <div style="display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px dashed #334155; font-size: 11px;">
                    <span style="color: #94a3b8;">{item['sitio']}</span>
                    <a href="{item['url']}" target="_blank" style="color: #60a5fa; text-decoration: none; font-weight: bold;">${item['precio']} ↗</a>
                </div>
                """
            
            html = get_card_template(op, roi, margen_neto, amz_url, filas_comparativa)
            st.markdown(html, unsafe_allow_html=True)
