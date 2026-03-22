# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    # Forzamos 4 columnas en el layout de Streamlit
    cols = st.columns(4, gap="small")

    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            # Cálculos Financieros
            costo = op.get('c', 0)
            venta = op.get('v', 0)
            margen_neto = venta - costo
            roi = int((margen_neto / costo) * 100) if costo > 0 else 0
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}"

            # Mapeo de comparativa de 5 puntos
            comp = {item['sitio'].lower(): item['precio'] for item in op.get('comparativa', [])}
            
            puntos = [
                ("AMZ", costo),
                ("EBY", comp.get('ebay', '---')),
                ("GGL", comp.get('google', '---')),
                ("SHP", comp.get('shopify', '---')),
                ("LOC", venta)
            ]

            # Construcción de filas en una sola columna vertical
            filas_html = ""
            for sitio, precio in puntos:
                val = f"${precio}" if isinstance(precio, (int, float)) else precio
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid #1e293b; padding: 1px 0;">
                    <span style="color: #64748b; font-size: 9px; font-weight: 600;">{sitio}</span>
                    <span style="color: #60a5fa; font-size: 9px; font-weight: 800;">{val}</span>
                </div>"""

            # Inyectar el HTML con la altura reducida
            html_final = get_card_template(op, roi, margen_neto, amz_url, filas_html)
            st.components.v1.html(html_final, height=225, scrolling=False)
