# data/products.py

def get_all_products():
    products = []

    # --- CATEGORÍA 1: ELECTRÓNICA (32 PRODUCTOS) ---
    electronics = [
        {'id': f'E{i:02d}', 'n': f'Gadget Tech Pro Mod-{i}', 'cat': 'ELECTRÓNICA', 'c': 100+i, 'v': 150+i, 'q': 'tech gadget', 'clr': '#22c55e', 'r': 'BAJO', 'comparativa': [{'sitio': 'ebay', 'precio': 120+i}, {'sitio': 'google', 'precio': 130+i}, {'sitio': 'shopify', 'precio': 140+i}]}
        for i in range(1, 33)
    ]
    products.extend(electronics)

    # --- CATEGORÍA 2: HOGAR Y COCINA (32 PRODUCTOS) ---
    home_kitchen = [
        {'id': f'H{i:02d}', 'n': f'Accesorio Hogar Premium {i}', 'cat': 'HOGAR', 'c': 50+i, 'v': 90+i, 'q': 'home decor', 'clr': '#facc15', 'r': 'MEDIO', 'comparativa': [{'sitio': 'ebay', 'precio': 65+i}, {'sitio': 'google', 'precio': 75+i}, {'sitio': 'shopify', 'precio': 85+i}]}
        for i in range(1, 33)
    ]
    products.extend(home_kitchen)

    # --- CATEGORÍA 3: BELLEZA (32 PRODUCTOS) ---
    beauty = [
        {'id': f'B{i:02d}', 'n': f'Kit Belleza Profesional {i}', 'cat': 'BELLEZA', 'c': 30+i, 'v': 75+i, 'q': 'beauty kit', 'clr': '#ef4444', 'r': 'ALTO', 'comparativa': [{'sitio': 'ebay', 'precio': 45+i}, {'sitio': 'google', 'precio': 55+i}, {'sitio': 'shopify', 'precio': 65+i}]}
        for i in range(1, 33)
    ]
    products.extend(beauty)

    # --- CATEGORÍA 4: HERRAMIENTAS (32 PRODUCTOS) ---
    tools = [
        {'id': f'T{i:02d}', 'n': f'Herramienta Industrial {i}', 'cat': 'HERRAMIENTAS', 'c': 120+i, 'v': 210+i, 'q': 'power tools', 'clr': '#22c55e', 'r': 'BAJO', 'comparativa': [{'sitio': 'ebay', 'precio': 150+i}, {'sitio': 'google', 'precio': 170+i}, {'sitio': 'shopify', 'precio': 190+i}]}
        for i in range(1, 33)
    ]
    products.extend(tools)

    # REPITIE ESTE BLOQUE PARA LAS OTRAS CATEGORÍAS:
    # 5. Deportes, 6. Juguetes, 7. Oficina, 8. Bebé, 9. Automotriz, 10. Mascotas...

    return products
