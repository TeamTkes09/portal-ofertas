import streamlit as st
import datetime

def render_news_section():
    st.markdown("### 📡 TechFlash Live")
    
    # Simulación de Noticias en Tiempo Real (Respaldo)
    # Esto asegura que NUNCA se quede en "Cargando..."
    news_data = [
        {
            "tag": "🔥 IA",
            "title": "OpenAI Sora expande acceso a creadores",
            "desc": "La generación de video hiperrealista llega a más usuarios Pro este mes.",
            "time": "15m",
            "type": "info"
        },
        {
            "tag": "💾 HARDWARE",
            "title": "Escasez de chips H100 impacta precios",
            "desc": "El mercado de reventa de GPUs de IA sube un 12% en la última semana.",
            "time": "34m",
            "type": "warning"
        },
        {
            "tag": "📈 MERCADO",
            "title": "Amazon Prime Day confirmado para Julio",
            "desc": "Se espera un volumen récord de lotes de liquidación para arbitraje.",
            "time": "1h",
            "type": "success"
        }
    ]

    cols = st.columns(len(news_data))

    for i, item in enumerate(news_data):
        with cols[i]:
            if item["type"] == "info":
                st.info(f"**{item['tag']}**\n\n{item['title']}\n\n*{item['desc']}*")
            elif item["type"] == "warning":
                st.warning(f"**{item['tag']}**\n\n{item['title']}\n\n*{item['desc']}*")
            else:
                st.success(f"**{item['tag']}**\n\n{item['title']}\n\n*{item['desc']}*")
            st.caption(f"🕒 Hace {item['time']}")

    st.divider()
