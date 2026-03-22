# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    # Usamos 4 columnas
    cols = st.columns(4, gap="small")

    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            costo = op.get('c', 0)
            venta = op.get('v', 0)
            margen = venta - costo
            roi = int((margen / costo) * 100) if costo > 0 else 0
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}"

            comp = {item['sitio'].lower(): item['precio'] for item in op.get('comparativa', [])}
            
            # Formato ultra compacto: una sola línea para ahorrar espacio si prefieres, 
            # o mantenemos los 5 puntos pero con letra minúscula.
            puntos = [
                ("AMZ", costo), ("EBY", comp.get('ebay', '-')), 
                ("GGL", comp.get('google', '-')), ("LOC", venta)
            ]

            filas_html = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2px 8px;">'
            for sitio, precio in puntos:
                val = f"${precio}" if isinstance(precio, (int, float)) else precio
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; font-size: 9px;">
                    <span style="color: #64748b;">{sitio}:</span>
                    <span style="color: #60a5fa; font-weight: bold;">{val}</span>
                </div>"""
            filas_html += '</div>'

            html_card = get_card_template(op, roi, margen, amz_url, filas_html)
            
            # ALTURA A LA MITAD: de 420px pasamos a 220px
            st.components.v1.html(html_card, height=220, scrolling=False)
