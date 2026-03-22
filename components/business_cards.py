import streamlit as st

def render_investment_section(suffix, lista_productos):
    """
    Renderiza las tarjetas basadas en la lista filtrada/ordenada que recibe.
    """
    # 1. Título de la sección
    st.markdown("### 🎯 Oportunidades Seleccionadas (Alta Rentabilidad)")
    st.caption(f"Mostrando {len(lista_productos)} activos detectados en Amazon{suffix}")

    # 2. Configuración de Rejilla (Grid)
    # Usamos 4 columnas para escritorio, se adaptará en móvil automáticamente
    cols = st.columns(4)

    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            # Cálculos de negocio rápidos
            margen = op['v'] - op['c']
            roi = int((margen / op['c']) * 100)
            
            # Construcción de la URL de afiliado
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # HTML de la Tarjeta (Diseño Premium)
            card_html = f"""
            <div style="
                background-color: #1e293b; 
                border: 1px solid #334155; 
                border-radius: 12px; 
                padding: 15px; 
                margin-bottom: 20px; 
                transition: transform 0.3s;
                height: 380px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            ">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <span style="background: {op['clr']}; color: white; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 20px;">
                            {op['cat']}
                        </span>
                        <span style="color: #94a3b8; font-size: 10px; font-weight: bold;">ID: {op['id']}</span>
                    </div>
                    
                    <h4 style="color: white; margin: 12px 0 8px 0; font-size: 14px; line-height: 1.3;">{op['n']}</h4>
                    
                    <div style="background: #0f172a; border-radius: 8px; padding: 10px; margin: 10px 0;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="color: #94a3b8; font-size: 11px;">Costo:</span>
                            <span style="color: white; font-size: 11px; font-weight: bold;">${op['c']}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #94a3b8; font-size: 11px;">Venta Est:</span>
                            <span style="color: #22c55e; font-size: 11px; font-weight: bold;">${op['v']}</span>
                        </div>
                    </div>

                    <div style="text-align: center; margin-top: 10px;">
                        <div style="font-size: 24px; font-weight: 900; color: {op['clr']};">{roi}% <small style="font-size: 12px;">ROI</small></div>
                        <div style="font-size: 10px; color: #64748b; font-weight: bold;">RIESGO {op['r']}</div>
                    </div>
                </div>

                <a href="{amz_url}" target="_blank" style="
                    text-decoration: none; 
                    background: {op['clr']}; 
                    color: white; 
                    text-align: center; 
                    padding: 10px; 
                    border-radius: 8px; 
                    font-weight: 800; 
                    font-size: 12px;
                    display: block;
                    margin-top: 15px;
                ">
                    🛒 COMPRAR LOTE
                </a>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
