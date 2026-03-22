# styles/html_templates.py

def get_card_template(op, roi, margen_neto, amz_url, filas_html):
    msg = f"ROI: {roi}% | {op['n']}"
    wa_link = f"https://api.whatsapp.com/send?text={msg} - {amz_url}"
    
    return f"""
    <div style="background: #1e293b; border-radius: 6px; padding: 8px; border: 1px solid #334155; font-family: sans-serif; height: 210px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box; ovelow: hidden;">
        
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="width: 80%;">
                <span style="color: #94a3b8; font-size: 8px; font-weight: 700; text-transform: uppercase;">{op['cat']}</span>
                <h4 style="color: white; margin: 2px 0; font-size: 11px; height: 28px; overflow: hidden; line-height: 1.1;">{op['n']}</h4>
            </div>
            <a href="{wa_link}" target="_blank" style="text-decoration:none; font-size: 14px;">🟢</a>
        </div>

        <div style="background: #0f172a; border-radius: 4px; padding: 4px; margin: 4px 0;">
            {filas_html}
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #334155; padding-top: 4px;">
            <div>
                <span style="font-size: 18px; font-weight: 800; color: #22c55e;">{roi}%</span>
                <span style="font-size: 9px; color: #94a3b8; margin-left: 4px;">${margen_neto}</span>
            </div>
            <a href="{amz_url}" target="_blank" style="text-decoration: none; background: #22c55e; color: white; padding: 4px 8px; border-radius: 3px; font-size: 9px; font-weight: bold;">AMZ ↗</a>
        </div>
    </div>
    """
