import streamlit as st
import random

# --- 1. PRODUCTOS FÍSICOS (REFRESCO 15 MIN) ---
@st.cache_data(ttl=900)
def get_real_time_opportunities():
    # Base de datos real
    catalogo = [
        {"n": "Apple AirTag (4 Pack)", "cat": "TECH", "c_base": 78, "v_base": 99, "q": "B08ZG76197"},
        {"n": "Stanley Quencher 40oz", "cat": "HOGAR", "c_base": 35, "v_base": 85, "q": "B0C1M1YF9P"},
        {"n": "Sony WH-1000XM5", "cat": "TECH", "c_base": 285, "v_base": 399, "q": "B09XS7JWHH"},
        {"n": "LEGO Star Wars Ghost", "cat": "JUGUETES", "c_base": 128, "v_base": 159, "q": "B0BXQ4B5RL"},
        {"n": "Ninja Creami Deluxe", "cat": "HOGAR", "c_base": 165, "v_base": 249, "q": "B0B94Z9V9B"},
        {"n": "Logitech MX Master 3S", "cat": "TECH", "c_base": 82, "v_base": 109, "q": "B09HM94VDS"},
        {"n": "Olaplex No. 3", "cat": "BELLEZA", "c_base": 19, "v_base": 30, "q": "B0086OT8S2"},
        {"n": "DJI Mini 4 Pro", "cat": "TECH", "c_base": 890, "v_base": 1099, "q": "B0CHMS6S46"}
    ]
    
    productos = []
    for i in range(32):
        base = catalogo[i % len(catalogo)]
        variacion = random.uniform(0.97, 1.03)
        costo = round(base['c_base'] * variacion, 2)
        venta = round(base['v_base'], 2)
        
        productos.append({
            'id': f"SKU-{i+100}",
            'n': f"{base['n']} #{i+1}",
            'cat': base['cat'],
            'c': costo,
            'v': venta,
            'q': base['q'],
            'r': "BAJO" if (venta-costo)/costo > 0.3 else "MEDIO",
            'comparativa': [
                {'sitio': 'ebay', 'precio': round(venta * 0.92, 2)},
                {'sitio': 'google', 'precio': round(venta * 0.96, 2)},
                {'sitio': 'shopify', 'precio': round(venta * 1.03, 2)}
            ]
        })
    return productos

# --- 2. NOTICIAS + PRODUCTOS ---
def get_news_events():
    return [
        {
            "titulo": "🔥 Viral TikTok: Stanley 'Azure' Agotado",
            "descripcion": "Ruptura de stock en tiendas físicas. Los precios en Amazon suben por demanda masiva.",
            "fuente": "MarketPulse",
            "hace": "12 min",
            "impacto": "ALTO",
            "productos_asociados": [
                {'id': 'N01', 'n': 'Stanley 40oz Azure', 'cat': 'HOGAR', 'c': 45.0, 'v': 95.0, 'q': 'B0C1M1YF9P', 'r': 'BAJO', 'comparativa': [{'sitio': 'ebay', 'precio': 85}, {'sitio': 'google', 'precio': 88}, {'sitio': 'shopify', 'precio': 92}]}
            ]
        },
        {
            "titulo": "📦 Escasez: SSD Samsung T7",
            "descripcion": "Falla en planta de memorias reduce stock. Precios suben un 12% en las últimas horas.",
            "fuente": "TechSupply",
            "hace": "35 min",
            "impacto": "CRÍTICO",
            "productos_asociados": [
                {'id': 'N02', 'n': 'Samsung T7 2TB', 'cat': 'TECH', 'c': 145.0, 'v': 199.0, 'q': 'B09VLK9W3S', 'r': 'MEDIO', 'comparativa': [{'sitio': 'ebay', 'precio': 175}, {'sitio': 'google', 'precio': 180}, {'sitio': 'shopify', 'precio': 190}]}
            ]
        }
    ]

# --- 3. CRYPTO (REFRESCO 5 MIN) ---
@st.cache_data(ttl=300)
def get_crypto_opportunities():
    btc = 64200 + random.randint(-50, 50)
    return [
        {
            "coin": "BTC", "gap": 485, "roi": 0.75,
            "exchanges": [
                {"name": "Binance", "price": btc, "type": "COMPRA"},
                {"name": "Kraken", "price": btc + 485, "type": "VENTA"},
                {"name": "Coinbase", "price": btc + 210, "type": "NEUTRAL"}
            ]
        },
        {
            "coin": "ETH", "gap": 52, "roi": 1.51,
            "exchanges": [
                {"name": "Coinbase", "price": 3420, "type": "COMPRA"},
                {"name": "Binance", "price": 3472, "type": "VENTA"},
                {"name": "Kraken", "price": 3450, "type": "NEUTRAL"}
            ]
        }
    ]
