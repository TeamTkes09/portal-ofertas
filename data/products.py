import streamlit as st
import random

# --- 1. PRODUCTOS FÍSICOS (REFRESCO 15 MIN) ---
@st.cache_data(ttl=900)
def get_real_time_opportunities():
    """Genera 32 oportunidades de arbitraje retail con datos de 2026"""
    catalogo_maestro = [
        {"n": "Apple AirTag (4 Pack)", "cat": "TECH", "c_base": 79, "v_base": 99, "q": "B08ZG76197"},
        {"n": "Stanley Quencher 40oz", "cat": "HOGAR", "c_base": 35, "v_base": 85, "q": "B0C1M1YF9P"},
        {"n": "Sony WH-1000XM5", "cat": "TECH", "c_base": 285, "v_base": 399, "q": "B09XS7JWHH"},
        {"n": "LEGO Star Wars Ghost", "cat": "JUGUETES", "c_base": 128, "v_base": 159, "q": "B0BXQ4B5RL"},
        {"n": "Ninja Creami Deluxe", "cat": "HOGAR", "c_base": 165, "v_base": 245, "q": "B0B94Z9V9B"},
        {"n": "Logitech MX Master 3S", "cat": "TECH", "c_base": 82, "v_base": 109, "q": "B09HM94VDS"},
        {"n": "Olaplex No. 3 Hair", "cat": "BELLEZA", "c_base": 18, "v_base": 30, "q": "B0086OT8S2"},
        {"n": "DJI Mini 4 Pro Combo", "cat": "TECH", "c_base": 880, "v_base": 1099, "q": "B0CHMS6S46"}
    ]
    
    productos = []
    for i in range(32):
        base = catalogo_maestro[i % len(catalogo_maestro)]
        # Simulación de volatilidad de precios de Amazon (+/- 2%)
        variacion = random.uniform(0.98, 1.02)
        costo_actual = round(base['c_base'] * variacion, 2)
        venta_actual = round(base['v_base'], 2)
        
        productos.append({
            'id': f"SKU-{2026}-{i:03d}",
            'n': f"{base['n']} - Lote {i+1}",
            'cat': base['cat'],
            'c': costo_actual,
            'v': venta_actual,
            'q': base['q'],
            'r': "BAJO" if (venta_actual - costo_actual)/costo_actual > 0.3 else "MEDIO",
            'comparativa': [
                {'sitio': 'ebay', 'precio': round(venta_actual * 0.92, 2)},
                {'sitio': 'google', 'precio': round(venta_actual * 0.96, 2)},
                {'sitio': 'shopify', 'precio': round(venta_actual * 1.04, 2)}
            ]
        })
    return productos

# --- 2. NOTICIAS OPERATIVAS (VINCULADAS A PRODUCTOS) ---
def get_news_events():
    """Eventos de mercado que disparan oportunidades de compra"""
    return [
        {
            "titulo": "🔥 Viral: Stanley 'Azure' Agotado en Target",
            "descripcion": "Ruptura de stock masiva en tiendas físicas. Los precios de reventa en Amazon han escalado un 45% en las últimas 24h.",
            "fuente": "TikTok Trends",
            "hace": "10 min",
            "impacto": "ALTO",
            "productos_asociados": [
                {'id': 'NW1', 'n': 'Stanley 40oz Azure Edition', 'cat': 'HOGAR', 'c': 45.0, 'v': 95.0, 'q': 'B0C1M1YF9P', 'r': 'BAJO', 'comparativa': [{'sitio': 'ebay', 'precio': 85}]}
            ]
        },
        {
            "titulo": "📦 Escasez Global: SSD Samsung T7",
            "descripcion": "Falla técnica en la planta de ensamble de Corea. Se espera una caída del 20% en el suministro para el próximo mes.",
            "fuente": "Bloomberg Tech",
            "hace": "40 min",
            "impacto": "CRÍTICO",
            "productos_asociados": [
                {'id': 'NW2', 'n': 'Samsung T7 Shield 2TB', 'cat': 'TECH', 'c': 148.0, 'v': 210.0, 'q': 'B09VLK9W3S', 'r': 'MEDIO', 'comparativa': [{'sitio': 'ebay', 'precio': 185}]}
            ]
        }
    ]

# --- 3. CRIPTOMONEDAS (DATOS TÉCNICOS PARA ARBITRAJE) ---
@st.cache_data(ttl=300)
def get_crypto_opportunities():
    """Diferenciales entre exchanges incluyendo costos de red (Gas)"""
    # Precios base simulados con fluctuación real
    btc_ref = 64200 +
