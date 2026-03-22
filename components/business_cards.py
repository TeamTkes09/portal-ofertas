import streamlit as st

def render_investment_section(suffix, lista_productos):
    st.markdown("### 🎯 Oportunidades de Arbitraje Verificadas")
    st.info("💡 **Metodología:** Comparamos el costo en Amazon contra los precios actuales en canales de reventa. Haz clic en 'Verificar' para validar la brecha de ganancia.")
    
    # Grid de 3 columnas para que la tabla comparativa se vea bien
    cols = st.columns(3)

    for i, op in enumerate(lista_productos):
        with cols[i % 3]:
            # Cálculos financieros
            margen_neto = op['v'] - op['c']
            roi = int((margen_neto / op['c']) * 100)
            amz_url = f"https://www.amazon{suffix}/s?k={op['q']}&tag=tu-tag-20"

            # Generar filas de la tabla comparativa
            filas_comparativa = ""
            for item in op.get('comparativa', []):
                filas_comparativa += f"""
                <div style="display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px dashed #334155; font-size: 11px;">
                    <span style="color: #94a3b8;">{item['sitio']}</span>
                    <a href="{item['url']}" target="_blank" style="color: #60a5fa; text-decoration: none; font-weight: bold;">${item['precio']} ↗</a>
                </div>
                """

            # HTML de la Tarjeta Profesional
            card_html = f"""
            <div style="
                background-color: #1e293b; 
                border: 1px solid #334155; 
                border-radius: 12px; 
                padding: 20px; 
                margin-bottom: 25px; 
                min-height: 480px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                font-family: sans-serif;
            ">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <span style="background: {op['clr']}; color: white; font-size: 10px; font-weight: 800; padding: 4px 10px; border-radius: 20px;">{op['cat']}</span>
                        <span style="color: #64748b; font-size: 10px; font-weight: bold;">ID: {op['id']}</span>
                    </div>

                    <h4 style="color: white; margin-bottom: 15px; font-size: 15px; line-height: 1.4; font-weight: 600;">{op['n']}</h4>

                    <div style="background: #0f172a; border-radius: 8px; padding: 12px; margin-bottom: 15px; border: 1px solid #1e293b;">
                        <div style="color: #22c55e; font-size: 10px; font-weight: 800; margin-bottom: 8px; letter-spacing: 1px;">ESPECTRO DE REVENTA:</div>
                        {filas_comparativa}
                    </div>

                    <div style="text-align: center; padding: 10px 0;">
                        <div style="font-size: 32px; font-weight: 900; color: {op['clr']}; letter-spacing: -1px;">
                            {roi}% <small style="font-size: 14px; color: #94a3b8;">ROI</small>
                        </div>
                        <div style="font-size: 11px; color: #94a3b8; margin-top: 5px;">
                            Ganancia estimada: <b>${margen_neto}</b> por unidad
                        </div>
                    </div>
                </div>

                <div style="margin-top: 15px;">
                    <div style="font-size: 10px; color: #64748b; text-align: center; margin-bottom: 8px; font-weight: bold;">RIESGO {op['r']}</div>
                    <a href="{amz_url}" target="_blank" style="
                        text-decoration: none; 
                        background: {op['clr']}; 
                        color: white; 
                        text-align: center; 
                        padding: 14px; 
                        border-radius: 8px; 
                        font-weight: 800; 
                        font-size: 14px;
                        display: block;
                        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
                    ">
                        🛒 COMPRAR EN AMAZON
                    </a>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
