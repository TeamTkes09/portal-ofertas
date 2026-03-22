import ccxt
import pandas as pd
import streamlit as st

@st.cache_data(ttl=10) # Aumentamos a 10s para evitar saturar la API
def get_binance_tickers():
    try:
        # Configuración con Timeout y Proxy-friendly
        ex = ccxt.binance({
            'timeout': 20000, # 20 segundos de espera
            'enableRateLimit': True,
            'options': {'defaultType': 'spot'}
        })
        
        # Intentar obtener solo los tickers necesarios para no saturar
        tickers = ex.fetch_tickers()
        
        if not tickers:
            return None

        data = []
        for symbol, t in tickers.items():
            if symbol.endswith('/USDT'):
                # Validamos que existan los datos básicos
                ask = t.get('ask') or t.get('last') or 0
                bid = t.get('bid') or t.get('last') or 0
                
                data.append({
                    "Token": symbol.split('/')[0],
                    "Precio Compra": ask,
                    "Precio Venta": bid,
                    "Spread %": round(((ask - bid) / ask * 100), 4) if ask > 0 else 0,
                    "Volumen 24h": round(t.get('quoteVolume', 0), 2),
                    "Cambio %": t.get('percentage', 0)
                })
        
        if not data:
            return None

        return pd.DataFrame(data).sort_values(by="Volumen 24h", ascending=False).head(50)

    except Exception as e:
        # Esto imprimirá el error real en tu consola de Streamlit
        st.sidebar.error(f"Detalle técnico: {str(e)}")
        return None
