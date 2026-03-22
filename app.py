import streamlit as st
import feedparser
import time

# --- CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="TechFlash | Ofertas al Instante", page_icon="⚡", layout="wide")

# Diseño CSS para máxima velocidad y estética minimalista
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        background-color: #FF9900;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #e68a00; transform: scale(1.02); }
    .offer-card {
        padding: 20px;
        border: 1px solid #e6e9ef;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE DATOS (Con Caché para ser veloz) ---
@st.cache_data(ttl=600) # Guarda los datos 10 minutos para no recargar siempre
def obtener_ofertas():
    urls = [
        "https://wwwhatsnew.com/feed",
        "https://elandroidelibre.elespanol.com/feed",
        "https://vandal.elespanol.com/tecnologia/rss"
    ]
    todas_las_ofertas = []
    for url in urls:
        feed = feedparser.parse(url)
        todas_las_ofertas.extend(feed.entries[:5])
    return todas_las_ofertas

# --- INTERFAZ ---
st.title("⚡ TechFlash")
st.caption("Las mejores ofertas y noticias de tecnología analizadas por IA en tiempo real.")

AMAZON_ID = "unlimited0f3-20"

# Sidebar para filtros rápidos
st.sidebar.title("Filtros")
categoria = st.sidebar.selectbox("Categoría", ["Todo", "Smartphones", "Gaming", "PC", "Hogar"])

# Cuerpo principal
noticias = obtener_ofertas()

# Sistema de columnas para que parezca una tienda moderna
cols = st.columns(2)

for i, nota in enumerate(noticias):
    col = cols[i % 2] # Distribuye en 2 columnas
    with col:
        st.markdown(f"""
        <div class="offer-card">
            <h3>{nota.title}</h3>
            <p style="color: #666;">{nota.published if 'published' in nota else ''}</p>
        </div>
        """, unsafe_allow_html=True)
        
        link_final = f"{nota.link}?tag={AMAZON_ID}"
        st.link_button(f"🛒 Ver en Amazon", link_final)
        st.write("") # Espaciado

st.divider()
st.caption("© 2026 TechFlash Argentina - Sistema de Arbitraje Automático.")