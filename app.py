import streamlit as st
import pandas as pd
from data.products import get_all_products
from components.cards import render_investment_section

# 1. CONFIGURACIÓN DE PÁGINA Y LENGUAJE/PAÍS AUTOMÁTICO
# Nota: Streamlit detecta el idioma del navegador, pero aquí damos la opción manual.
st.set_page_config(page_title="Arbitraje Pro 2026", layout="wide", initial_sidebar_state="expanded")

# --- FUNCIONES DE SOPORTE (PAÍS Y LENGUAJE) ---
def get_local_settings():
    col_lang, col_country, col_theme = st.sidebar.columns(3)
    with col_lang:
        lang = st.selectbox("🌐", ["ES", "EN"], help="Idioma / Language")
    with col_country:
        country = st.selectbox("📍", [".com", ".es", ".mx", ".co"], help="Dominio de Amazon")
    with col_theme:
        # El modo Día/Noche en Streamlit se controla mejor desde los settings del usuario, 
        # pero podemos forzar un toggle visual o mensaje.
        theme = st.toggle("🌙", value=True, help="Modo Noche/Día")
    return lang, country, theme

# --- BLOQUE DE SEGURIDAD: BLINDAJE DE RESPONSABILIDAD ---
def render_disclaimer(lang):
    text = {
        "ES": "⚠️ **AVISO LEGAL:** Los datos mostrados son estimaciones de terceros. No garantizamos ganancias. El arbitraje conlleva riesgo de capital.",
        "EN": "⚠️ **LEGAL NOTICE:** Data shown are third-party estimates. Profits are not guaranteed. Arbitrage involves capital risk."
    }
    st.warning(text[lang])

# 2. SIDEBAR (CONTROLES MANUALES)
with st.sidebar:
    st.header("⚙️ Configuración")
    idioma, dominio, modo_noche = get_local_settings()
    st.divider()
    st.info(f"Sistema optimizado para Amazon {dominio}")

# 3. ESTILOS DINÁMICOS (MODO DÍA/NOCHE CUSTOM)
if modo_noche:
    bg_color, text_color = "#0f172a", "#ffffff"
else:
    bg_color, text_color = "#f8fafc", "#1e293b"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; color: {text_color}; }}
    .block-container {{ padding: 1rem 2rem; }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("🚀 Portal de Arbitraje 2026")
render_disclaimer(idioma)

# 4. CARGA DE DATOS
productos = get_all_products()
cat_list = sorted(list(set([p['cat'] for p in productos])))
cat_sel = st.selectbox("Filtrar Categoría", ["TODAS"] + cat_list)

productos_final = productos if cat_sel == "TODAS" else [p for p in productos if p['cat'] == cat_sel]

# 5. SELECTOR DE VISTAS
tab1, tab2 = st.tabs(["🎴 Tarjetas", "📊 Excel"])

with tab1:
    # Pasamos el 'dominio' seleccionado (.com, .mx, etc) dinámicamente
    render_investment_section(dominio, productos_final)

with tab2:
    st.subheader("📊 Reporte de Datos")
    df = pd.DataFrame([{
        "ID": p['id'], "Producto": p['n'], "Costo": p['c'], 
        "Venta": p['v'], "ROI": f"{(p['v']-p['c'])/p['c']*100:.0f}%"
    } for p in productos_final])
    st.dataframe(df, use_container_width=True)
