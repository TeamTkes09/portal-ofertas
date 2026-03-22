import streamlit as st
import random

# --- 1. GENERADOR DE CATÁLOGO EXTENSO (32 PRODUCTOS) ---
@st.cache_data(ttl=900)
def get_real_time_opportunities():
    # Base de datos diversificada por nichos reales 2026
    nicho_tech = [
        {"n": "Apple AirTag (4 Pack)", "q": "B08ZG76197", "c": 79, "v": 99},
        {"n": "Sony WH-1000XM5", "q": "B09XS7JWHH", "c": 285, "v": 398},
        {"n": "Samsung T7 Shield 2TB", "q": "B09VLK9W3S", "c": 145, "v": 195},
        {"n": "Logitech MX Master 3S", "q": "B09HM94VDS", "c": 85, "v": 109}
    ]
    nicho_hogar = [
        {"n": "Stanley Quencher 40oz", "q": "B0C1M1YF9P", "c": 35, "v": 85},
        {"n": "Ninja Creami Deluxe", "q": "B0B94Z9V9B", "c": 165, "v": 249},
        {"n": "Cosori Air Fryer 5.8QT", "q": "B07GJBBGHG", "c": 89, "v": 119},
        {"n": "Keurig K-Elite Coffee", "q": "B078WMGD6P", "c": 110, "v": 189}
    ]
    nicho_juguetes = [
        {"n": "LEGO Star Wars Ghost", "q": "B0BXQ4B5RL", "c": 128, "v": 160},
        {"n": "Barbie Dreamhouse 2026", "q": "B0CB6K8C2X", "c": 140, "v": 199},
        {"n": "Pokémon TCG: Elite Box", "q": "B0CVR2T5X8", "c": 38, "v": 55},
        {"n": "Tamagotchi Uni Pink", "q": "B0C399G3SS", "c": 42, "v": 59}
    ]
    
    todos = nicho_tech + nicho_hogar + nicho_juguetes
    categorias = ["TECH", "HOGAR", "JUGUETES"]
    final_list = []
    
    # Generamos los 32 espacios exactos
    for i in range(32):
        base = todos[i % len(todos)]
        var = random.uniform(0.97, 1.03) # Simulación de precio vivo
        costo = round(base['c'] * var, 2)
        venta = base['v']
        
        final_list.append({
            'id': f"SKU-{i:03d}",
            'n': f"{base['n']} - Lote #{i+1}",
            'cat': categorias[i % 3],
            'c': costo,
            'v': venta,
            'q': base['q'],
            'comparativa': [
                {'sitio': 'ebay', 'precio': round(venta * 0.91, 2)},
                {'sitio': 'google', 'precio': round(venta * 0.94, 2)},
                {'sitio': 'shopify', 'precio': round(venta * 1.02, 2)}
            ]
        })
    return final_list

# --- 2. NOTICIAS CONTEXTUALES ---
def get_news_events():
    return [
        {
            "titulo": "🚨 Alerta: Ruptura de Stock en Stanley",
            "descripcion": "El color 'Rose Quartz' está agotado en el 90% de los retailers. El precio en Amazon (FBA) se ha disparado un 35% hoy.",
            "fuente": "Retail Dive", "hace": "8m", "impacto": "CRÍTICO",
            "productos_asociados": [
                {'id': 'N1', 'n': 'Stanley 40oz Rose Quartz', 'cat': 'HOGAR', 'c': 45.0, 'v': 115.0, 'q': 'B0C1M1YF9P', 
                 'comparativa': [{'sitio': 'ebay', 'precio': 95.0}]}
            ]
        },
        {
            "titulo": "📈 Tendencia: Regreso de Consolas Retro",
            "descripcion": "Anuncio de nueva película de Nintendo dispara ventas de hardware antiguo. Gaps detectados entre eBay y Amazon.",
            "fuente": "Gaming Insider", "hace": "25m", "impacto": "MEDIO",
            "productos_asociados": [
                {'id': 'N2', 'n': 'Gameboy Color (Restored)', 'cat': 'TECH', 'c': 65.0, 'v': 120.0, 'q': 'B00002STXP', 
                 'comparativa': [{'sitio': 'google', 'precio': 110.0}]}
            ]
        }
    ]

# --- 3. CRYPTO CON DATOS DE RED ---
@st.cache_data(ttl=300)
def get_crypto_opportunities():
    # Precios base simulados para 2026
    prices = {"BTC": 64200, "ETH": 3450, "SOL": 145, "USDT": 1.00, "MATIC": 0.85, "DOT": 7.20}
    
    return [
        {"coin": "BTC", "red": "Bitcoin (Legacy)", "fee_usd": 15.00, "vel": "30-60 min", "diff": 580, "ex": ["Binance", "Kraken"]},
        {"coin": "ETH", "red": "Ethereum (ERC20)", "fee_usd": 8.50, "vel": "5-12 min", "diff": 45, "ex": ["Coinbase", "Binance"]},
        {"coin": "SOL", "red": "Solana (SPL)", "fee_usd": 0.01, "vel": "< 1 min", "diff": 3.20, "ex": ["Kraken", "Binance"]},
        {"coin": "USDT", "red": "TRON (TRC20)", "fee_usd": 1.00, "vel": "2-5 min", "diff": 0.02, "ex": ["Bybit", "Binance"]},
        {"coin": "MATIC", "red": "Polygon", "fee_usd": 0.05, "vel": "2-3 min", "diff": 0.12, "ex": ["OKX", "Coinbase"]},
        {"coin": "DOT", "red": "Polkadot", "fee_usd": 0.25, "vel": "5 min", "diff": 0.40, "ex": ["Binance", "Kraken"]}
    ]
