# styles/html_templates.py

def get_card_template(op, roi, margen_neto, amz_url, filas_html):
    msg = f"Oferta: {op['n']} | ROI: {roi}%"
    wa_link = f"https://api.whatsapp.com/send?text={msg} - {amz_url}"
    tg_link = f"https://t.me/share/url?url={amz_url}&text={msg}"

    return f"""
    <div style="background: #1e293b; border-radius: 8px; padding: 12px; border: 1px solid #334155; font-family: 'Segoe UI', sans-serif; height: 410px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
        
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="background: #0f172a; color: #94a3b8; padding: 2px 6px; border-radius: 4px; font-size: 9px; font-weight: 700;">{op['cat']}</span>
                <div style="display: flex; gap: 6px;">
                    <a href="{wa_link}" target="_blank" style="text-decoration: none; font-size: 12px;">🟢</a>
                    <a href="{tg_link}" target="_blank" style="text-decoration: none; font-size: 12px;">🔵</a>
                </div>
            </div>

            <h4 style="color: white; margin: 0 0 10px 0; font-size: 13px; font-weight: 600; line-height: 1.2; height: 32px; overflow: hidden;">{op['n']}</h4>
            
            <div style="background: #0f172a; border-radius: 6px; padding: 8px; border: 1px solid #1e293b;">
                {filas_html}
            </div>
        </div>

        <div style="margin-top: 10px;">
            <div style="text-align: center; margin-bottom: 8px;">
                <div style="font-size: 26px; font-weight: 900; color: #22c55e; line-height: 1;">{roi}%</div>
                <div style="font-size: 10px; color: #94a3b8;">NETO: <b style="color: white;">${margen_neto}</b></div>
            </div>
            <a href="{amz_url}" target="_blank" style="text-decoration: none; background: #22c55e; color: white; text-align: center; padding: 10px; border-radius: 5px; font-weight: 800; font-size: 11px; display: block; text-transform: uppercase;">
                Ver en Amazon
            </a>
        </div>
    </div>
    """
