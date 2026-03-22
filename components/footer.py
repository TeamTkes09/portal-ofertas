import streamlit as st
import datetime

def render_legal_bunker():
    st.markdown(f'''
        <div style="background:#000; padding:40px; margin-top:100px; font-size:10px; color:#444; border-top:1px solid #222;">
            <strong>TECHFLASH780 - BLINDAJE JURÍDICO GLOBAL</strong><br>
            Este sitio utiliza enlaces de afiliados. Las proyecciones de ROI son informativas. 
            El usuario asume el riesgo comercial y legal en su jurisdicción local.
            <br>© {datetime.datetime.now().year} TechFlash Pro.
        </div>
    ''', unsafe_allow_html=True)
    st.link_button("☕ Support Dev", "https://paypal.me/TechFlash780")
