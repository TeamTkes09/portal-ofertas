import streamlit as st
import pandas as pd

def render_crypto_section(lista_crypto):
    if not lista_crypto:
        st.error("🚨 Error de conexión con los Exchanges. Reintentando...")
        return

    st.subheader("🏦 Monitor de Arbitraje en Tiempo Real (Top 200)")
    
    df = pd.DataFrame(lista_crypto)
    
    # Cálculos críticos de valor
    df['Spread USD'] = df['Precio Venta'] - df['Precio Compra']
    df['Ganancia Neta'] = df['Spread USD'] - df['Fee Red']
    df['ROI %'] = (df['Ganancia Neta'] / df['Precio Compra']) * 100

    # Controles de usuario
    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("🔍 Filtrar por Token (BTC, SOL, MATIC...)").upper()
    with col2:
        min_roi = st.number_input("ROI Mínimo %", value=0.0, step=0.1)

    if search:
        df = df[df['Token'].str.contains(search)]
    
    # Filtro de oportunidad real
    df_oportunidades = df[df['ROI %'] >= min_roi].sort_values(by="ROI %", ascending=False)

    st.dataframe(
        df_oportunidades,
        column_config={
            "Precio Compra": st.column_config.NumberColumn(format="$%.4f"),
            "Precio Venta": st.column_config.NumberColumn(format="$%.4f"),
            "Ganancia Neta": st.column_config.NumberColumn(format="$%.2f"),
            "ROI %": st.column_config.NumberColumn(format="%.3f%%"),
            "Volumen 24h": st.column_config.NumberColumn(format="$%d"),
            "Cambio %": st.column_config.NumberColumn(format="%.2f%%")
        },
        hide_index=True,
        use_container_width=True
    )

def render_investment_section(pais, prods):
    st.write("Sección de productos físicos (FBA)")
