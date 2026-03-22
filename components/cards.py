# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    # Forzamos 4 columnas con un gap pequeño
    cols = st.columns(4, gap="small")

    for i, op in enumerate(lista_productos):
        # El índice % 4 asegura la distribución en las 4 columnas creadas
        with cols[i % 4]:
            # Lógica de Precios
            costo = op.get('c', 0)
            venta = op.get('v', 0)
            margen_neto = venta - costo
            roi = int((margen_neto / costo) * 100) if costo > 0 else 0
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}"

            # Mapeo de comparativa
            comp = {item['sitio'].lower(): item['precio'] for item in op.get('comparativa', [])}
            
            # Puntos clave abreviados para ahorrar espacio
            puntos = [
                ("AMZ", costo),
                ("EBY", comp.get('ebay', '---')),
                ("GGL", comp.get('google', '---')),
                ("SHP", comp.get('shopify', '---')),
                ("LOC", venta)
            ]

            filas_html = ""
            for sitio, precio in puntos:
                val = f"${precio}" if isinstance(precio, (int, float)) else precio
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; padding: 2px 0; border-bottom: 1px solid #1e293b; font-size: 10px;">
                    <span style="color: #64748b;">{sitio}</span>
                    <span style="color: #60a5fa; font-weight: bold;">{val}</span>
                </div>"""

            html_final = get_card_template(op, roi, margen_neto, amz_url, filas_html)
            
            # Altura del componente reducida a 430px para evitar scrollbars
            st.components.v1.html(html_final, height=430, scrolling=False)
