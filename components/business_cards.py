import streamlit as st

def render_investment_section(suffix, lista_productos):
    st.markdown("### 🎯 Oportunidades Seleccionadas (Alta Rentabilidad)")
    st.caption(f"Mostrando {len(lista_productos)} activos detectados en Amazon{suffix}")

    # Creamos las 4 columnas
    cols = st.columns(4)

    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            # Cálculos de ROI
            margen = op['v'] - op['c']
            roi = int((margen / op['c']) * 100)
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # Diseño de la tarjeta en un solo bloque HTML
            card_html = f"""
            <div style="
                background-color: #1e293b; 
                border: 1px solid #334155; 
                border-radius: 12px; 
                padding: 15px; 
                margin-bottom: 20px; 
                height: 420px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                font-family: sans-serif;
            ">
                <div style="width: 100%;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <span style="background: {op['clr']}; color: white; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 20px; text-transform: uppercase;">
                            {op['cat']}
                        </span>
                        <span style="color: #94a3b8; font-size: 10px; font-weight: bold;">ID: {op['id']}</span>
                    </div>
                    
                    <h4 style="
                        color: white; 
                        margin: 15px 0 10px 0; 
                        font-size: 14px; 
                        line-height: 1.3; 
                        font-weight: 600;
                        display: -webkit-box;
                        -webkit-line-clamp: 2;
                        -webkit-box-orient: vertical;
                        overflow: hidden;
                        height: 36px;
                    ">
                        {op['n']}
                    </h4>
                    
                    <div style="background: #0f172a; border-radius: 8px; padding: 12px; margin: 10px 0; border: 1px solid #1e293b;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                            <span style="color: #94a3b8; font-size: 11px;">Costo Amazon:</span>
                            <span style="color: white; font-size: 11px; font-weight: bold;">${op['c']}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #94a3b8; font-size: 11px;">Venta Estimada:</span>
                            <span style="color: #22c55e; font-size: 11px; font-weight: bold;">${op['v']}</span>
                        </div>
                    </div>

                    <div style="text-align: center; margin-top: 15px; padding: 5px; border-top: 1px solid #334155;">
                        <div style="font-size: 26px; font-weight: 900; color: {op['clr']}; letter-spacing: -1px;">
                            {roi}% <small style="font-size: 12px; color: #94a3b8;">ROI</small>
                        </div>
                        <div style="font-size: 10px; color: #64748b; font-weight: 800; letter-spacing: 1px; margin-top: 4px;">
                            RIESGO {op['r']}
                        </div>
                    </div>
                </div>

                <a href="{amz_url}" target="_blank" style="
                    text-decoration: none; 
                    background: {op['clr']}; 
                    color: white; 
                    text-align: center; 
                    padding: 12px; 
                    border-radius: 8px; 
                    font-weight: 800; 
                    font-size: 13px;
                    display: block;
                    width: 100%;
                ">
                    🛒 COMPRAR LOTE
                </a>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
