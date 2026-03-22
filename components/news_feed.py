import streamlit as st
import urllib.parse

def render_news_section(suffix):
    st.markdown("### 📡 TechFlash Live: Oportunidades en Tiempo Real")
    
    # Base de datos con Enlaces de Compra Relacionados
    news_data = [
        {
            "tag": "💾 HW", 
            "title": "Escasez de chips H100", 
            "desc": "El mercado de reventa sube un 12%. Revisa existencias de GPUs profesionales.", 
            "time": "5m", "type": "warning",
            "link_query": "NVIDIA RTX 6000 Ada" # Producto profesional alternativo
        },
        {
            "tag": "🔥 IA", 
            "title": "Nuevas Mac con M4", 
            "desc": "Apple prioriza chips para IA. Los modelos M3 podrían entrar en liquidación.", 
            "time": "12m", "type": "info",
            "link_query": "MacBook Pro M3 Max"
        },
        {
            "tag": "🎮 GAME", 
            "title": "PS5 Pro Reacondicionadas", 
            "desc": "Stock detectado en almacenes oficiales. Alta demanda esperada.", 
            "time": "28m", "type": "success",
            "link_query": "PS5 Pro Console"
        },
        {
            "tag": "🎧 AUDIO", 
            "title": "Lanzamiento Sony XM6", 
            "desc": "Filtración inminente. El stock de XM5 está bajando de precio para limpiar inventario.", 
            "time": "45m", "type": "warning",
            "link_query": "Sony WH-1000XM5"
        }
    ]

    cols = st.columns(4)
    for i, item in enumerate(news_data):
        with cols[i]:
            # Generar link de Amazon basado en la noticia
            query = urllib.parse.quote(item["link_query"])
            amz_url = f"https://www.amazon{suffix}/s?k={query}&tag=unlimited0f3-20"
            
            color_map = {"info": "#0ea5e9", "success": "#22c55e", "warning": "#f59e0b"}
            
            st.markdown(f"""
                <div style="background: #1e293b; padding: 12px; border-left: 4px solid {color_map[item['type']]}; border-radius: 5px; margin-bottom: 10px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                            <span style="font-size: 8px; font-weight: 800; color: {color_map[item['type']]}; background: rgba(0,0,0,0.2); padding: 2px 5px; border-radius: 3px;">{item['tag']}</span>
                            <span style="font-size: 8px; color: #64748b;">{item['time']}</span>
                        </div>
                        <p style="margin: 0; font-size: 11px; font-weight: 700; color: #f8fafc; line-height: 1.2;">{item['title']}</p>
                        <p style="margin: 5px 0 0 0; font-size: 10px; color: #94a3b8; line-height: 1.3;">{item['desc']}</p>
                    </div>
                    <a href="{amz_url}" target="_blank" style="display: block; background: {color_map[item['type']]}; color: white; text-align: center; padding: 4px; border-radius: 3px; font-size: 9px; font-weight: bold; text-decoration: none; margin-top: 10px;">
                        🛒 VER OFERTA RELACIONADA
                    </a>
                </div>
            """, unsafe_allow_html=True)
