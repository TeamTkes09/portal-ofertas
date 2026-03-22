import streamlit as st
import urllib.parse
import random

def render_investment_section(suffix):
    st.markdown("### 🏹 Terminal de Análisis: Nodos de Mercado")
    st.caption("⚠️ Los valores mostrados son proyecciones de mercado basadas en precios actuales.")

    # Base de Datos con IDs FIJOS
    oportunidades = [
        {"id": "101", "n": "SSD Samsung 990 PRO 2TB", "c": 170, "v": 245, "r": "BAJO", "clr": "#22c55e", "q": "samsung 990 pro 2tb", "cat": "💾 HARDWARE"},
        {"id": "102", "n": "Crucial RAM 32GB Kit DDR5", "c": 95, "v": 145, "r": "BAJO", "clr": "#22c55e", "q": "crucial ddr5 32gb kit", "cat": "💾 HARDWARE"},
        {"id": "103", "n": "WD_BLACK 1TB SN850X NVMe", "c": 85, "v": 130, "r": "BAJO", "clr": "#22c55e", "q": "wd black sn850x 1tb", "cat": "💾 HARDWARE"},
        {"id": "104", "n": "Lote x5 Ryzen 5 5600G", "c": 450, "v": 720, "r": "MEDIO", "clr": "#facc15", "q": "ryzen 5 5600g bulk", "cat": "💾 HARDWARE"},
        {"id": "105", "n": "RTX 4060 Ti (Open Box)", "c": 340, "v": 450, "r": "ALTO", "clr": "#ef4444", "q": "rtx 4060 ti open box", "cat": "💾 HARDWARE"},
        {"id": "106", "n": "Corsair RM850e PSU", "c": 115, "v": 175, "r": "BAJO", "clr": "#22c55e", "q": "corsair rm850e", "cat": "💾 HARDWARE"},
        {"id": "201", "n": "Echo Dot 5 + Philips Hue", "c": 64, "v": 115, "r": "BAJO", "clr": "#22c55e", "q": "echo dot hue bundle", "cat": "🏠 SMART HOME"},
        {"id": "202", "n": "Ring Video Doorbell Wired", "c": 39, "v": 75, "r": "BAJO", "clr": "#22c55e", "q": "ring video doorbell wired", "cat": "🏠 SMART HOME"},
        {"id": "203", "n": "Tapo Smart Plug (4-Pack)", "c": 28, "v": 55, "r": "BAJO", "clr": "#22c55e", "q": "tapo smart plug 4 pack", "cat": "🏠 SMART HOME"},
        {"id": "204", "n": "Apple TV 4K 128GB (2025)", "c": 140, "v": 195, "r": "BAJO", "clr": "#22c55e", "q": "apple tv 4k 128gb", "cat": "🏠 SMART HOME"},
        {"id": "301", "n": "Logitech G Pro X Super2", "c": 145, "v": 210, "r": "MEDIO", "clr": "#facc15", "q": "logitech g pro x superlight 2", "cat": "🎮 GAMING"},
        {"id": "302", "n": "Razer BlackShark V2 Pro", "c": 125, "v": 190, "r": "MEDIO", "clr": "#facc15", "q": "razer blackshark v2 pro", "cat": "🎮 GAMING"},
        {"id": "303", "n": "PS5 DualSense Edge", "c": 195, "v": 260, "r": "MEDIO", "clr": "#facc15", "q": "dualsense edge ps5", "cat": "🎮 GAMING"},
        {"id": "304", "n": "ASUS ROG Ally (Renewed)", "c": 450, "v": 590, "r": "ALTO", "clr": "#ef4444", "q": "asus rog ally refurbished", "cat": "🎮 GAMING"},
        {"id": "401", "n": "Elgato Stream Deck MK.2", "c": 135, "v": 195, "r": "BAJO", "clr": "#22c55e", "q": "elgato stream deck mk2", "cat": "🎙️ STREAMING"},
        {"id": "402", "n": "Lote x10 USB-C Hub 7-in-1", "c": 110, "v": 250, "r": "ALTO", "clr": "#ef4444", "q": "usb c hub bulk", "cat": "🔌 GADGETS"},
        {"id": "403", "n": "Apple AirTag (Pack de 4)", "c": 79, "v": 125, "r": "BAJO", "clr": "#22c55e", "q": "apple airtag 4 pack", "cat": "🔌 GADGETS"},
        {"id": "404", "n": "Sony WH-1000XM5 (Renewed)", "c": 260, "v": 380, "r": "ALTO", "clr": "#ef4444", "q": "sony wh-1000xm5 renewed", "cat": "🎧 AUDIO"},
        {"id": "405", "n": "Kindle Paperwhite 16GB", "c": 110, "v": 180, "r": "BAJO", "clr": "#22c55e", "q": "kindle paperwhite", "cat": "📖 E-READERS"},
        {"id": "406", "n": "DJI Mini 3 Pro Drone", "c": 620, "v": 850, "r": "ALTO", "clr": "#ef4444", "q": "dji mini 3 pro", "cat": "📸 FOTO/VIDEO"},
        {"id": "407", "n": "GoPro Hero 12 Bundle", "c": 350, "v": 490, "r": "MEDIO", "clr": "#facc15", "q": "gopro hero 12 bundle", "cat": "📸 FOTO/VIDEO"},
        {"id": "408", "n": "Keychron Q1 Mechanical", "c": 160, "v": 235, "r": "MEDIO", "clr": "#facc15", "q": "keychron q1 custom keyboard", "cat": "🎙️ STREAMING"}
    ]

    # Filtros
    f1, f2 = st.columns([2, 1])
    with f1:
        cat_list = ["TODOS LOS SECTORES"] + sorted(list(set(op['cat'] for op in oportunidades)))
        sel_cat = st.selectbox("Seleccionar Sector:", cat_list)
    with f2:
        sel_riesgo = st.selectbox("Riesgo Percibido:", ["TODOS", "BAJO", "MEDIO", "ALTO"])

    # Filtrado
    items = [o for o in oportunidades if 
             (sel_cat == "TODOS LOS SECTORES" or o['cat'] == sel_cat) and 
             (sel_riesgo == "TODOS" or o['r'] == sel_riesgo)]

    # Renderizado - AQUÍ ESTABA EL ERROR: Aseguramos el contexto de columna
    cols = st.columns(4)
    for i, op in enumerate(items):
        col_index = i % 4
        with cols[col_index]:
            margen = op['v'] - op['c']
            roi = int((margen/op['c'])*100)
            amz_url = f"https://www.amazon{suffix}/s?k={urllib.parse.quote(op['q'])}&tag=unlimited0f3-20"
            stock = random.randint(2, 9)
            
            # Encapsulamos todo el HTML en una sola cadena limpia
            card_html = f"""
            <div style="background:white; border-top:4px solid {op['clr']}; padding:10px; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1); margin-bottom:15px; min-height:240px; font-family:sans-serif;">
                <div style="display:flex; justify-content:space-between; font-size:8px; margin-bottom:5px;">
                    <b style="color:{op['clr']};">{op['cat']}</b>
                    <span style="color:#94a3b8;">TF-{op['id']}</span>
                </div>
                <h4 style="font-size:11px; margin:5px 0; color:#1e293b; height:30px; overflow:hidden;">{op['n']}</h4>
                <div style="background:#f8fafc; padding:5px; border-radius:4px; font-size:10px; border:1px solid #edf2f7;">
                    <div style="display:flex; justify-content:space-between;"><span>ROI Proyectado:</span><b style="color:#16a34a;">+{roi}%</b></div>
                    <div style="display:flex; justify-content:space-between;"><span>Margen Est. (*):</span><b style="color:#1e40af;">+${margen}</b></div>
                </div>
                <div style="margin-top:10px;">
                    <div style="width:100%; background:#edf2f7; height:3px; border-radius:2px;">
                        <div style="width:{stock*11}%; background:{op['clr']}; height:3px; border-radius:2px;"></div>
                    </div>
                    <p style="font-size:8px; text-align:right; color:#94a3b8; margin:2px 0;">STOCK: {stock} Ltes</p>
                </div>
                <a href="{amz_url}" target="_blank" style="display:block; background:#fbbf24; color:black; text-align:center; padding:6px; border-radius:4px; font-size:10px; font-weight:bold; text-decoration:none; margin-top:10px; border-bottom:2px solid #d97706;">ADQUIRIR NODO</a>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("<p style='font-size:10px; color:#94a3b8; text-align:center; margin-top:20px;'>(*) Los márgenes son estimaciones brutas. No incluyen envíos ni impuestos locales.</p>", unsafe_allow_html=True)
