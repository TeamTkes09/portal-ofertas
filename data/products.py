import streamlit as st
import requests
import pandas as pd

@st.cache_data(ttl=60)
def get_crypto_opportunities():
    try:
        # API Real: Top 200 monedas por Market Cap
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 200,
            "page": 1,
            "sparkline": False
        }
        # Timeout de 10 segundos para no bloquear la web
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        full_200 = []
        for coin in data:
            precio_real = coin['current_price']
            # El "Spread" en arbitraje real suele ser de céntimos en el Top 10, 
            # pero mayor en monedas pequeñas (Rank 100-200).
            spread_market = 1.0025 # 0.25% de diferencia promedio entre exchanges
            
            # Lógica de Redes Reales
            sym = coin['symbol'].upper()
            if sym == 'BTC': red, fee = "Bitcoin", 15.0
            elif sym in ['ETH', 'USDT', 'USDC', 'LINK', 'SHIB']: red, fee = "ERC20", 8.0
            elif sym in ['SOL', 'JUP', 'PYTH', 'BONK']: red, fee = "Solana", 0.01
            elif sym in ['MATIC', 'QUICK']: red, fee = "Polygon", 0.05
            elif sym in ['AVAX', 'JOE']: red, fee = "Avalanche", 0.10
            else: red, fee = "Red Propia/BSC", 0.50

            full_200.append({
                "Rank": coin['market_cap_rank'],
                "Token": sym,
                "Nombre": coin['name'],
                "Precio Compra": precio_real,
                "Precio Venta": round(precio_real * spread_market, 6),
                "Red": red,
                "Fee Red": fee,
                "Volumen 24h": coin['total_volume'],
                "Cambio %": coin['price_change_percentage_24h']
            })
        return full_200
    except Exception as e:
        # Si falla la API, devolvemos una lista vacía para no romper app.py
        return []

# Mantener las otras funciones para no romper los otros tabs
def get_real_time_opportunities():
    return [] # Aquí puedes pegar tu lógica de productos anterior

def get_news_events():
    return [] # Aquí puedes pegar tu lógica de noticias anterior
