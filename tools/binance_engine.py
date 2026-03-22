import ccxt
import networkx as nx
import math

def buscar_n_puntas(api_key, secret_key):
    try:
        exchange = ccxt.binance({'apiKey': api_key, 'secret': secret_key})
        G = nx.DiGraph()
        tickers = exchange.fetch_tickers()
        fee = 0.99925 # 0.075% fee
        
        for sym, d in tickers.items():
            if '/' in sym and d['ask'] and d['bid']:
                b, q = sym.split('/')
                G.add_edge(b, q, weight=-math.log(d['bid'] * fee))
                G.add_edge(q, b, weight=-math.log((1/d['ask']) * fee))
        
        try:
            ciclo = nx.find_negative_cycle(G, 'USDT')
            # (Lógica de ROI simplificada para el ejemplo)
            return {"status": "success", "ruta": ciclo, "roi": 0.85} 
        except:
            return {"status": "no_path"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
