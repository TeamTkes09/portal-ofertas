import streamlit as st
from data.products import get_real_time_opportunities, get_news_events, get_crypto_opportunities
from components.cards import render_investment_section, render_crypto_section

st.set_page_config(
    page_title="Arbitraje Pro 360", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ⚙️ SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Panel de Control")
    pais = st.selectbox("Mercado Amazon", [".com", ".es", ".mx", ".it"])
    st.divider()
    
    # Widget de Estado del Sistema
    st.success("✅ Conectado a APIs de Exchanges")
    st.info("⏱️ Próximo refresco: 15 min")
    
    st.divider()
    st.markdown("### 📊 Resumen de Mercado")
    st.caption("BTC Dominance: 52.4%")
    st.caption("Gas ETH: 15 Gwei (Bajo)")

# --- 🚀 CUERPO PRINCIPAL ---
st.title("🚀 Sistema de Arbitraje Multisectorial 2026")

t1, t2, t3 = st.tabs(["📰 Noticias de Impacto", "📦 Arbitraje Retail FBA", "₿ Arbitraje Crypto & Redes"])

# PESTAÑA 1: NOTICIAS (Arbitraje Reactivo)
with t1:
    noticias = get_news_events()
    for n in noticias:
        col_n, col_p = st.columns([1, 2])
        with col_n:
            st.warning(f"### {n['titulo']}")
            st.write(n['descripcion'])
            st.caption(f"Fuente: {n['fuente']} | {n['hace']}")
            if n['impacto'] == "CRÍTICO":
                st.error("🔥 IMPACTO CRÍTICO EN PRECIO")
        with col_p: 
            render_investment_section(pais, n['productos_asociados'])
        st.divider()

# PESTAÑA 2: PRODUCTOS FÍSICOS
with t2:
    st.subheader("📦 Oportunidades de Catálogo General")
    render_investment_section(pais, get_real_time_opportunities())

# PESTAÑA 3: CRIPTOMONEDAS (La nueva joya del portal)
with t3:
    st.header("₿ Comparativa de 6 Redes y Exchanges")
    
    # --- BOTÓN DE MÁS INFORMACIÓN ---
    with st.expander("❓ ¿Cómo realizar este Arbitraje paso a paso?", expanded=False):
        st.markdown("""
        ### Guía de Operación Segura
        1. **Detección:** Mira la tabla de abajo. El sistema ya resta el **Costo de Retiro**.
        2. **Compra:** Ve al exchange con el precio más bajo.
        3. **Verificación de Red:** Asegúrate de que ambos exchanges soporten la **misma red** (ej. Solana, Polygon).
        4. **Envío:** Copia la dirección de depósito del Exchange Destino y pégala en el de Origen.
        5. **Venta:** Una vez acreditado, vende por Stablecoin (USDT/USDC).
        
        *Consejo: Empieza con redes como **Solana** o **Polygon** donde el error de comisión es casi cero.*
        """)
    
    # Renderizamos la nueva sección detallada de crypto
    render_crypto_section(get_crypto_opportunities())

# --- FOOTER ---
st.divider()
st.center_text = st.markdown("<center><small>Arbitraje Pro © 2026 | Datos para fines de análisis de mercado</small></center>", unsafe_allow_html=True)
