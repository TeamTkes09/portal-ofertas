import streamlit as st
import urllib.parse
import random

def render_investment_section(suffix):
    st.markdown("### 🏹 Nodos de Arbitraje Disponibles")
    
    # Base de Datos Expandida
    oportunidades = [
        {"n": "Echo Dot 5th Gen + Philips Hue", "c": 64, "v": 115, "r": "BAJO", "clr": "#22c55e", "q": "echo dot hue bundle", "cat": "🏠 SMART HOME"},
        {"n": "SSD Samsung 990 PRO 2TB", "c": 170, "v": 245, "r": "BAJO", "clr": "#22c55e", "q": "samsung 990 pro 2tb", "cat": "💾 HARDWARE"},
        {"n": "Logitech G Pro X Superlight 2", "c": 145, "v": 210, "r": "MEDIO", "clr": "#facc15", "q": "logitech g pro x superlight 2", "cat": "🎮 GAMING"},
        {"n": "Elgato Stream Deck MK.2", "c": 135, "v": 195, "r": "BAJO", "clr": "#22c55e", "q": "elgato stream deck mk2", "cat": "🎙️ STREAMING"},
        {"n": "Lote x10 USB-C Hub 7-in-1", "c": 110, "v": 250, "r": "ALTO", "clr": "#ef4444", "q": "usb c hub bulk", "cat": "🔌 GADGETS"},
        {"n": "Razer BlackShark V2 Pro", "c": 125, "v": 190, "r": "MEDIO", "clr": "#facc15", "q": "razer blackshark v2 pro", "cat": "🎮 GAMING"},
        {"n": "Crucial RAM 32GB Kit DDR5", "c": 95, "v": 145, "r": "BAJO", "clr": "#22c55e", "q": "crucial ddr5 32gb kit", "cat": "💾 HARDWARE"},
        {"n": "Sony WH-1000XM5 (Open Box)", "c": 280, "v": 410, "r": "ALTO", "clr": "#ef4444", "q": "sony wh-1000xm5 refurbished", "cat": "🎧 AUDIO"},
        {"n": "Kindle Paperwhite 16GB", "c": 110, "v": 180, "r": "BAJO", "clr": "#22c55e", "q": "kindle paperwhite", "cat": "📖 E-READERS"},
        {"n": "Apple AirTag (Pack de 4)", "c": 79, "v": 125, "r": "BAJO", "clr": "#22c55e", "q": "apple airtag 4 pack", "cat": "🔌 GADGETS"}
    ]

    # Barra de Filtros
    categorias = ["TODOS"] + sorted(list(set(op['cat'] for op in oportunidades)))
    seleccion = st.selectbox("Seleccione un Nicho de Mercado:", categorias)

    # Filtrado lógico
    items = oportunidades if seleccion == "TODOS" else [o for o in oportunidades if o['cat'] == seleccion]

    # Renderizado en 3 Columnas
    cols = st.columns(3)
    for i, op in enumerate(items):
        with cols[i % 3]:
            ganancia = op['v'] - op['c']
            roi = int((ganancia/op['c'])*100)
            amz_url = f"https://www.amazon{suffix}/s?k={urllib.parse.quote(op['q'])}&tag=unlimited0f3-20"
            ref_id = f"TF-{random.randint(100,999)}"
            
            st.markdown(f"""
                <div style="background:#fff; color:#000; padding:15px; border-radius:12px; border-left:6px solid {op['clr']}; margin-bottom:20px; box-shadow:0 2px 8px rgba(0,0,0,0.1); min-height:220px; font-family: sans-serif;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <small style="color:#64748b; font-weight:800; font-size:10px;">{op['cat']}</small>
                        <small style="color:#94a3b8; font-size:9px;">{ref_id}</small>
                    </div>
                    <h4 style="margin:8px 0; font-size:14px; line-height:1.2; color:#1e293b;">{op['n']}</h4>
                    <div style="background:#f8fafc; padding:10px; border-radius:8px; margin:10px 0; border:1px solid #e2e8f0;">
                        <div style="display:flex; justify-content:space-between; font-size:11px; margin-bottom:3px;">
                            <span style="color:#64748b;">ROI Estimado:</span>
                            <b style="color:#16a34a;">+{roi}%</b>
                        </div>
                        <div style="display:flex; justify-content:space-between; font-size:11px;">
                            <span style="color:#64748b;">Profit Neto:</span>
                            <b style="color:#1e40af;">+${ganancia}</b>
                        </div>
                    </div>
                    <a href="{amz_url}" target="_blank" style="background:#fbbf24; color:#000; text-decoration:none; display:block; text-align:center; padding:10px; border-radius:6px; font-weight:bold; font-size:11px; border-bottom: 2px solid #d97706;">ADQUIRIR LOTE</a>
                </div>
            """, unsafe_allow_html=True)
