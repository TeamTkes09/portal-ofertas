import streamlit as st

def render_hero(pais_nombre):
    # --- BARRA SUPERIOR PROFESIONAL (Sustituye al texto feo) ---
    st.markdown(f'''
        <div style="
            display: flex; 
            justify-content: space-between; 
            padding: 5px 20px; 
            background: #0f172a; 
            border-bottom: 1px solid #1e293b;
            margin: -50px -50px 20px -50px;
        ">
            <span style="font-size: 10px; color: #64748b; font-weight: 600; letter-spacing: 1px;">
                TRADING NODE: {pais_nombre.upper()}
            </span>
            <span style="font-size: 10px; color: #475569; font-style: italic;">
                Contenido Patrocinado & Inteligencia de Mercado © TechFlash780
            </span>
        </div>
    ''', unsafe_allow_html=True)
    
    # --- BANNER PRINCIPAL ---
    st.markdown(f'''
        <div style="
            background: linear-gradient(135deg, #1e3a8a 0%, #020617 100%); 
            padding: 40px; 
            border-radius: 20px; 
            text-align: center; 
            margin-bottom: 25px; 
            border: 1px solid #1e40af;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        ">
            <h1 style="font-size: 3rem; font-weight: 900; margin:0; color: white; letter-spacing: -1px;">
                TECHFLASH <span style="color:#3b82f6;">PRO</span>
            </h1>
            <p style="color: #94a3b8; font-size: 1rem; margin-top: 10px; font-weight: 400;">
                Plataforma de Arbitraje y Análisis de Hardware
            </p>
        </div>
    ''', unsafe_allow_html=True)
