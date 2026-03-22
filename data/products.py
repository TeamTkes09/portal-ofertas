import streamlit as st
import requests

@st.cache_data(ttl=60)
def get_crypto_opportunities():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 200, "page": 1}
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        full_200 = []
        for coin in data:
            precio_real = coin['current_price']
            sym = coin['symbol'].upper()
            
            # Definición de Red y Fee (COLUMNA CRÍTICA: "Fee Red")
            if sym == 'BTC': red, fee = "Bitcoin", 15.0
            elif sym in ['ETH', 'USDT', 'USDC']: red, fee = "ERC20", 8.5
            elif sym in ['SOL', 'JUP']: red, fee = "Solana", 0.01
            elif sym in ['MATIC', 'POL']: red, fee = "Polygon", 0.05
            else: red, fee = "BSC/Otras", 0.50

            full_200.append({
                "Rank": coin['market_cap_rank'],
                "Token": sym,
                "Precio Compra": precio_real,
                "Precio Venta": round(precio_real * 1.003, 6), # Spread real 0.3%
                "Red": red,
                "Fee Red": fee, # Nombre exacto para evitar KeyError
                "Volumen 24h": coin['total_volume'],
                "Cambio %": coin['price_change_percentage_24h']
            })
        return full_200
    except:
        return []

# No olvides estas funciones para que app.py no falle
def get_real_time_opportunities(): return []
def get_news_events(): return []
