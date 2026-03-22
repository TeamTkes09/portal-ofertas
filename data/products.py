# data/products.py

def get_all_products():
    return [
        {
            'id': 'H32',
            'n': 'Lote Fan Pack x10 ARGB 120mm',
            'cat': 'HARDWARE', 'c': 85, 'v': 195,
            'q': 'argb case fan bulk 120mm', 'clr': '#ef4444', 'r': 'ALTO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 135, 'url': 'https://www.google.com/search?q=argb+fan+10+pack+price'},
                {'sitio': 'eBay', 'precio': 155, 'url': 'https://www.ebay.com/sch/i.html?_nkw=120mm+argb+fan+lot'},
                {'sitio': 'Retail Local', 'precio': 195, 'url': 'https://www.google.com/search?q=tienda+computacion+ventiladores+argb'}
            ]
        },
        {
            'id': 'H05',
            'n': 'Corsair Dominator Titanium 64GB DDR5',
            'cat': 'HARDWARE', 'c': 210, 'v': 340,
            'q': 'corsair dominator titanium 64gb ddr5', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 285, 'url': 'https://www.google.com/search?q=corsair+dominator+64gb+ddr5+price'},
                {'sitio': 'Newegg', 'precio': 310, 'url': 'https://www.newegg.com/p/pl?d=corsair+dominator+64gb'},
                {'sitio': 'Retail Local', 'precio': 340, 'url': 'https://www.google.com/search?q=corsair+dominator+titanium+precio+local'}
            ]
        },
        {
            'id': 'H30',
            'n': 'TeamGroup T-Force Delta 32GB RGB',
            'cat': 'HARDWARE', 'c': 105, 'v': 165,
            'q': 'teamgroup t-force delta ddr5 32gb', 'clr': '#22c55e', 'r': 'BAJO',
            'comparativa': [
                {'sitio': 'Google Shopping', 'precio': 130, 'url': 'https://www.google.com/search?q=t-force+delta+32gb+ddr5+price'},
                {'sitio': 'eBay', 'precio': 145, 'url': 'https://www.ebay.com/sch/i.html?_nkw=t-force+delta+32gb+ddr5'},
                {'sitio': 'Retail Local', 'precio': 165, 'url': 'https://www.google.com/search?q=t-force+delta+32gb+precio+retail'}
            ]
        }
        # Puedes seguir añadiendo los 29 restantes aquí...
    ]
