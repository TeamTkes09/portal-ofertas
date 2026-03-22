import streamlit as st
import pandas as pd
from data.products import get_all_products
from components.cards import render_investment_section

# 1. Configuración de página
st.set_page_config(page_title="Arbitraje Pro 2026", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS para optimizar espacio
st.markdown("""
    <style>
    .block-container { padding: 1rem 2rem; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Portal de Arbitraje 2026")

# 3. Carga y Filtro de Datos
productos = get_all_products()
cat_list = sorted(list(set([p['cat'] for p in productos])))
cat_sel = st.selectbox("Filtrar por Categoría", ["TODAS"] + cat_list)

productos_final = productos if cat_sel == "TODAS" else [p for p in productos if p['cat'] == cat_sel]

# 4. Selector de Vistas
tab1, tab2 = st.tabs(["🎴 Vista de Tarjetas", "📊 Vista de Tabla (Excel)"])

with tab1:
    # Renderiza tus tarjetas compactas de 215px
    render_investment_section(".com", productos_final)

with tab2:
    st.subheader("📊 Panel de Análisis y Exportación")
    
    # Preparamos los datos para el DataFrame
    datos_excel = []
    for p in productos_final:
        comp = {item['sitio'].lower(): item['precio'] for item in p.get('comparativa', [])}
        costo = p['c']
        venta = p['v']
        ganancia = venta - costo
        roi = (ganancia / costo) * 100 if costo > 0 else 0
        
        datos_excel.append({
            "SKU": p['id'],
            "Producto": p['n'],
            "Categoría": p['cat'],
            "Costo AMZ": costo,
            "eBay": comp.get('ebay', 0),
            "Google": comp.get('google', 0),
            "Shopify": comp.get('shopify', 0),
            "Venta Local": venta,
            "Ganancia $": ganancia,
            "ROI %": round(roi, 2),
            "Riesgo": p['r']
        })
    
    df = pd.DataFrame(datos_excel)
    
    # Botón de descarga en la parte superior para fácil acceso
    st.download_button(
        label="📥 Descargar Reporte para Excel (CSV)",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='analisis_arbitraje_2026.csv',
        mime='text/csv',
    )

    # Tabla interactiva avanzada
    st.dataframe(
        df, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "ROI %": st.column_config.ProgressColumn("ROI %", min_value=0, max_value=100, format="%d%%"),
            "Ganancia $": st.column_config.NumberColumn("Ganancia", format="$%d"),
            "Costo AMZ": st.column_config.NumberColumn("Costo", format="$%d"),
            "Venta Local": st.column_config.NumberColumn("P. Venta", format="$%d"),
            "Riesgo": st.column_config.SelectboxColumn("Nivel Riesgo", options=["BAJO", "MEDIO", "ALTO"])
        }
    )
    
    st.info("💡 Puedes ordenar los datos haciendo clic en el nombre de cualquier columna.")
