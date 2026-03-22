import streamlit as st
import urllib.parse

def render_news_section(suffix):
    st.markdown("### 📡 TechFlash Live: Oportunidades en Tiempo Real")
    
    # CSS para el efecto de parpadeo (Blink)
    st.markdown("""
        <style>
        @keyframes blinker {  
            50% { opacity: 0.4; }
        }
        .urgent-blink {
            animation: blinker 1.5s linear infinite;
            background: #ef4444 !important;
            color: white !important;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 800;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Datos con Consultas de Compra Estratégicas
    news_data = [
        {
            "tag": "⚠️ URGENTE", 
            "title": "Escasez Chips H100", 
            "desc": "Stock global bajo mínimos. Las alternativas workstation están subiendo.", 
            "time": "2m", "type": "warning",
            "link_query": "NVIDIA RTX 6000 Ada",
            "blink": True
        },
        {
            "tag": "🔥 IA", 
            "title": "Lanzamiento M4 Ultra", 
            "desc": "Apple renueva stock. Los modelos M2/M3 entran en fase de liquidación.", 
            "time": "15m", "type": "info",
            "link_query": "MacBook Pro M3 Max",
            "blink": False
        },
        {
            "tag": "💎 OPORTUNIDAD", 
            "title": "PS5 Pro Refurbished", 
            "desc": "Amazon Warehouse detecta 15 unidades. Margen de reventa: 35%.", 
            "time": "32m", "type": "success",
            "link_query": "PS5 Pro Console refurbished",
            "blink": False
        },
        {
            "tag": "⚡ MERCADO", 
            "title": "Sony XM5 vs XM6", 
            "desc": "Bajada de precio agresiva en XM5 por cambio de generación inminente.", 
            "time": "50m", "type": "warning",
            "link_query": "Sony WH-1000XM5",
            "blink": True
        }
    ]

    cols = st.columns(4)
    for i, item in enumerate(news_data):
        with cols[i]:
            query = urllib.parse.quote(item["link_query"])
            amz_url = f"https://www.amazon{suffix}/s?k={query}&tag=unlimited0f3-20"
            
            # Colores dinámicos
            color_map = {"info": "#0ea5e9", "success": "#22c55e", "warning": "#f59e0b"}
            tag_class = "urgent-blink" if item["blink"] else ""
            tag_style = f"font-size: 8px; font-weight: 800; color: white; background: {color_map[item['type']]}; padding: 2px 5px; border-radius: 3px;" if not item["blink"] else ""

            st.markdown(f"""
                <div style="background: #1e293b; padding: 12px; border-bottom: 3px solid {color_map[item['type']]}; border-radius: 8px; margin-bottom: 10px; min-height: 180px; display: flex; flex-direction: column; justify-content: space-between; border: 1px solid #334155;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span class="{tag_class}" style="{tag_style}">{item['tag']}</span>
                            <span style="font-size: 8px; color: #64748b; font-weight: bold;">{item['time']}</span>
                        </div>
                        <p style="margin: 0; font-size: 11px; font-weight: 700; color: #f8fafc; line-height: 1.2;">{item['title']}</p>
                        <p style="margin: 6px 0 0 0; font-size: 10px; color: #94a3b8; line-height: 1.4; height: 40px; overflow: hidden;">{item['desc']}</p>
                    </div>
                    <a href="{amz_url}" target="_blank" style="display: block; background: #fbbf24; color: #000; text-align: center; padding: 6px; border-radius: 4px; font-size:
