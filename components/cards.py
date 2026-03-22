# components/cards.py
import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    """
    Renderiza la sección de oportunidades en una cuadrícula de 3 columnas.
    Acepta el sufijo de Amazon (ej: .com, .es) y la lista filtrada de productos.
    """
    
    # Título de la sección
    st.markdown(f"### 🎯 Oportunidades Detectadas en Amazon{suffix}")
    
    # Creamos una rejilla de 3 columnas
    # Esto permite que si hay 32 productos, Streamlit cree automáticamente las filas necesarias
    cols = st.columns(3)

    for i, op in enumerate(lista_productos):
        # El operador % 3 asegura que los productos se repartan: 0, 1, 2, 0, 1, 2...
        with cols[i % 3]:
            
            # --- 1. LÓGICA DE NEGOCIO ---
            # Calculamos el margen y el ROI en tiempo real
            costo = op.get('c', 0)
            venta = op.get('v', 0)
            margen_neto = venta - costo
            
            # Evitamos división por cero si el costo no está definido
            roi = int((margen_neto / costo) * 100) if costo > 0 else 0
            
            # Generamos el enlace de búsqueda en Amazon
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # --- 2. CONSTRUCCIÓN DE LA TABLA DE COMPARATIVA ---
            # Generamos el HTML para las filas de verificación (Google, eBay, etc.)
            filas_comparativa_html = ""
            for item in op.get('comparativa', []):
                filas_comparativa_html += f"""
                <div style="display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #1e293b; font-size: 11px;">
                    <span style="color: #94a3b8;">{item['sitio']}</span>
                    <a href="{item['url']}" target="_blank" style="color: #60a5fa; text-decoration: none; font-weight: bold;">
                        ${item['precio']} ↗
                    </a>
                </div>
                """

            # --- 3. RENDERIZADO FINAL ---
            # Llamamos al template que está en styles/html_templates.py
            try:
                html_card = get_card_template(
                    op=op, 
                    roi=roi, 
                    margen_neto=margen_neto, 
                    amz_url=amz_url, 
                    filas_html=filas_comparativa_html
                )
                
                # Inyectamos el HTML en Streamlit con el blindaje activado
                st.markdown(html_card, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error al renderizar la tarjeta {op.get('id')}: {e}")

    # Espaciado final para que el footer legal no quede pegado
    st.markdown("<br>", unsafe_allow_html=True)
