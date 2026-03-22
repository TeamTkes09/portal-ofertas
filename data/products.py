import streamlit as st
import requests
import pandas as pd

@st.cache_data(ttl=30)
def get_crypto_opportunities():
    try:
        # Consultamos el Top 200 de CoinGecko (API Gratuita)
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 200,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(url, params=params)
        data = response.json()

        full_200 = []
        for coin in data:
            # Lógica de spreads reales: Simulamos un diferencial de mercado (0.1% - 0.5%)
            # En un entorno de producción, aquí conectarías con WebSockets de Binance/Kraken
            precio_actual = coin['current_price']
            spread_simulado = 1.002 # Diferencial típico del 0.2% entre exchanges top
            
            # Asignación de red lógica según el activo
            red = "Propia"
            fee = 1.0
            if coin['symbol'].upper() in ['ETH', 'USDT', 'USDC']: 
                red, fee = "ERC20", 8.0
            elif coin['symbol'].upper() == 'BTC': 
                red, fee = "Bitcoin", 15.0
            elif coin['symbol'].upper() in ['SOL', 'PYTH', 'JUP']: 
                red, fee = "Solana", 0.01

            full_200.append({
                "Rank": coin['market_cap_rank'],
                "Token": coin['symbol'].upper(),
                "Precio Compra": precio_actual,
                "Precio Venta": round(precio_actual * spread_simulado, 6),
                "Red": red,
                "Fee Red": fee,
                "Vol 24h": f"${coin['total_volume']:,}",
                "Cambio 24h": f"{coin['price_change_percentage_24h']:.2f}%"
            })
        return full_200
    except Exception as e:
        st.error(f"Error conectando con el mercado: {e}")
        return []
