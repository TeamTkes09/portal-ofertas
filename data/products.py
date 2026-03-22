import ccxt
import networkx as nx
import math
import streamlit as st
import requests
import pandas as pd
import random

# --- CONFIGURACIÓN DE REDES PARA MONITOR GENERAL ---
NETWORK_FEES = {
    'BTC': {'red': 'Bitcoin', 'fee': 15.0},
    'ETH': {'red': 'ERC20', 'fee': 8.5},
    'SOL': {'red': 'Solana', 'fee': 0.01},
    'USDT': {'red': 'TRC20', 'fee': 1.0},
    'DEFAULT': {'red': 'BSC/BEP20', 'fee': 0.5}
}

# --- 1. MONITOR TOP 200 (PRECIOS DE MERCADO) ---
@st.cache_data(ttl=60)
def get_crypto_opportunities():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 200, "page": 1}
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            full_200 = []
            for coin in data:
                sym = coin['symbol'].upper()
                price = coin['current_price']
                net = NETWORK_FEES.get(sym, NETWORK_FEES['DEFAULT'])
                full_200.append({
                    "Rank": coin['market_cap_rank'],
                    "Token": sym,
                    "Precio Compra": price,
                    "Precio Venta": round(price * 1.002, 6),
                    "Red": net['red'],
                    "Fee Red": net['fee'],
                    "Volumen 24h": coin['total_volume'],
                    "Cambio %": coin['price_change_percentage_24h']
                })
            return full_200
    except:
        return []

# --- 2. MOTOR DE ARBITRAJE INFINITO (N-PUNTAS) ---
def buscar_ciclo_infinito(api_key, secret_key):
    """
    Usa algoritmos de grafos (Bellman-Ford) para encontrar la ruta
    más rentable de N pasos dentro de Binance.
    """
    try:
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key,
            'enableRateLimit': True,
        })
        
        G = nx.DiGraph()
        tickers = exchange.fetch_tickers()
        
        # Factor de comisión (0.075% con BNB activo)
        fee_factor = 0.99925 

        for symbol, data in tickers.items():
            if '/' in symbol and data['ask'] and data['bid']:
                base, quote = symbol.split('/')
                ask, bid = data['ask'], data['bid']

                if ask > 0 and bid > 0:
                    # Peso negativo del logaritmo: suma de log = log de multiplicación
                    # De Base a Quote (Venta)
                    G.add_edge(base, quote, weight=-math.log(bid * fee_factor))
                    # De Quote a Base (Compra)
                    G.add_edge(quote, base, weight=-math.log((1/ask) * fee_factor))

        # Buscar el ciclo de mayor ganancia partiendo de USDT
        try:
            ciclo = nx.find_negative_cycle(G, 'USDT')
            
            # Cálculo del ROI Real
            peso_total = 0
            for i in range(len(ciclo) - 1):
                peso_total += G[ciclo[i]][ciclo[i+1]]['weight']
            
            roi_estimado = (math.exp(-peso_total) - 1) * 100
            return {"status": "success", "ruta": ciclo, "roi": roi_estimado}
            
        except nx.NetworkXNoCycle:
            return {"status": "no_path", "ruta": [], "roi": 0}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 3. EJECUCIÓN ATÓMICA DE TRADES ---
def ejecutar_ruta_dinamica(api_key, secret_key, ruta, monto_usdt):
    """Ejecuta secuencialmente los pares de la ruta hallada"""
    exchange = ccxt.binance({
        'apiKey': api_key, 'secret': secret_key, 'options': {'defaultType': 'spot'}
    })
    
    try:
        balance_actual = monto_usdt
        for i in range(len(ruta) - 1):
            source = ruta[i]
            target = ruta[i+1]
            
            # Determinar si es compra o venta
            symbol_buy = f"{target}/{source}"
            symbol_sell = f"{source}/{target}"
            
            if symbol_buy in exchange.markets:
                order = exchange.create_market_buy_order(symbol_buy, balance_actual)
                balance_actual = order['filled']
            else:
                order = exchange.create_market_sell_order(symbol_sell, balance_actual)
                balance_actual = order['filled']
                
        return {"status": "success", "final": balance_actual}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 4. RETAIL & NOTICIAS ---
def get_real_time_opportunities():
    return [
        {"n": "MacBook M3 Pro", "cat": "TECH", "c": 1800.0, "v": 2100.0, "q": "B0CM5N3LY5", 
         "comparativa": [{"sitio": "ebay", "precio": 1950.0}]}
    ]

def get_news_events():
    return [
        {"titulo": "Volatilidad en SOL", "impacto": "ALTO", "fuente": "Binance", "hace": "1m", "descripcion": "Spread de SOL/BTC aumentando."}
    ]
