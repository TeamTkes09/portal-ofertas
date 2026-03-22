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

        # Buscar el ciclo de mayor ganancia partiendo de USDTimport ccxt
import networkx as nx
import math
import streamlit as st
import requests
import pandas as pd
import time

# --- CONFIGURACIÓN E ESTÁNDARES ---
NETWORK_FEES = {
    'BTC': {'red': 'Bitcoin', 'fee': 15.0},
    'ETH': {'red': 'ERC20', 'fee': 8.5},
    'SOL': {'red': 'Solana', 'fee': 0.01},
    'USDT': {'red': 'TRC20', 'fee': 1.0},
    'DEFAULT': {'red': 'BSC/BEP20', 'fee': 0.5}
}

# --- 1. MONITOR DE SPREADS (PRIORIDAD BINANCE) ---
@st.cache_data(ttl=5)
def get_crypto_opportunities(api_key=None, secret_key=None):
    """
    Obtiene precios directos de Binance para evitar latencia y bloqueos de API.
    Si Binance falla, intenta conectar con CoinGecko.
    """
    try:
        # Conexión rápida (Pública o Privada)
        exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key,
            'enableRateLimit': True
        })
        
        tickers = exchange.fetch_tickers()
        binance_data = []
        
        # Filtramos solo pares contra USDT para el monitor principal
        for symbol, t in tickers.items():
            if symbol.endswith('/USDT'):
                token = symbol.split('/')[0]
                # Calculamos el spread real del libro de órdenes (Bid/Ask)
                ask = t['ask'] if t['ask'] else 0
                bid = t['bid'] if t['bid'] else 0
                spread_pct = ((ask - bid) / ask * 100) if ask > 0 else 0
                
                binance_data.append({
                    "Token": token,
                    "Precio Compra (Ask)": ask,
                    "Precio Venta (Bid)": bid,
                    "Spread %": round(spread_pct, 4),
                    "Volumen 24h": t['quoteVolume'],
                    "Cambio 24h %": t['percentage'],
                    "Fuente": "Binance Live"
                })
        
        # Ordenar por volumen para mostrar los más importantes primero
        df = pd.DataFrame(binance_data).sort_values(by="Volumen 24h", ascending=False)
        return df.to_dict('records')

    except Exception as e:
        # Si Binance falla, intentamos CoinGecko como Plan B
        return get_coingecko_fallback()

def get_coingecko_fallback():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 50, "page": 1}
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return [{"Token": c['symbol'].upper(), "Precio Compra (Ask)": c['current_price'], 
                     "Fuente": "CoinGecko Fallback"} for c in data]
    except:
        return []

# --- 2. MOTOR DE CICLO INFINITO (N-PUNTAS) ---
def buscar_ciclo_infinito(api_key, secret_key):
    try:
        exchange = ccxt.binance({'apiKey': api_key, 'secret': secret_key})
        G = nx.DiGraph()
        tickers = exchange.fetch_tickers()
        
        # Costo con descuento BNB (0.075%)
        fee_factor = 0.99925 

        for symbol, data in tickers.items():
            if '/' in symbol and data['ask'] and data['bid']:
                base, quote = symbol.split('/')
                ask, bid = data['ask'], data['bid']
                if ask > 0 and bid > 0:
                    # Logaritmos para encontrar ciclos de ganancia (Bellman-Ford)
                    G.add_edge(base, quote, weight=-math.log(bid * fee_factor))
                    G.add_edge(quote, base, weight=-math.log((1/ask) * fee_factor))

        try:
            ciclo = nx.find_negative_cycle(G, 'USDT')
            peso_total = sum(G[ciclo[i]][ciclo[i+1]]['weight'] for i in range(len(ciclo)-1))
            roi_estimado = (math.exp(-peso_total) - 1) * 100
            return {"status": "success", "ruta": ciclo, "roi": roi_estimado}
        except nx.NetworkXNoCycle:
            return {"status": "no_path", "ruta": [], "roi": 0}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 3. EJECUCIÓN DINÁMICA ---
def ejecutar_ruta_dinamica(api_key, secret_key, ruta, monto_usdt):
    exchange = ccxt.binance({'apiKey': api_key, 'secret': secret_key, 'options': {'defaultType': 'spot'}})
    try:
        balance = monto_usdt
        for i in range(len(ruta) - 1):
            source, target = ruta[i], ruta[i+1]
            symbol_buy = f"{target}/{source}"
            symbol_sell = f"{source}/{target}"
            
            if symbol_buy in exchange.markets:
                order = exchange.create_market_buy_order(symbol_buy, balance)
                balance = order['filled']
            else:
                order = exchange.create_market_sell_order(symbol_sell, balance)
                balance = order['filled']
        return {"status": "success", "final": balance}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 4. RETAIL & NOTICIAS ---
def get_news_events():
    return [{"titulo": "Arbitraje Activo", "impacto": "MEDIO", "fuente": "Binance System", "hace": "Ahora", "descripcion": "Monitorizando N-Puntas."}]

def get_real_time_opportunities():
    return [{"n": "Tech Item", "c": 100, "v": 120}]
