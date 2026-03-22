# components/table_view.py
import streamlit as st
import pandas as pd

def render_table_section(lista_productos):
    st.markdown("### 📊 Análisis de Activos (Vista Expandida)")
    
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
    
    # ACTUALIZADO: Cambiamos use_container_width por width='stretch'
    st.dataframe(
        df, 
        width='stretch', 
        hide_index=True,
        column_config={
            "ROI %": st.column_config.TextColumn("ROI %", help="Retorno de Inversión Estimado"),
            "Ganancia": st.column_config.TextColumn("Ganancia", help="Margen neto por unidad")
        }
    )
