import ccxt
import pandas as pd
import streamlit as st

@st.cache_data(ttl=10)
def get_binance_tickers():
    try:
        ex = ccxt.binance({
            'timeout': 15000, 
            'enableRateLimit': True
        })
        
        # 1. Obtenemos TODOS los tickers (Binance envía esto en un solo paquete JSON)
        tickers = ex.fetch_tickers()
        
        data = []
        for symbol, t in tickers.items():
            # Filtramos solo pares contra USDT y que tengan datos válidos
            if symbol.endswith('/USDT') and t.get('ask') and t.get('bid'):
                data.append({
                    "Token": symbol.split('/')[0],
                    "Precio Compra": t['ask'],
                    "Precio Venta": t['bid'],
                    "Spread %": round(((t['ask'] - t['bid']) / t['ask'] * 100), 4),
                    "Volumen 24h": t.get('quoteVolume', 0),
                    "Cambio %": t.get('percentage', 0)
                })
        
        # 2. Convertimos a DataFrame y tomamos los TOP 500 por Volumen
        df = pd.DataFrame(data)
        if not df.empty:
            df = df.sort_values(by="Volumen 24h", ascending=False).head(500)
            return df
        return None

    except Exception as e:
        st.error(f"Error de conexión: {e}")
        return None
