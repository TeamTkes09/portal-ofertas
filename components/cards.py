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
    st.markdown("### 🗺️ Ruta de Ejecución por Red")
    
    # Encabezados de la tabla
    h1, h2, h3, h4, h5, h6 = st.columns([1, 1.5, 1.5, 1, 1, 1])
    h1.write("**Moneda**")
    h2.write("**🛒 COMPRA EN**")
    h3.write("**💰 VENDE EN**")
    h4.write("**🌐 Red**")
    h5.write("**⛽ Fee**")
    h6.write("**📈 Neto**")
    
    st.divider()

    for c in lista_crypto:
        col1, col2, col3, col4, col5, col6 = st.columns([1, 1.5, 1.5, 1, 1, 1])
        
        # Cálculo de ganancia restando el Fee de Red
        diff = c['precio_venta'] - c['precio_compra']
        ganancia_neta = diff - c['fee_usd']
        
        col1.write(f"**{c['coin']}**")
        
        # UI Exchange Compra
        col2.markdown(f"""
            <div style="background:#064e3b; padding:8px; border-radius:5px; text-align:center; border: 1px solid #22c55e;">
                <small style="color:#4ade80;">{c['compra_en']}</small><br>
                <b style="color:white;">${c['precio_compra']:,}</b>
            </div>
        """, unsafe_allow_html=True)
        
        # UI Exchange Venta
        col3.markdown(f"""
            <div style="background:#450a0a; padding:8px; border-radius:5px; text-align:center; border: 1px solid #f87171;">
                <small style="color:#f87171;">{c['vende_en']}</small><br>
                <b style="color:white;">${c['precio_venta']:,}</b>
            </div>
        """, unsafe_allow_html=True)
        
        col4.caption(f"{c['red']}\n({c['vel']})")
        col5.write(f"${c['fee_usd']}")
        
        # Color según rentabilidad
        if ganancia_neta > 0:
            col6.success(f"+${ganancia_neta:.2f}")
        else:
            col6.error(f"${ganancia_neta:.2f}")
