import ccxt
import networkx as nx
import math
import streamlit as st
import requests
import pandas as pd

# --- CONFIGURACIÓN ---
NETWORK_FEES = {
    'BTC': {'red': 'Bitcoin', 'fee': 15.0},
    'ETH': {'red': 'ERC20', 'fee': 8.5},
    'SOL': {'red': 'Solana', 'fee': 0.01},
    'USDT': {'red': 'TRC20', 'fee': 1.0},
    'DEFAULT': {'red': 'BSC/BEP20', 'fee': 0.5}
}

# --- 1. MONITOR DE SPREADS (BINANCE-FIRST) ---
@st.cache_data(ttl=5)
def get_crypto_opportunities(api_key=None, secret_key=None):
    try:
        # Intentar conexión con Binance
        exchange = ccxt.binance({
            'apiKey': api_key if api_key else '',
            'secret': secret_key if secret_key else '',
            'enableRateLimit': True
        })
        
        tickers = exchange.fetch_tickers()
        binance_data = []
        
        for symbol, t in tickers.items():
            if symbol.endswith('/USDT'):
                token = symbol.split('/')[0]
                ask = t.get('ask', 0) if t.get('ask') else 0
                bid = t.get('bid', 0) if t.get('bid') else 0
                spread_pct = ((ask - bid) / ask * 100) if ask > 0 else 0
                
                binance_data.append({
                    "Token": token,
                    "Precio Compra (Ask)": ask,
                    "Precio Venta (Bid)": bid,
                    "Spread %": round(spread_pct, 4),
                    "Volumen 24h": t.get('quoteVolume', 0),
                    "Cambio 24h %": t.get('percentage', 0),
                    "Fuente": "Binance Live"
                })
        
        if not binance_data:
            return get_coingecko_fallback()
            
        return binance_data

    except Exception:
        return get_coingecko_fallback()

def get_coingecko_fallback():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 50, "page": 1}
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            fallback_list = []
            for c in data:
                fallback_list.append({
                    "Token": c['symbol'].upper(), 
                    "Precio Compra (Ask)": c['current_price'], 
                    "Precio Venta (Bid)": c['current_price'],
                    "Spread %": 0.0,
                    "Volumen 24h": c['total_volume'],
                    "Cambio 24h %": c['price_change_percentage_24h'],
                    "Fuente": "CoinGecko Fallback"
                })
            return fallback_list
    except Exception:
        return []
    return []

# --- 2. MOTOR DE CICLO INFINITO ---
def buscar_ciclo_infinito(api_key, secret_key):
    try:
        exchange = ccxt.binance({
            'apiKey': api_key, 
            'secret': secret_key,
            'enableRateLimit': True
        })
        G = nx.DiGraph()
        tickers = exchange.fetch_tickers()
        
        fee_factor = 0.99925 # Comisión 0.075% con BNB

        for symbol, data in tickers.items():
            if '/' in symbol and data.get('ask') and data.get('bid'):
                base, quote = symbol.split('/')
                ask, bid = data['ask'], data['bid']
                if ask > 0 and bid > 0:
                    G.add_edge(base, quote, weight=-math.log(bid * fee_factor))
                    G.add_edge(quote, base, weight=-math.log((1/ask) * fee_factor))

        try:
            ciclo = nx.find_negative_cycle(G, 'USDT')
            peso_total = 0
            for i in range(len(ciclo) - 1):
                peso_total += G[ciclo[i]][ciclo[i+1]]['weight']
            
            roi_estimado = (math.exp(-peso_total) - 1) * 100
            return {"status": "success", "ruta": ciclo, "roi": roi_estimado}
        except Exception:
            return {"status": "no_path", "ruta": [], "roi": 0}
            
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 3. EJECUCIÓN DINÁMICA ---
def ejecutar_ruta_dinamica(api_key, secret_key, ruta, monto_usdt):
    try:
        exchange = ccxt.binance({
            'apiKey': api_key, 
            'secret': secret_key, 
            'options': {'defaultType': 'spot'}
        })
        exchange.load_markets()
        balance = monto_usdt
        
        for i in range(len(ruta) - 1):
            source, target = ruta[i], ruta[i+1]
            symbol_buy = f"{target}/{source}"
            symbol_sell = f"{source}/{target}"
            
            if symbol_buy in exchange.markets:
                order = exchange.create_market_buy_order(symbol_buy, balance)
                balance = order['filled']
            elif symbol_sell in exchange.markets:
                order = exchange.create_market_sell_order(symbol_sell, balance)
                balance = order['filled']
            else:
                raise Exception(f"Par no encontrado: {source}/{target}")
                
        return {"status": "success", "final": balance}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 4. COMPLEMENTOS ---
def get_news_events():
    return [{"titulo": "Radar OK", "impacto": "BAJO", "fuente": "System", "hace": "Ahora", "descripcion": "Sistema listo."}]

def get_real_time_opportunities():
    return [{"n": "Monitor Tech", "c": 100, "v": 150}]
