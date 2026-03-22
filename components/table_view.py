# components/table_view.py
import streamlit as st
import pandas as pd

def render_table_section(lista_productos):
    st.markdown("### 📊 Análisis de Activos (Vista Expandida)")
    
    # Preparamos los datos para el DataFrame
    data_list = []
    for p in lista_productos:
        margen = p['v'] - p['c']
        roi = int((margen / p['c']) * 100)
        
        data_list.append({
            "ID": p['id'],
            "Producto": p['n'],
            "Categoría": p['cat'],
            "Costo AMZ": f"${p['c']}",
            "Venta Est.": f"${p['v']}",
            "Ganancia": f"${margen}",
            "ROI %": f"{roi}%",
            "Riesgo": p['r']
        })
    
    df = pd.DataFrame(data_list)
    
    # Renderizado de tabla interactiva
    st.dataframe(
        df, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "ROI %": st.column_config.TextColumn("ROI %", help="Retorno de Inversión Estimado"),
            "Ganancia": st.column_config.TextColumn("Ganancia", help="Margen neto por unidad")
        }
    )
    st.caption("💡 Tip: Haz clic en las cabeceras para ordenar por ROI o Ganancia.")
