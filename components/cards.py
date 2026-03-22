import streamlit as st
import pandas as pd

def render_crypto_section(lista_crypto):
    if not lista_crypto:
        st.warning("Esperando respuesta de los exchanges...")
        return

    st.markdown("### 🏦 Terminal de Arbitraje en Tiempo Real (Top 200)")
    
    # Convertimos a DataFrame para cálculos masivos
    df = pd.DataFrame(lista_crypto)
    
    # Cálculo de rentabilidad real
    df['Spread Bruto'] = df['Precio Venta'] - df['Precio Compra']
    df['Ganancia Neta'] = df['Spread Bruto'] - df['Fee Red']
    df['ROI %'] = (df['Ganancia Neta'] / df['Precio Compra']) * 100

    # Buscador y filtros
    col_a, col_b = st.columns([2, 1])
    search = col_a.text_input("🔍 Buscar moneda...").upper()
    min_roi = col_b.slider("ROI Mínimo %", -1.0, 5.0, 0.1)

    if search:
        df = df[df['Token'].str.contains(search)]
    
    df = df[df['ROI %'] >= min_roi]

    # Visualización Profesional
    st.dataframe(
        df.sort_values(by="ROI %", ascending=False),
        column_config={
            "Precio Compra": st.column_config.NumberColumn(format="$%.4f"),
            "Precio Venta": st.column_config.NumberColumn(format="$%.4f"),
            "Ganancia Neta": st.column_config.NumberColumn(format="$%.2f"),
            "ROI %": st.column_config.NumberColumn(format="%.3f%%"),
            "Vol 24h": "Volumen 24h",
            "Cambio 24h": st.column_config.TextColumn("Tendencia")
        },
        hide_index=True,
        use_container_width=True
    )
    
    st.caption("🔄 Los precios se sincronizan automáticamente cada 60 segundos con CoinGecko API.")
