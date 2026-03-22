# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    """
    Renderiza las tarjetas de inversión en una cuadrícula de 3 columnas.
    """
    st.markdown(f"### 🎯 Oportunidades Detectadas en Amazon{suffix}")
    
    # Creamos la fila base de 3 columnas
    cols = st.columns(3)

    for i, op in enumerate(lista_productos):
        # El índice % 3 distribuye los productos en las 3 columnas de forma infinita
        with cols[i % 3]:
            
            # 1. Cálculos de Negocio
            costo = op.get('c', 0)
            venta = op.get('v', 0)
            margen_neto = venta - costo
            roi = int((margen_neto / costo) * 100) if costo > 0 else 0
            
            # 2. URL de Amazon con Tag de Afiliado
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # 3. Construcción del bloque de comparativa (HTML)
            filas_html = ""
            for item in op.get('comparativa', []):
                filas_html += f"""
                <div style="display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #1e293b; font-size: 11px;">
                    <span style="color: #94a3b8;">{item['sitio']}</span>
                    <span style="color: #60a5fa; font-weight: bold;">${item['precio']} ↗</span>
                </div>
                """

            # 4. Obtención del Template
            # Pasamos los datos a la función que genera el string HTML
            html_final = get_card_template(
                op=op, 
                roi=roi, 
                margen_neto=margen_neto, 
                amz_url=amz_url, 
                filas_html=filas_html
            )
            
            # 5. RENDERIZADO CRÍTICO (Sin esto, verás texto plano)
            # Usamos un contenedor vacío para asegurar que el HTML se inyecte limpio
            container = st.container()
            container.markdown(html_final, unsafe_allow_html=True)

    # Espacio estético al final
    st.write("")
