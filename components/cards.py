import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    if not lista_productos: return
    cols = st.columns(4)
    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            costo, venta = op['c'], op['v']
            roi = int(((venta - costo) / costo) * 100)
            amz_url = f"https://www.amazon{suffix}/dp/{op['q']}"
            comp = {item['sitio']: item['precio'] for item in op['comparativa']}
            filas = "".join([f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid #1e293b;"><span style="color:#64748b;font-size:9px;">{s}</span><span style="color:#60a5fa;font-size:9px;">${p}</span></div>' for s,p in [("AMZ", costo), ("EBY", comp.get('ebay',0)), ("Venta", venta)]])
            st.components.v1.html(get_card_template(op, roi, round(venta-costo,2), amz_url, filas), height=225)

def render_crypto_section(lista_crypto):
    st.subheader("🧮 Calculadora de Arbitraje Crypto")
    capital = st.number_input("Capital Operativo (USD)", min_value=100, value=1000)
    
    cols = st.columns(len(lista_crypto))
    for i, c in enumerate(lista_crypto):
        with cols[i]:
            buy_p = c['exchanges'][0]['price']
            sell_p = c['exchanges'][1]['price']
            ganancia_bruta = (capital / buy_p * sell_p) - capital
            costo_red = c['fee_red'] * sell_p
            neto = ganancia_bruta - costo_red
            
            st.markdown(f"""
            <div style="background:#1e293b; padding:20px; border-radius:12px; border:1px solid #334155; color:white;">
                <h3 style="color:#facc15;margin:0;">{c['coin']}</h3>
                <small>Red: {c['red']}</small>
                <hr style="opacity:0.1;">
                <div style="font-size:12px;margin-bottom:10px;">
                    Compra: <b>${buy_p}</b><br>Venta: <b>${sell_p}</b>
                </div>
                <div style="background:#0f172a; padding:10px; border-radius:8px;">
                    <small>Fee Red: -${costo_red:.2f}</small><br>
                    <b style="color:#22c55e;">Neto: ${neto:.2f}</b>
                </div>
                <div style="text-align:center; margin-top:10px; font-size:22px; font-weight:bold; color:#22c55e;">
                    {((neto/capital)*100):.2f}%
                </div>
            </div>
            """, unsafe_allow_html=True)
