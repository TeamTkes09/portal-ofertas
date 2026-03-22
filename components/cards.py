import streamlit as st
from styles.html_templates import get_card_template

def render_investment_section(suffix, lista_productos):
    if not lista_productos:
        st.write("No hay productos.")
        return
    cols = st.columns(4, gap="small")
    for i, op in enumerate(lista_productos):
        with cols[i % 4]:
            costo, venta = op['c'], op['v']
            roi = int(((venta - costo) / costo) * 100) if costo > 0 else 0
            amz_url = f"https://www.amazon{suffix}/dp/{op['q']}"
            comp = {item['sitio']: item['precio'] for item in op['comparativa']}
            puntos = [("Amazon", costo), ("eBay", comp.get('ebay', 0)), ("Google", comp.get('google', 0)), ("Venta", venta)]
            filas_html = ""
            for sitio, precio in puntos:
                filas_html += f'<div style="display: flex; justify-content: space-between; border-bottom: 1px solid #1e293b; padding: 1px 0;"><span style="color: #64748b; font-size: 9px;">{sitio}</span><span style="color: #60a5fa; font-size: 9px; font-weight: bold;">${precio}</span></div>'
            html = get_card_template(op, roi, round(venta-costo, 2), amz_url, filas_html)
            st.components.v1.html(html, height=225)

def render_crypto_section(lista_crypto):
    cols = st.columns(3)
    for i, c in enumerate(lista_crypto):
        with cols[i % 3]:
            ex_html = "".join([f'<div style="display:flex; justify-content:space-between; font-size: 12px; margin: 4px 0; color: white;"><span>{ex["name"]}</span><b style="color:{"#22c55e" if ex["type"]=="COMPRA" else "#ef4444" if ex["type"]=="VENTA" else "white"}">${ex["price"]}</b></div>' for ex in c['exchanges']])
            st.markdown(f"""<div style="background: #1e293b; border-radius: 10px; padding: 15px; border: 1px solid #334155; color: white;"><h3 style="color: gold; margin: 0;">{c['coin']}</h3><p style="font-size: 20px; font-weight: bold; color: #22c55e; margin: 10px 0;">Gap: ${c['gap']}</p><hr style="border-color: #334155;">{ex_html}</div>""", unsafe_allow_html=True)
