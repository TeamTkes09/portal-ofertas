import streamlit as st
import random

# --- 1. PRODUCTOS FÍSICOS ---
@st.cache_data(ttl=900)
def get_real_time_opportunities():
    items = [
        {"n": "Apple AirTag 4-Pack", "cat": "TECH", "c": 75.0, "v": 99.0, "q": "B08ZG76197"},
        {"n": "Stanley Quencher 40oz", "cat": "HOGAR", "c": 35.0, "v": 85.0, "q": "B0C1M1YF9P"},
        {"n": "Sony WH-1000XM5", "cat": "TECH", "c": 280.0, "v": 398.0, "q": "B09XS7JWHH"},
        {"n": "LEGO Ghost & Phantom", "cat": "JUGUETES", "c": 125.0, "v": 159.0, "q": "B0BXQ4B5RL"}
    ]
    final_list = []
    for i in range(32):
        base = items[i % len(items)]
        var = random.uniform(0.98, 1.02)
        final_list.append({
            'id': f"SKU-{i}", 'n': f"{base['n']} #{i+1}", 'cat': base['cat'],
            'c': round(base['c'] * var, 2), 'v': base['v'], 'q': base['q'],
            'comparativa': [{'sitio': 'ebay', 'precio': round(base['v']*0.9, 2)}, 
                           {'sitio': 'google', 'precio': round(base['v']*0.95, 2)}]
        })
    return final_list

# --- 2. NOTICIAS ---
def get_news_events():
    return [{
        "titulo": "📈 Viral: Escasez de Termos Stanley",
        "descripcion": "Ruptura de stock masiva. Los precios suben un 40%.",
        "fuente": "TikTok", "hace": "5m", "impacto": "ALTO",
        "productos_asociados": [{
            'id': 'N1', 'n': 'Stanley Azure 40oz', 'cat': 'HOGAR', 'c': 45.0, 'v': 95.0, 
            'q': 'B0C1M1YF9P', 'comparativa': [{'sitio': 'ebay', 'precio': 85.0}]
        }]
    }]

# --- 3. CRYPTO ---
@st.cache_data(ttl=300)
def get_crypto_opportunities():
    btc = 64000 + random.randint(-100, 100)
    return [
        {"coin": "BTC", "red": "Bitcoin Network", "fee_red": 0.0002, "exchanges": [
            {"name": "Binance", "price": btc, "type": "COMPRA"},
            {"name": "Kraken", "price": btc + 550, "type": "VENTA"}
        ]},
        {"coin": "SOL", "red": "Solana", "fee_red": 0.01, "exchanges": [
            {"name": "Kraken", "price": 145.0, "type": "COMPRA"},
            {"name": "Binance", "price": 149.5, "type": "VENTA"}
        ]}
    ]
