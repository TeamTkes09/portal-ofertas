import streamlit as st
import pandas as pd

def render_crypto_section(lista_crypto):
    """Renderiza el monitor principal de 200 criptos con datos reales"""
    if not lista_crypto:
        st.error("⚠️ Error al conectar con los mercados. Reintentando...")
        return

    st.subheader("🏦 Monitor Global de Arbitraje (Top 200)")
    
    df = pd.DataFrame(lista_crypto)
    
    # Cálculos de rentabilidad de "Ida"
    df['Spread USD'] = df['Precio Venta'] - df['Precio Compra']
    df['Ganancia Neta'] = df['Spread USD'] - df['Fee Red']
    df['ROI %'] = (df['Ganancia Neta'] / df['Precio Compra']) * 100

    # Filtros rápidos
    c1, c2 = st.columns([2, 1])
    search = c1.text_input("🔍 Buscar Token...").upper()
    min_roi = c2.slider("Filtrar ROI Mínimo %", -0.5, 2.0, 0.1)

    if search:
        df = df[df['Token'].str.contains(search)]
    
    df_filtered = df[df['ROI %'] >= min_roi].sort_values(by="ROI %", ascending=False)

    st.dataframe(
        df_filtered,
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

def render_optimized_selector(rutas_optimizadas):
    """Renderiza el selector inteligente de 2, 3 y 4 puntas"""
    st.markdown("---")
    st.header("🎯 Selector de Rutas de Alto Rendimiento")
    st.caption("Optimiza la cantidad de exchanges según la rentabilidad esperada.")

    # Slider para que el usuario decida complejidad
    max_nodos = st.select_slider(
        "¿Cuántos saltos (exchanges/pasos) estás dispuesto a realizar?",
        options=[2, 3, 4],
        value=2,
        help="2: Rápido | 3: Triangulación | 4: Loop Cerrado (Mismo Exchange)"
    )

    # Filtrar rutas por la elección del usuario
    rutas_visibles = [r for r in rutas_optimizadas if r['nodos'] <= max_nodos]

    # Mostrar como tarjetas informativas
    cols = st.columns(len(rutas_visibles) if rutas_visibles else 1)
    
    for i, ruta in enumerate(rutas_visibles):
        with cols[i]:
            # Color dinámico por ROI
            color = "#4ade80" if ruta['roi_neto'] > 1.0 else "#60a5fa"
            
            st.markdown(f"""
                <div style="border: 1px solid {color}; padding: 15px; border-radius: 10px; background-color: #0f172a;">
                    <small style="color:{color}; font-weight:bold;">{ruta['tipo']}</small>
                    <h3 style="margin:5px 0; font-size:18px;">{ruta['ruta']}</h3>
                    <p style="font-size:24px; color:{color}; margin:0;">{ruta['roi_neto']}% ROI</p>
                    <hr style="margin:10px 0; opacity:0.2;">
                    <small style="color:#94a3b8;">Exchanges: {', '.join(ruta['exchanges'])}</small><br>
                    <small style="color:#94a3b8;">Riesgo: {ruta['riesgo']}</small>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Ver Pasos {ruta['id']}", use_container_width=True):
                st.info(f"📋 **Instrucciones:** {ruta['descripcion']}")

def render_investment_section(suffix, lista_productos):
    """Renderiza la sección de FBA (Retail Arbitrage)"""
    if not lista_productos:
        st.info("No hay ofertas retail activas en este momento.")
        return
        
    cols = st.columns(3)
    for i, p in enumerate(lista_productos):
        with cols[i % 3]:
            st.markdown(f"""
                <div style="background:#1e293b; padding:10px; border-radius:10px;">
                    <b>{p['n']}</b><br>
                    <span style="color:#4ade80;">Compra: ${p['c']}</span> | 
                    <span style="color:#60a5fa;">Venta: ${p['v']}</span>
                </div>
            """, unsafe_allow_html=True)
