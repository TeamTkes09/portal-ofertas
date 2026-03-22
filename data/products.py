# data/products.py

def get_all_products():
    return [
        # --- CATEGORÍA: CELULARES (16 Productos de muestra) ---
        {
            'id': 'C01', 'n': 'Samsung Galaxy S24 Ultra 512GB', 'cat': 'CELULARES', 
            'c': 1150, 'v': 1450, 'q': 'samsung galaxy s24 ultra unlocked', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 1299, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 1450, 'url': '#'}
            ]
        },
        {
            'id': 'C02', 'n': 'iPhone 15 Pro Max 256GB (Renewed)', 'cat': 'CELULARES', 
            'c': 940, 'v': 1180, 'q': 'iphone 15 pro max renewed', 'clr': '#facc15', 'r': 'MEDIO',
            'comparativa': [
                {'sitio': 'eBay Refurbished', 'precio': 1050, 'url': '#'},
                {'sitio': 'Marketplace', 'precio': 1180, 'url': '#'}
            ]
        },
        {
            'id': 'C03', 'n': 'Google Pixel 8 Pro 128GB', 'cat': 'CELULARES', 
            'c': 749, 'v': 990, 'q': 'google pixel 8 pro unlocked', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Google Store', 'precio': 899, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 990, 'url': '#'}
            ]
        },
        {
            'id': 'C04', 'n': 'Xiaomi 14 Ultra Photography Kit', 'cat': 'CELULARES', 
            'c': 1100, 'v': 1550, 'q': 'xiaomi 14 ultra global version', 'clr': '#ef4444', 'r': 'ALTO',
            'comparativa': [
                {'sitio': 'AliExpress Global', 'precio': 1300, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 1550, 'url': '#'}
            ]
        },
        {
            'id': 'C05', 'n': 'OnePlus 12 512GB Emerald', 'cat': 'CELULARES', 
            'c': 799, 'v': 1050, 'q': 'oneplus 12 unlocked', 'clr': '#facc15', 'r': 'MEDIO',
            'comparativa': [
                {'sitio': 'BestBuy', 'precio': 899, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 1050, 'url': '#'}
            ]
        },
        {
            'id': 'C06', 'n': 'Nothing Phone (2) 256GB', 'cat': 'CELULARES', 
            'c': 590, 'v': 820, 'q': 'nothing phone 2 unlocked', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'StockX', 'precio': 700, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 820, 'url': '#'}
            ]
        },
        # (Agregaremos más IDs C07-C16 siguiendo este patrón para completar 16 celulares)

        # --- CATEGORÍA: HARDWARE (16 Productos de muestra) ---
        {
            'id': 'H01', 'n': 'AMD Ryzen 9 7950X3D', 'cat': 'HARDWARE', 
            'c': 580, 'v': 740, 'q': 'ryzen 9 7950x3d', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Newegg', 'precio': 650, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 740, 'url': '#'}
            ]
        },
        {
            'id': 'H02', 'n': 'RTX 4080 Super ASUS ROG Strix', 'cat': 'HARDWARE', 
            'c': 1150, 'v': 1580, 'q': 'rtx 4080 super rog strix', 'clr': '#ef4444', 'r': 'ALTO',
            'comparativa': [
                {'sitio': 'B&H Photo', 'precio': 1300, 'url': '#'},
                {'sitio': 'Retail Local', 'precio': 1580, 'url': '#'}
            ]
        },
        {
            'id': 'H03', 'n': 'Lote 5x SSD Samsung 990 Pro 2TB', 'cat': 'HARDWARE', 
            'c': 850, 'v': 1350, 'q': 'samsung 990 pro 2tb bulk', 'clr': '#facc15', 'r': 'MEDIO',
            'comparativa': [
                {'sitio': 'eBay Business', 'precio': 1100, 'url': '#'},
                {'sitio': 'Local IT Store', 'precio': 1350, 'url': '#'}
            ]
        },
        {
            'id': 'H04', 'n': 'G.Skill Trident Z5 RGB 64GB DDR5', 'cat': 'HARDWARE', 
            'c': 215, 'v': 320, 'q': 'g.skill trident z5 64gb ddr5', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 270, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 320, 'url': '#'}
            ]
        },
        {
            'id': 'H05', 'n': 'Corsair RM1000e PSU (White Edition)', 'cat': 'HARDWARE', 
            'c': 160, 'v': 245, 'q': 'corsair rm1000e white', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Newegg', 'precio': 190, 'url': '#'},
                {'sitio': 'Tienda Local', 'precio': 245, 'url': '#'}
            ]
        },
        {
            'id': 'H06', 'n': 'Lote 10x Ventiladores Noctua NF-A12', 'cat': 'HARDWARE', 
            'c': 300, 'v': 450, 'q': 'noctua nf-a12 pack', 'clr': '#facc15', 'r': 'MEDIO',
            'comparativa': [
                {'sitio': 'eBay', 'precio': 380, 'url': '#'},
                {'sitio': 'Tienda Local
