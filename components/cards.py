import streamlit as st

def render_crypto_section(lista_crypto):
    st.info("💡 **Estrategia:** Compra en el exchange verde, transfiere por la red indicada y vende en el rojo.")
    
    # Input de capital para cálculo dinámico
    capital = st.number_input("Capital a invertir (USD)", min_value=100, value=1000, step=100)
    
    cols = st.columns(3)
    for i, c in enumerate(lista_crypto):
        with cols[i % 3]:
            # Lógica de cálculo
            buy_p = next(ex['price'] for ex in c['exchanges'] if ex['type'] == "COMPRA")
            sell_p = next(ex['price'] for ex in c['exchanges'] if ex['type'] == "VENTA")
            
            # Cálculo de cantidad y ganancia
            cantidad = capital / buy_p
            ganancia_bruta = (cantidad * sell_p) - capital
            costo_transferencia = c['fee_red'] * sell_p
            ganancia_neta = ganancia_bruta - costo_transferencia
            roi_neto = (ganancia_neta / capital) * 100

            st.markdown(f"""
            <div style="background: #1e293b; border-radius: 12px; padding: 20px; border: 1px solid #334155; color: white;">
                <div style="display: flex; justify-content: space-between;">
                    <h2 style="margin:0; color: #facc15;">{c['coin']}</h2>
                    <span style="font-size: 0.8rem; color: #94a3b8;">Red: {c['red']}</span>
                </div>
                <hr style="opacity: 0.2; margin: 15px 0;">
                
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>🛒 Compra (Min):</span>
                    <b style="color: #22c55e;">${buy_p:,}</b>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                    <span>💰 Venta (Max):</span>
                    <b style="color: #60a5fa;">${sell_p:,}</b>
                </div>

                <div style="background: #0f172a; border-radius: 8px; padding: 12px; margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem;">
                        <span>Ganancia Bruta:</span>
                        <span>+${ganancia_bruta:.2f}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #ef4444;">
                        <span>Fee de Red:</span>
                        <span>-${costo_transferencia:.2f}</span>
                    </div>
                    <hr style="opacity: 0.1; margin: 8px 0;">
                    <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 1.1rem; color: #22c55e;">
                        <span>NETO:</span>
                        <span>${ganancia_neta:.2f}</span>
                    </div>
                </div>
                
                <div style="text-align: center;">
                    <small style="color: #94a3b8;">ROI NETO FINAL</small>
                    <div style="font-size: 1.5rem; font-weight: 800; color: #facc15;">{roi_neto:.2f}%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
