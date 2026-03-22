import ccxt
import networkx as nx
import math

def buscar_n_puntas(api_key, secret_key, vol_min=1000000):
    """
    Busca ciclos de arbitraje de N-puntas filtrando por volumen
    para evitar señales falsas en monedas sin liquidez.
    """
    try:
        exchange = ccxt.binance({
            'apiKey': api_key, 
            'secret': secret_key,
            'enableRateLimit': True
        })
        
        G = nx.DiGraph()
        
        # 1. Obtener todos los tickers de un solo golpe
        all_tickers = exchange.fetch_tickers()
        
        # 2. Filtrar los 500 mejores por volumen (en USDT o equivalente)
        # Esto asegura que operamos donde hay gente comprando y vendiendo
        sorted_tickers = sorted(
            all_tickers.values(), 
            key=lambda x: x.get('quoteVolume', 0), 
            reverse=True
        )[:500]
        
        fee = 0.99925 # 0.075% con BNB activo

        # 3. Construir el Grafo de Liquidez
        for d in sorted_tickers:
            sym = d.get('symbol')
            if sym and '/' in sym and d.get('ask') and d.get('bid'):
                # Evitar monedas con volumen ínfimo (ajustable)
                if d.get('quoteVolume', 0) < vol_min:
                    continue
                    
                b, q = sym.split('/')
                ask, bid = d['ask'], d['bid']
                
                if ask > 0 and bid > 0:
                    # Peso del arco: -log(precio * (1-fee))
                    # De Base a Quote (Venta)
                    G.add_edge(b, q, weight=-math.log(bid * fee))
                    # De Quote a Base (Compra)
                    G.add_edge(q, base := b, weight=-math.log((1/ask) * fee))
        
        # 4. Encontrar el Ciclo de Beneficio (Ciclo Negativo)
        try:
            # Buscamos el ciclo partiendo desde USDT
            ciclo = nx.find_negative_cycle(G, 'USDT')
            
            # 5. Calcular el ROI Real acumulado del ciclo
            peso_total = 0
            for i in range(len(ciclo) - 1):
                peso_total += G[ciclo[i]][ciclo[i+1]]['weight']
            
            # El ROI es la exponencial del peso negativo acumulado
            roi_real = (math.exp(-peso_total) - 1) * 100
            
            # Solo reportar si el ROI es positivo tras comisiones
            if roi_real > 0:
                return {
                    "status": "success", 
                    "ruta": ciclo, 
                    "roi": round(roi_real, 4),
                    "nodos": len(ciclo) - 1
                }
            else:
                return {"status": "no_path", "message": "ROI negativo tras comisiones"}

        except nx.NetworkXNoCycle:
            return {"status": "no_path", "message": "No se encontraron brechas de precio"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
