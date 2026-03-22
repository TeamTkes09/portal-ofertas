import streamlit as st
import pandas as pd

def render_data_table(oportunidades, suffix):
    st.markdown("### 📊 Panel Analítico Pro (Vista de Tabla)")
    st.caption("Haz clic en los encabezados para ordenar por ROI, Categoría o Precio.")

    # 1. Preparar los datos para Pandas
    data = []
    for op in oportunidades:
        margen = op['v'] - op['c']
        roi = int((margen/op['c'])*100)
        
        data.append({
            "ID": f"TF-{op['id']}",
            "Producto": op['n'],
            "Categoría": op['cat'],
            "Costo ($)": op['c'],
            "Venta Est. ($)": op['v'],
            "Margen ($)": margen,
            "ROI (%)": roi,
            "Riesgo": op['r']
        })

    df = pd.DataFrame(data)

    # 2. Configuración de la tabla interactiva
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "ROI (%)": st.column_config.ProgressColumn(
                "ROI (%)",
                help="Retorno sobre la inversión proyectado",
                format="%d%%",
                min_value=0,
                max_value=150,
            ),
            "Riesgo": st.column_config.SelectboxColumn(
                "Riesgo",
                options=["BAJO", "MEDIO", "ALTO"],
            ),
            "ID": st.column_config.TextColumn("Ref ID"),
        }
    )
