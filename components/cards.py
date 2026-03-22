import streamlit as st
import pandas as pd

def render_crypto_section(lista_crypto):
    if not lista_crypto:
        st.error("No se pudieron obtener datos reales. Verifica tu conexión.")
        return

    st.markdown("### 🏦 Monitor de Arbitraje Real (Top 200)")
    
    df = pd.DataFrame(lista_crypto)
    
    # --- CÁLCULOS DE VALOR REAL ---
    df['Spread USD'] = df['Precio Venta'] - df['Precio Compra']
    df['Ganancia Neta'] = df['Spread USD'] - df['Fee Red']
    df['ROI %'] = (df['Ganancia Neta'] / df['Precio Compra']) * 100

    # Buscador dinámico
    col1, col2 = st.columns([2, 1])
    search = col1.text_input("🔍 Buscar Token...").upper()
    min_roi = col2.slider("Filtrar ROI Mínimo %", -0.5, 2.0, 0.0, step=0.1)

    if search:
        df = df[df['Token'].str.contains(search)]
    
    df = df[df['ROI %'] >= min_roi]

    # Visualización estilo Terminal Financiera
    st.dataframe(
        df.sort_values(by="ROI %", ascending=False),
        column_config={
            "Precio Compra": st.column_config.NumberColumn(format="$%.4f"),
            "Precio Venta": st.column_config.NumberColumn(format="$%.4f"),
            "Ganancia Neta": st.column_config.NumberColumn(format="$%.2f"),
            "ROI %": st.column_config.NumberColumn(format="%.3f%%"),
            "Volumen 24h": st.column_config.NumberColumn(format="$%d"),
            "Fee Red": st.column_config.NumberColumn(format="$%.2f")
        },
        hide_index=True,
        use_container_width=True
    )

def render_investment_section(pais, prods):
    st.write("Cargando catálogo retail...")
