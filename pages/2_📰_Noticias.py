import streamlit as st
from data.products import get_news_events

st.title("📰 Noticias de Impacto Económico")

for n in get_news_events():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.error(f"**{n['impacto']}**") if n['impacto'] == "ALTO" else st.info(f"**{n['impacto']}**")
    with col2:
        st.subheader(n['titulo'])
        st.write(n['descripcion'])
        st.caption(f"Fuente: {n['fuente']} | {n['hace']}")
    st.divider()
