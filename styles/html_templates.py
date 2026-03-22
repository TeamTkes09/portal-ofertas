# styles/html_templates.py

def get_card_template(op, roi, margen_neto, amz_url, filas_html):
    """
    Genera el HTML de la tarjeta con botones de compartir y comparativa extendida.
    """
    # Configuración de mensaje para compartir
    msg = f"Oportunidad de Arbitraje: {op['n']} | ROI: {roi}% | Ganancia: ${margen_neto}"
    wa_link = f"https://api.whatsapp.com/send?text={msg} - Ver más: {amz_url}"
    tg_link = f"https://t.me/share/url?url={amz_url}&text={msg}"

    return f"""
    <div style="background: #1e293b; border-radius: 12px; padding: 18px; border: 1px solid #334155; font-family: sans-serif; height: 520px; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span style="background: #334155; color: #94a3b8; padding: 4px 10px; border-radius: 6px; font-size: 10px; font-weight: bold; text-transform: uppercase;">{op['cat']}</span>
                <div style="display: flex; gap: 10px;">
                    <a href="{wa_link}" target="_blank" title="Compartir en WhatsApp" style="text-decoration: none;">
                        <div style="background: #22c55e; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">W</div>
                    </a>
                    <a href="{tg_link}" target="_blank" title="Compartir en Telegram" style="text-decoration: none;">
                        <div style="background: #3b82f6; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">T</div>
                    </a>
                </div>
            </div>

            <h4 style="color: white; margin: 0 0 15px 0; font-size: 16px; font-weight: 600; line-height: 1.3; height: 42px; overflow: hidden;">{op['n']}</h4>
            
            <div style="background: #0f172a; border-radius: 10px; padding: 12px; border: 1px solid #1e293b;">
                <div style="color: #22c55e; font-size: 9px; font-weight: 800; margin-bottom: 8px; letter-spacing: 1px; text-transform: uppercase;">Ecosistema de Precios:</div>
                {filas_html}
            </div>
        </div>

        <div>
            <div style="text-align: center; padding: 15px 0; border-top: 1px solid #334155;">
                <div style="font-size: 36px; font-weight: 900; color: #22c55e; letter-spacing: -1px;">
                    {roi}% <small style="font-size: 14px; color: #94a3b8; font-weight: 400;">ROI</small>
                </div>
                <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">Ganancia Neta: <b style="color: white;">${margen_neto}</b></div>
            </div>

            <div style="margin-top: 10px;">
                <div style="font-size: 10px; color: {op['clr']}; text-align: center; margin-bottom: 8px; font-weight: 800; letter-spacing: 1px;">RIESGO {op['r']}</div>
                <a href="{amz_url}" target="_blank" style="text-decoration: none; background: #22c55e; color: white; text-align: center; padding: 14px; border-radius: 8px; font-weight: 800; font-size: 14px; display: block; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
                    🛒 VER EN AMAZON
                </a>
            </div>
        </div>
    </div>
    """
