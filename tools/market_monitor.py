import ccxt
import requests

def get_binance_prices():
    try:
        ex = ccxt.binance({'enableRateLimit': True})
        tickers = ex.fetch_tickers()
        return [{
            "Token": s.split('/')[0],
            "Precio Compra (Ask)": t['ask'],
            "Precio Venta (Bid)": t['bid'],
            "Spread %": round(((t['ask']-t['bid'])/t['ask']*100), 4) if t['ask']>0 else 0,
            "Volumen 24h": t['quoteVolume'],
            "Fuente": "Binance Live"
        } for s, t in tickers.items() if s.endswith('/USDT')]
    except:
        return []

def get_coingecko_prices():
    # Lógica de fallback que ya teníamos
    return []
