# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    """
    Renderiza las tarjetas de inversión en una cuadrícula de 3 columnas.
    """
    # Usamos st.markdown normal para el título
    st.markdown(f"### 🎯 Oportunidades Detectadas en Amazon{suffix}")
    
    # Creamos las columnas
    cols = st.columns(3)

    for i, op in enumerate(lista_productos):
        # Seleccionamos la columna según el índice
        with cols[i % 3]:
            # 1. Cálculos de Negocio
            costo = op.get('c', 0)
            venta = op.get('v', 0)
            margen_neto = venta - costo
            roi = int((margen_neto / costo) * 100) if costo > 0 else 0
            
            # 2. URL de Amazon
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # 3. Construcción del bloque de comparativa
            # Importante: Mantenerlo como un string limpio
            filas_html = ""
            for item in op.get('comparativa', []):
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #1e293b; font-size: 11px;">
                    <span style="color: #94a3b8;">{item['sitio']}</span>
                    <span style="color: #60a5fa; font-weight: bold;">${item['precio']} ↗</span>
                </div>"""

            # 4. Obtención del Template del archivo styles/html_templates.py
            html_final = get_card_template(
                op=op, 
                roi=roi, 
                margen_neto=margen_neto, 
                amz_url=amz_url, 
                filas_html=filas_html
            )
            
            # 5. RENDERIZADO (El punto donde fallaba)
            # Forzamos a Streamlit a interpretar esto como HTML puro
            st.components.v1.html(html_final, height=500, scrolling=False)

    st.write("")
