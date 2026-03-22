import streamlit as st
import urllib.parse
import random

def render_investment_section(suffix):
    st.markdown("### 🏹 Terminal de Arbitraje: Nodos Activos")
    
    # Base de Datos Maestra (24 Nodos)
    oportunidades = [
        # --- HARDWARE ---
        {"n": "SSD Samsung 990 PRO 2TB", "c": 170, "v": 245, "r": "BAJO", "clr": "#22c55e", "q": "samsung 990 pro 2tb", "cat": "💾 HARDWARE"},
        {"n": "Crucial RAM 32GB Kit DDR5", "c": 95, "v": 145, "r": "BAJO", "clr": "#22c55e", "q": "crucial ddr5 32gb kit", "cat": "💾 HARDWARE"},
        {"n": "WD_BLACK 1TB SN850X NVMe", "c": 85, "v": 130, "r": "BAJO", "clr": "#22c55e", "q": "wd black sn850x 1tb", "cat": "💾 HARDWARE"},
        {"n": "Lote x5 Ryzen 5 5600G", "c": 450, "v": 720, "r": "MEDIO", "clr": "#facc15", "q": "ryzen 5 5600g bulk", "cat": "💾 HARDWARE"},
        {"n": "RTX 4060 Ti (Open Box)", "c": 340, "v": 450, "r": "ALTO", "clr": "#ef4444", "q": "rtx 4060 ti open box", "cat": "💾 HARDWARE"},
        {"n": "Corsair RM850e PSU", "c": 115, "v": 175, "r": "BAJO", "clr": "#22c55e", "q": "corsair rm850e", "cat": "💾 HARDWARE"},

        # --- SMART HOME ---
        {"n": "Echo Dot 5 + Philips Hue", "c": 64, "v": 115, "r": "BAJO", "clr": "#22c55e", "q": "echo dot hue bundle", "cat": "🏠 SMART HOME"},
        {"n": "Ring Video Doorbell Wired", "c": 39, "v": 75, "r": "BAJO", "clr": "#22c55e", "q": "ring video doorbell wired", "cat": "🏠 SMART HOME"},
        {"n": "Tapo Smart Plug (4-Pack)", "c": 28, "v": 55, "r": "BAJO", "clr": "#22c55e", "q": "tapo smart plug 4 pack", "cat": "🏠 SMART HOME"},
        {"n": "Apple TV 4K 128GB (2025)", "c": 140, "v": 195, "r": "BAJO", "clr": "#22c55e", "q": "apple tv 4k 128gb", "cat": "🏠 SMART HOME"},

        # --- GAMING ---
        {"n": "Logitech G Pro X Super2", "c": 145, "v": 210, "r": "MEDIO", "clr": "#facc15", "q": "logitech g pro x superlight 2", "cat": "🎮 GAMING"},
        {"n": "Razer BlackShark V2 Pro", "c": 125, "v": 190, "r": "MEDIO", "clr": "#facc15", "q": "razer blackshark v2 pro", "cat": "🎮 GAMING"},
        {"n": "PS5 DualSense Edge", "c": 195, "v": 260, "r": "MEDIO", "clr": "#facc15", "q": "dualsense edge ps5", "cat": "🎮 GAMING"},
        {"n": "ASUS ROG Ally (Renewed)", "c": 450, "v": 590, "r": "ALTO", "clr": "#ef4444", "q": "asus rog ally refurbished", "cat": "🎮 GAMING"},
        {"n": "Nintendo Switch OLED", "c": 290, "v": 385, "r": "MEDIO", "clr": "#facc15", "q": "nintendo switch oled", "cat": "🎮 GAMING"},
        {"n": "Steam Deck 512GB OLED", "c": 540, "v": 690, "r": "ALTO", "clr": "#ef4444", "q": "steam deck oled", "cat": "🎮 GAMING"},

        # --- GADGETS & AUDIO ---
        {"n": "Elgato Stream Deck MK.2", "c": 135, "v": 195, "r": "BAJO", "clr": "#22c55e", "q": "elgato stream deck mk2", "cat": "🎙️ STREAMING"},
        {"n": "Lote x10 USB-C Hub 7-in-1", "c": 110, "v": 250, "r": "ALTO", "clr": "#ef4444", "q": "usb c hub bulk", "cat": "🔌 GADGETS"},
        {"n": "Apple AirTag (Pack de 4)", "c": 79, "v": 125, "r": "BAJO", "clr": "#22c55e", "q": "apple airtag 4 pack", "cat": "🔌 GADGETS"},
        {"n": "Sony WH-1000XM5 (Renewed)", "c": 260, "v": 380, "r": "ALTO", "clr": "#ef4444", "q": "sony wh-1000xm5 renewed", "cat": "🎧 AUDIO"},
        {"n": "Kindle Paperwhite 16GB", "c": 110, "v": 180, "r": "BAJO", "clr": "#22c55e", "q": "kindle paperwhite", "cat": "📖 E-READERS"},
        {"n": "DJI Mini 3 Pro Drone", "c": 620, "v": 850, "r": "ALTO", "clr": "#ef4444", "q": "dji mini 3 pro", "cat": "📸 FOTO/VIDEO"},
        {"n": "GoPro Hero 12 Bundle", "c": 350, "v": 490, "r": "MEDIO", "clr": "#facc15", "q": "gopro hero 12 bundle", "cat": "📸 FOTO/VIDEO"},
        {"n": "Keychron Q1 Mechanical", "c": 160, "v": 235, "r": "MEDIO", "clr": "#facc15", "q": "keychron q1 custom keyboard", "cat": "🎙️ STREAMING"}
    ]

    # Filtros por Categoría y Riesgo
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        cat_list = ["TODOS LOS SECTORES"] + sorted(list(set(op['cat'] for op in oportunidades)))
        sel_cat = st.selectbox("Filtrar Sector:", cat_list)
    with col_f2:
        riesgo_list = ["TODOS", "BAJO", "MEDIO", "ALTO"]
        sel_riesgo = st.selectbox("Nivel de Riesgo:", riesgo_list)

    # Lógica de Filtrado
    items = [o for o in oportunidades if 
             (sel_cat == "TODOS LOS SECTORES" or o['cat'] == sel_cat) and 
             (sel_riesgo == "TODOS" or o['r'] == sel_riesgo)]

    # Grid de 4 Columnas
    cols = st.columns(4)
    for i, op in enumerate(items):
        with cols[i % 4]:
            ganancia = op['v'] - op['c']
            roi = int((ganancia/op['c'])*100)
            amz_url = f"https://www.amazon{suffix}/s?k={urllib.parse.quote(op['q'])}&tag=unlimited0f3-20"
            ref_id = f"TF-{random.randint(100,999)}"
            stock = random.randint(2, 9)

            st.markdown(f"""
                <div style="background:#fff; color:#000; padding:12px; border-radius:10px; border-top:5px solid {op['clr']}; margin-bottom:15px; box-shadow:0 2px 5px rgba(0,0,0,0.1); min-height:220px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                        <span style="font-size:8px; font-weight:800; color:{op['clr']};">{op['cat']}</span>
                        <span style="font-size:8px; color:#94a3b8;">{ref_id}</span>
                    </div>
                    <h4 style="margin:0 0 8px 0; font-size:11px; line-height:1.2; height:28px; overflow:hidden; color:#1e293b;">{op['n']}</h4>
                    <div style="background:#f8fafc; padding:8px; border-radius:6px; margin-bottom:10px; border:1px solid #f1f5f9;">
                        <div style="display:flex; justify-content:space-between; font-size:10px; margin-bottom:2px;">
                            <span style="color:#64748b;">ROI:</span><b style="color:#16a34a;">+{roi}%</b>
                        </div>
                        <div style="display:flex; justify-content:space-between; font-size:10px;">
                            <span style="color:#64748b;">Profit:</span><b style="color:#1e40af;">+${ganancia}</b>
                        </div>
                    </div>
                    <div style="margin-bottom:10px;">
                        <div style="width:100%; background:#e2e8f0; height:3px; border-radius:10px;">
                            <div style="width:{stock*11}%; background:{op['clr']}; height:3px; border-radius:10px;"></div>
                        </div>
                        <p style="font-size:8px; color:#94a3b8; margin-top:4px; text-align:right;">STOCK: {stock} LOTES</p>
                    </div>
                    <a href="{amz_url}" target="_blank" style="background:#fbbf24; color:#000; text-decoration:none; display:block; text-align:center; padding:8px; border-radius:5px; font-weight:800; font-size:10px; border-bottom:2px solid #d97706;">ADQUIRIR NODO</a>
                </div>
            """, unsafe_allow_html=True)
