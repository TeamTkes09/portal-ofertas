import streamlit as st
import pandas as pd # <-- Importante añadir esto
from data.products import get_all_products
from components.cards import render_investment_section

st.set_page_config(page_title="Arbitraje Pro 2026", layout="wide")

# CSS para limpieza visual
st.markdown("""<style>.block-container { padding: 1rem 2rem; }</style>""", unsafe_allow_html=True)

st.title("🚀 Portal de Arbitraje 2026")

# Carga de datos
productos = get_all_products()

# Filtros en la barra lateral o superior
cat_list = sorted(list(set([p['cat'] for p in productos])))
cat_sel = st.selectbox("Filtrar Categoría", ["TODAS"] + cat_list)

productos_final = productos if cat_sel == "TODAS" else [p for p in productos if p['cat'] == cat_sel]

# --- NUEVA SECCIÓN: SELECTOR DE VISTA ---
tab1, tab2 = st.tabs(["🎴 Vista de Tarjetas", "📊 Vista de Tabla (Excel)"])

with tab1:
    render_investment_section(".com", productos_final)

with tab2:
    st.subheader("Análisis Comparativo de Datos")
    
    # Transformamos los datos para que se vean bien en una tabla
    data_tabla = []
    for p in productos_final:
        # Extraemos precios de la comparativa
        comp = {item['sitio'].lower(): item['precio'] for item in p.get('comparativa', [])}
        costo = p['c']
        venta = p['v']
        margen = venta - costo
        roi = f"{(margen/costo)*100:.1f}%" if costo > 0 else "0%"
        
        data_tabla.append({
            "ID": p['id'],
            "Producto": p['n'],
            "Categoría": p['cat'],
            "Costo (AMZ)": costo,
            "eBay": comp.get('ebay', 0),
            "Google": comp.get('google', 0),
            "Shopify": comp.get('shopify', 0),
            "Venta (Local)": venta,
            "Margen $": margen,
            "ROI": roi,
            "Riesgo": p['r']
        })
    
    df = pd.DataFrame(data_tabla)
    
    # Mostramos la tabla interactiva
    # Streamlit permite descargar esto a CSV/Excel automáticamente al pasar el mouse por la esquina superior derecha de la tabla
    st.dataframe(
        df, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "ROI": st.column_config.TextColumn("ROI %", help="Retorno de inversión calculado"),
            "Margen $": st.column_config.NumberColumn("Ganancia", format="$%d")
        }
    )
    
    st.info("💡 Tip: Puedes hacer clic en las cabeceras para ordenar o usar el botón de descarga en la esquina superior derecha de la tabla.")
