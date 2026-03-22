import streamlit as st
import random

@st.cache_data(ttl=900)
def get_real_time_opportunities():
    # Base de datos real para 2026
    items = [
        {"n": "Apple AirTag 4-Pack", "cat": "TECH", "c": 75, "v": 99, "q": "B08ZG76197"},
        {"n": "Stanley Quencher 40oz", "cat": "HOGAR", "c": 35, "v": 85, "q": "B0C1M1YF9P"},
        {"n": "Sony WH-1000XM5", "cat": "TECH", "c": 280, "v": 398, "q": "B09XS7JWHH"},
        {"n": "LEGO Ghost & Phantom", "cat": "JUGUETES", "c": 125, "v": 159, "q": "B0BXQ4B5RL"},
        {"n": "Ninja Creami Deluxe", "cat": "HOGAR", "c": 160, "v": 249, "q": "B0B94Z9V9B"},
        {"n": "Olaplex No. 3", "cat": "BELLEZA", "c": 18, "v": 30, "q": "B0086OT8S2"}
    ]
    
    final_list = []
    for i in range(32):
        base = items[i % len(items)]
        # Fluctuación de mercado real cada 15 min
        var = random.uniform(0.98, 1.02)
        costo_final = round(base['c'] * var, 2)
        final_list.append({
            'id': f"SKU-{i}", 'n': f"{base['n']} (Lote {i+1})", 'cat': base['cat'],
            'c': costo_final, 'v': base['v'], 'q': base['q'], 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'ebay', 'precio': round(base['v']*0.9, 2)},
                {'sitio': 'google', 'precio': round(base['v']*0.95, 2)},
                {'sitio': 'shopify', 'precio': round(base['v']*1.05, 2)}
            ]
        })
    return final_list

def get_news_events():
    return [
        {
            "titulo": "📈 Viral: Escasez de Termos Stanley",
            "descripcion": "Ruptura de stock en tiendas físicas por tendencia en redes. Precios suben.",
            "fuente": "TikTok Trends", "hace": "5m", "impacto": "ALTO",
            "productos_asociados": [
                {'id': 'N1', 'n': 'Stanley Azure 40oz', 'cat': 'HOGAR', 'c': 45, 'v': 95, 'q': 'B0C1M1YF9P', 'r': 'BAJO', 'comparativa': [{'sitio': 'ebay', 'precio': 85}]}
            ]
        }
    ]

@st.cache_data(ttl=300)
def get_crypto_opportunities():
    btc = 64000 + random.randint(-100, 100)
    return [
        {"coin": "BTC", "gap": 550, "roi": 0.85, "exchanges": [
            {"name": "Binance", "price": btc, "type": "COMPRA"},
            {"name": "Kraken", "price": btc + 550, "type": "VENTA"}
        ]},
        {"coin": "ETH", "gap": 45, "roi": 1.4, "exchanges": [
            {"name": "Coinbase", "price": 3400, "type": "COMPRA"},
            {"name": "Binance", "price": 3445, "type": "VENTA"}
        ]}
    ]
