import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    cols = st.columns(4, gap="small")
    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            costo, venta = op['c'], op['v']
            roi = int(((venta - costo) / costo) * 100)
            
            # LINK REAL: Usa el código ASIN directo para ir al producto
            amz_url = f"https://www.amazon{suffix}/dp/{op['q']}?tag=tu_tag_afiliado-20"
            
            comp = {item['sitio']: item['precio'] for item in op['comparativa']}
            puntos = [("Amazon", costo), ("eBay", comp['ebay']), ("Google", comp['google']), ("Venta", venta)]
            
            filas_html = ""
            for sitio, precio in puntos:
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid #1e293b; padding: 1px 0;">
                    <span style="color: #64748b; font-size: 9px;">{sitio}</span>
                    <span style="color: #60a5fa; font-size: 9px; font-weight: bold;">${precio}</span>
                </div>"""

            html = get_card_template(op, roi, round(venta-costo, 2), amz_url, filas_html)
            st.components.v1.html(html, height=220)
