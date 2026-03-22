import streamlit as st
import random

@st.cache_data(ttl=900)
def get_real_time_opportunities():
    prods = []
    base = {"n": "Producto Real", "cat": "TECH", "c": 50, "v": 100, "q": "B08ZG76197"}
    for i in range(32):
        prods.append({
            'id': f"ID-{i}", 'n': f"{base['n']} {i}", 'cat': base['cat'], 
            'c': base['c'], 'v': base['v'], 'q': base['q'], 'r': 'BAJO',
            'comparativa': [{'sitio': 'ebay', 'precio': 80}, {'sitio': 'google', 'precio': 85}]
        })
    return prods

def get_news_events():
    return [{
        "titulo": "Noticia de Prueba", "descripcion": "Descripción", "fuente": "BBC", 
        "hace": "1m", "impacto": "ALTO", 
        "productos_asociados": [{'id': 'N1', 'n': 'Producto Noticia', 'cat': 'HOGAR', 'c': 40, 'v': 80, 'q': 'B0C1M1YF9P', 'comparativa': []}]
    }]

def get_crypto_opportunities():
    return [{"coin": "BTC", "gap": 500, "roi": 1.2, "exchanges": [{"name": "Binance", "price": 60000, "type": "COMPRA"}]}]
