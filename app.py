import streamlit as st
import pandas as pd
from data.products import get_real_time_opportunities, get_news_events
from components.cards import render_investment_section

st.set_page_config(layout="wide", page_title="Arbitraje Inteligente 2026")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .news-card { background: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #22c55e; margin-bottom: 20px; }
    .source { color: #94a3b8; font-size: 0.8rem; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Centro de Mando de Arbitraje")

# Pestañas
tab_news, tab_prod, tab_crypto = st.tabs(["📰 Noticias y Oportunidades", "📦 Catálogo General", "₿ Cripto-Exchanges"])

with tab_news:
    st.subheader("🔥 Eventos de Mercado en Tiempo Real")
    st.caption("Productos detectados por alta demanda o ruptura de stock inminente.")
    
    eventos = get_news_events()
    
    for ev in eventos:
        with st.container():
            # Layout de la noticia
            col_text, col_prod = st.columns([1, 2])
            
            with col_text:
                st.markdown(f"""
                <div class="news-card">
                    <div class="source">{ev['fuente']} • {ev['hace']}</div>
                    <h4>{ev['titulo']}</h4>
                    <p style="font-size: 0.9rem;">{ev['descripcion']}</p>
                    <span style="background: #064e3b; color: #4ade80; padding: 2px 8px; border-radius: 10px; font-size: 0.7rem;">Impacto: {ev['impacto']}</span>
                </div>
                """, unsafe_allow_html=True)
            
            with col_prod:
                # Renderizamos solo los productos que responden a esa noticia
                render_investment_section(".com", ev['productos_asociados'])
        st.divider()

with tab_prod:
    prods = get_real_time_opportunities()
    render_investment_section(".com", prods)

# ... resto de pestañas ...
