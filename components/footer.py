import streamlit as st
import datetime

def render_legal_bunker(paypal_user):
    st.markdown(f'''
        <div style="background: #000; padding: 50px 20px; margin-top: 80px; font-size: 9px; color: #334155; text-align: justify; border-top: 1px solid #1e293b; line-height: 1.6;">
            <div style="max-width: 1100px; margin: 0 auto;">
                <strong>TÉRMINOS, CONDICIONES Y BLINDAJE LEGAL GLOBAL ({datetime.datetime.now().year}):</strong><br><br>
                1. <b>Programa de Afiliados:</b> TechFlash780 participa en el Programa de Afiliados de Amazon. Recibimos comisiones por compras calificadas sin costo extra para usted.<br>
                2. <b>Exención de Responsabilidad:</b> No somos asesores financieros. Las cifras de "Ganancia" y "ROI" son simulaciones basadas en datos volátiles. No garantizamos resultados comerciales.<br>
                3. <b>Jurisdicción:</b> El usuario es responsable de cumplir con las leyes de importación, impuestos y reventa de su país. Operamos bajo cláusulas de "Puerto Seguro" (Safe Harbor).<br>
                4. <b>Precios:</b> Los precios en Amazon.com y sus variantes prevalecen sobre cualquier dato mostrado en este nodo informático.<br><br>
                <center>© TechFlash780 Intelligence System. Todos los derechos reservados.</center>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    st.write("")
    st.link_button("☕ Apoyar Mantenimiento del Nodo (PayPal)", f"https://www.paypal.me/{paypal_user}", use_container_width=True)
 target_col.markdown(html_card, unsafe_allow_html=True)
