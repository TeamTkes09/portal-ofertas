import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    if not lista_productos:
        st.info("No hay productos disponibles.")
        return
    cols = st.columns(4, gap="small")
    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            costo, venta = op['c'], op['v']
            roi = int(((venta - costo) / costo) * 100) if costo > 0 else 0
            amz_url = f"https://www.amazon{suffix}/dp/{op['q']}"
            comp = {item['sitio']: item['precio'] for item in op['comparativa']}
            filas_html = ""
            puntos = [("Amazon", costo), ("eBay", comp.get('ebay',0)), ("Google", comp.get('google',0)), ("Venta", venta)]
            for sitio, precio in puntos:
                filas_html += f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid #1e293b;"><span style="color:#64748b;font-size:9px;">{sitio}</span><span style="color:#60a5fa;font-size:9px;font-weight:bold;">${precio}</span></div>'
            html = get_card_template(op, roi, round(venta-costo, 2), amz_url, filas_html)
            st.components.v1.html(html, height=225)

def render_crypto_section(lista_crypto):
    st.markdown("### 🧮 Calculadora de Ejecución Inmediata")
    capital = st.number_input("Monto a invertir (USD)", min_value=100, value=1000, step=100)
    
    cols = st.columns(3)
    for i, c in enumerate(lista_crypto):
        with cols[i % 3]:
            buy_p = next(ex['price'] for ex in c['exchanges'] if ex['type'] == "COMPRA")
            sell_p = next(ex['price'] for ex in c['exchanges'] if ex['type'] == "VENTA")
            
            # Cálculo de Arbitraje Real
            cantidad = capital / buy_p
            ganancia_bruta = (cantidad * sell_p) - capital
            costo_red = c['fee_red'] * sell_p
            neto = ganancia_bruta - costo_red
            roi = (neto / capital) * 100

            color_roi = "#22c55e" if neto > 0 else "#ef4444"

            st.markdown(f"""
            <div style="background:#1e293b; border-radius:12px; padding:20px; border:1px solid #334155; color:white;">
                <div style="display:flex; justify-content:space-between;">
                    <h3 style="margin:0; color:#facc15;">{c['coin']}</h3>
                    <small style="color:#94a3b8;">{c['red']}</small>
                </div>
                <hr style="opacity:0.1; margin:10px 0;">
                <div style="display:flex; justify-content:space-between; font-size:12px;">
                    <span>Compra: <b>${buy_p:,}</b></span>
                    <span>Venta: <b>${sell_p:,}</b></span>
                </div>
                <div style="background:#0f172a; padding:10px; border-radius:8px; margin:15px 0;">
                    <div style="display:flex; justify-content:space-between; font-size:11px;">
                        <span>Bruto:</span><span>+${ganancia_bruta:.2f}</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-size:11px; color:#ef4444;">
                        <span>Fee Red:</span><span>-${costo_red:.2f}</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-weight:bold; margin-top:5px; color:{color_roi};">
                        <span>NETO:</span><span>${neto:.2f}</span>
                    </div>
                </div>
                <div style="text-align:center;">
                    <div style="font-size:20px; font-weight:800; color:{color_roi};">{roi:.2f}%</div>
                    <small style="color:#94a3b8;">ROI ESTIMADO</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
