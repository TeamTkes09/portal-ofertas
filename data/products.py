# data/products.py

def get_all_products():
    return [
        {
            'id': 'H32',
            'n': 'Lote Fan Pack x10 ARGB 120mm',
            'cat': 'HARDWARE', 'c': 85, 'v': 195,
            'q': 'argb case fan bulk 120mm', 'clr': '#ef4444', 'r': 'ALTO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 135, 'url': 'https://google.com/search?q=10+pack+argb+fans'},
                {'sitio': 'eBay (Promedio)', 'precio': 155, 'url': 'https://ebay.com'},
                {'sitio': 'Tienda Local', 'precio': 195, 'url': 'https://google.com'}
            ]
        },
        {
            'id': 'H05',
            'n': 'Corsair Dominator Titanium 64GB DDR5',
            'cat': 'HARDWARE', 'c': 210, 'v': 340,
            'q': 'corsair dominator titanium 64gb ddr5', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 285, 'url': 'https://google.com'},
                {'sitio': 'Newegg', 'precio': 310, 'url': 'https://newegg.com'},
                {'sitio': 'Tienda Local', 'precio': 340, 'url': 'https://google.com'}
            ]
        },
        {
            'id': 'H10',
            'n': 'Crucial T705 2TB Gen5 SSD',
            'cat': 'HARDWARE', 'c': 240, 'v': 385,
            'q': 'crucial t705 2tb ssd', 'clr': '#facc15', 'r': 'MEDIO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 310, 'url': 'https://google.com'},
                {'sitio': 'B&H Photo', 'precio': 345, 'url': 'https://bhphotovideo.com'},
                {'sitio': 'Tienda Local', 'precio': 385, 'url': 'https://google.com'}
            ]
        }
    ]
