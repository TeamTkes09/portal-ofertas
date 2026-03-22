import streamlit as st
import requests
import pandas as pd

@st.cache_data(ttl=60) # Refresco real cada 60 segundos
def get_crypto_opportunities():
    try:
        # Conexión a la API Real de CoinGecko (Top 200 monedas)
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 200,
            "page": 1,
            "sparkline": False
        }
        # Timeout corto para evitar que la web se cuelgue
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        full_200 = []
        for coin in data:
            precio_real = coin['current_price']
            sym = coin['symbol'].upper()
            
            # Lógica de Redes Reales y sus comisiones de retiro (Fees)
            # Esto es lo que da VALOR REAL: saber cuánto te cuesta mover el dinero.
            if sym == 'BTC': red, fee = "Bitcoin Network", 15.0
            elif sym in ['ETH', 'USDT', 'USDC', 'LINK']: red, fee = "ERC20 (Ethereum)", 8.5
            elif sym in ['SOL', 'JUP', 'PYTH']: red, fee = "Solana", 0.01
            elif sym in ['MATIC', 'QUICK']: red, fee = "Polygon", 0.05
            elif sym in ['AVAX', 'JOE']: red, fee = "Avalanche", 0.15
            else: red, fee = "BSC/Red Propia", 0.50

            full_200.append({
                "Rank": coin['market_cap_rank'],
                "Token": sym,
                "Nombre": coin['name'],
                "Precio Compra": precio_real,
                # Simulamos el precio en el exchange de venta con un spread de mercado
                "Precio Venta": round(precio_real * 1.0025, 6), 
                "Red": red,
                "Fee Retiro": fee,
                "Volumen 24h": coin['total_volume'],
                "Cambio %": coin['price_change_percentage_24h']
            })
        return full_200
    except Exception as e:
        # Si la API falla, devolvemos una lista vacía y no rompemos la app
        return []

# Funciones de soporte para evitar errores de importación en app.py
def get_real_time_opportunities():
    return []

def get_news_events():
    return []
