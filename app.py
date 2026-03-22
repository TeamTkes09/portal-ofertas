import streamlit as st
from data.products import get_all_products
from components.cards import render_investment_section

# 1. CONFIGURACIÓN DE PANTALLA (DEBE SER LA PRIMERA LÍNEA)
st.set_page_config(
    page_title="Arbitraje Pro 2026",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CORRECCIÓN DE ERROR: CSS para maximizar espacio
st.markdown("""
    <style>
    /* Elimina márgenes internos para que quepan las 4 columnas */
    .block-container { 
        padding-top: 1rem; 
        padding-bottom: 0rem; 
        padding-left: 1rem; 
        padding-right: 1rem; 
    }
    /* Fuerza a que el contenedor use el 100% del ancho */
    .main .block-container {
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Portal de Arbitraje 2026")

# 3. CARGA Y FILTRO
productos = get_all_products()
categorias = sorted(list(set([p['cat'] for p in productos])))
cat_seleccionada = st.selectbox("Filtrar por Categoría", ["TODAS"] + categorias)

productos_final = productos if cat_seleccionada == "TODAS" else [p for p in productos if p['cat'] == cat_seleccionada]

# 4. RENDER
render_investment_section(".com", productos_final)
