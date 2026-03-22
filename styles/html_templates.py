def get_card_template(op, roi, margen_neto, amz_url, filas_html):
    return f"""
    <div style="background: #1e293b; border-radius: 6px; padding: 10px; border: 1px solid #334155; font-family: sans-serif; height: 215px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box; color: white;">
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="color: #94a3b8; font-size: 8px; font-weight: 800; text-transform: uppercase;">{op['cat']}</span>
            </div>
            <h4 style="color: white; margin: 0 0 6px 0; font-size: 11px; height: 24px; overflow: hidden; line-height: 1.2;">{op['n']}</h4>
            <div style="background: #0f172a; border-radius: 4px; padding: 5px 8px; border: 1px solid #1e293b;">
                {filas_html}
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #334155; padding-top: 6px; margin-top: 4px;">
            <div>
                <span style="font-size: 18px; font-weight: 900; color: #22c55e;">{roi}%</span>
                <span style="font-size: 9px; color: #94a3b8; margin-left: 4px;">${margen_neto}</span>
            </div>
            <a href="{amz_url}" target="_blank" style="text-decoration: none; background: #22c55e; color: white; padding: 4px 10px; border-radius: 4px; font-weight: 800; font-size: 10px;">AMZ ↗</a>
        </div>
    </div>
    """
