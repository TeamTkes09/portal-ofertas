import streamlit as st
from data.products import get_news_events

st.title("📰 Noticias de Impacto")
noticias = get_news_events()

for n in noticias:
    with st.chat_message("assistant"):
        st.subheader(n['titulo'])
        st.write(n['descripcion'])
        st.caption(f"Fuente: {n['fuente']} | Hace: {n['hace']}")
