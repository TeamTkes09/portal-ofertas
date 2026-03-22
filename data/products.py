import streamlit as st
import requests
import pandas as pd
import random

# --- CONFIGURACIÓN DE REDES ---
NETWORK_FEES = {
    'BTC': {'red': 'Bitcoin', 'fee': 15.0},
    'ETH': {'red': 'ERC20', 'fee': 8.5},
    'SOL': {'red': 'Solana', 'fee': 0.01},
    'USDT': {'red': 'TRC20', 'fee': 1.0},
    'DEFAULT': {'red': 'BSC/BEP20', 'fee': 0.5}
}

@st.cache_data(ttl=60)
def get_crypto_opportunities():
    try:
        # Intentamos conectar con la API Real
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 200, "page": 1}
        response = requests.get(url, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            full_200 = []
            for coin in data:
                sym = coin['symbol'].upper()
                net = NETWORK_FEES.get(sym, NETWORK_FEES['DEFAULT'])
                price = coin['current_price']
                
                full_200.append({
                    "Rank": coin['market_cap_rank'],
                    "Token": sym,
                    "Precio Compra": price,
                    "Precio Venta": round(price * 1.002, 6), # Spread 0.2%
                    "Red": net['red'],
                    "Fee Red": net['fee'],
                    "Volumen 24h": coin['total_volume'],
                    "Cambio %": coin['price_change_percentage_24h']
                })
            return full_200
        else:
            # Si la API responde pero con error (ej. Rate Limit 429)
            return get_fallback_data()
    except Exception:
        # Si no hay internet o la API está caída
        return get_fallback_data()

def get_fallback_data():
    """Datos de respaldo para que la app siempre muestre algo"""
    return [
        {"Rank": 1, "Token": "BTC", "Precio Compra": 65000.0, "Precio Venta": 65150.0, "Red": "Bitcoin", "Fee Red": 15.0, "Volumen 24h": 30000000, "Cambio %": 0.5},
        {"Rank": 2, "Token": "ETH", "Precio Compra": 3500.0, "Precio Venta": 3515.0, "Red": "ERC20", "Fee Red": 8.5, "Volumen 24h": 15000000, "Cambio %": -0.2},
        {"Rank": 3, "Token": "SOL", "Precio Compra": 145.0, "Precio Venta": 146.5, "Red": "Solana", "Fee Red": 0.01, "Volumen 24h": 5000000, "Cambio %": 2.4}
    ]

@st.cache_data(ttl=15)
def get_optimized_routes():
    # Simulador de rutas de 2, 3 y 4 puntas
    # NOTA: Aquí restamos ya el 0.4% de comisiones (0.1% x 4 trades)
    return [
        {
            "id": "OPT-01", "tipo": "DIRECTO", "nodos": 2, 
            "ruta": "USDT → SOL → USDT", "exchanges": ["Binance", "Kraken"], 
            "roi_neto": 0.45, "riesgo": "BAJO", "descripcion": "Arbitraje simple."
        },
        {
            "id": "OPT-03", "tipo": "CUADRANGULAR", "nodos": 4, 
            "ruta": "USDT → BTC → ETH → SOL → USDT", "exchanges": ["Binance"], 
            "roi_neto": 0.52, "riesgo": "MÍNIMO", 
            "descripcion": "Ciclo interno. ROI ya descuenta el 0.4% de fees de trading."
        }
    ]

# --- 4. PRODUCTOS RETAIL (FBA) - COMPATIBILIDAD ---
def get_real_time_opportunities():
    """Mantiene la funcionalidad de productos físicos si el usuario la usa"""
    return [
        {"n": "Apple AirTag 4pk", "cat": "TECH", "c": 79.0, "v": 99.0, "q": "B08ZG76197", 
         "comparativa": [{"sitio": "ebay", "precio": 92.0}]},
        {"n": "Stanley Quencher 40oz", "cat": "HOGAR", "c": 35.0, "v": 85.0, "q": "B0C1M1YF9P", 
         "comparativa": [{"sitio": "ebay", "precio": 78.0}]}
    ]

def get_news_events():
    """Eventos de mercado"""
    return [
        {
            "titulo": "🔥 Alerta de Spread: BTC/KRW",
            "descripcion": "Diferencial de 2% detectado en exchanges coreanos (Kimchi Premium).",
            "fuente": "CryptoAlert", "hace": "2m", "impacto": "ALTO",
            "productos_asociados": []
        }
    ]
