import ccxt
import pandas as pd
import streamlit as st

@st.cache_data(ttl=5)
def get_binance_tickers():
    try:
        # Usamos una conexión limpia
        ex = ccxt.binance({'enableRateLimit': True})
        tickers = ex.fetch_tickers()
        
        data = []
        for symbol, t in tickers.items():
            if symbol.endswith('/USDT'):
                token = symbol.split('/')[0]
                ask = t.get('ask', 0)
                bid = t.get('bid', 0)
                # Calculamos el spread real
                spread = ((ask - bid) / ask * 100) if ask > 0 else 0
                
                data.append({
                    "Token": token,
                    "Precio Compra": ask,
                    "Precio Venta": bid,
                    "Spread %": round(spread, 4),
                    "Volumen 24h": round(t.get('quoteVolume', 0), 2),
                    "Cambio %": t.get('percentage', 0)
                })
        
        # Ordenamos por volumen para ver lo más importante
        return pd.DataFrame(data).sort_values(by="Volumen 24h", ascending=False).head(50)
    except Exception as e:
        return None
