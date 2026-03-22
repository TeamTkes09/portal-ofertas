# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    st.markdown(f"### 🎯 Oportunidades Detectadas en Amazon{suffix}")
    
    # Grid de 3 columnas
    cols = st.columns(3)

    for i, op in enumerate(lista_productos):
        with cols[i % 3]:
            # 1. Lógica de Precios Base
            costo = op.get('c', 0)
            venta = op.get('v', 0)
            margen_neto = venta - costo
            roi = int((margen_neto / costo) * 100) if costo > 0 else 0
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # 2. Mapeo de los 5 puntos de precio solicitados
            # Buscamos en la lista 'comparativa' del producto
            comp_data = {item['sitio'].lower(): item['precio'] for item in op.get('comparativa', [])}
            
            puntos = [
                ("Amazon", costo), # El costo de entrada
                ("eBay", comp_data.get('ebay', '---')),
                ("Google Shop", comp_data.get('google', '---')),
                ("Shopify", comp_data.get('shopify', '---')),
                ("Tienda Local", venta) # El precio de salida objetivo
            ]

            filas_html = ""
            for sitio, precio in puntos:
                # Formateamos el precio si es número, si no dejamos el string
                val_display = f"${precio}" if isinstance(precio, (int, float)) else precio
                
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px solid #1e293b; font-size: 11px;">
                    <span style="color: #94a3b8;">{sitio}</span>
                    <span style="color: #60a5fa; font-weight: bold;">{val_display}</span>
                </div>"""

            # 3. Renderizado mediante iFrame para evitar conflictos de CSS
            html_final = get_card_template(op, roi, margen_neto, amz_url, filas_html)
            
            # Altura de 560px para que no salga scrollbar con los nuevos campos
            st.components.v1.html(html_final, height=560, scrolling=False)

    st.write("")
