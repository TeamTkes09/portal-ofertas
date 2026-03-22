# styles/html_templates.py

def get_card_template(op, roi, margen_neto, amz_url, filas_html):
    """
    Genera el bloque HTML puro para la tarjeta de producto.
    IMPORTANTE: No debe contener código de Streamlit, solo un string de HTML.
    """
    # Usamos f-string con comillas triples para mantener el formato
    return f"""
    <div style="background: #1e293b; border-radius: 12px; padding: 20px; margin-bottom: 20px; border: 1px solid #334155; min-height: 480px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
        
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span style="background: #334155; color: #94a3b8; padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; letter-spacing: 0.5px;">{op['cat']}</span>
                <span style="color: #64748b; font-size: 10px; font-weight: bold;">ID: {op['id']}</span>
            </div>

            <h4 style="color: white; margin-bottom: 15px; font-size: 16px; line-height: 1.4; font-weight: 600; height: 45px; overflow: hidden;">{op['n']}</h4>
            
            <div style="background: #0f172a; border-radius: 8px; padding: 12px; margin-bottom: 15px; border: 1px solid #1e293b;">
                <div style="color: #22c55e; font-size: 9px; font-weight: 800; margin-bottom: 8px; letter-spacing: 1px; text-transform: uppercase;">Validación de Mercado:</div>
                {filas_html}
            </div>
        </div>

        <div>
            <div style="text-align: center; padding: 15px 0; border-top: 1px solid #334155;">
                <div style="font-size: 38px; font-weight: 900; color: #22c55e; letter-spacing: -1.5px;">
                    {roi}% <small style="font-size: 14px; color: #94a3b8;">ROI</small>
                </div>
                <div style="font-size: 13px; color: #94a3b8; margin-top: 5px;">
                    Ganancia neta: <b style="color: white;">${margen_neto}</b>
                </div>
            </div>

            <div style="margin-top: 15px;">
                <div style="font-size: 10px; color: {op['clr']}; text-align: center; margin-bottom: 8px; font-weight: bold; letter-spacing: 1px;">RIESGO {op['r']}</div>
                <a href="{amz_url}" target="_blank" style="text-decoration: none; background: #22c55e; color: white; text-align: center; padding: 14px; border-radius: 8px; font-weight: 800; font-size: 14px; display: block; transition: all 0.2s ease; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                    🛒 COMPRAR EN AMAZON
                </a>
            </div>
        </div>
    </div>
    """
