from tools.market_monitor import get_binance_prices
from tools.binance_engine import find_n_path_cycle, execute_trade_cycle

def get_crypto_opportunities():
    # Intentamos Binance, si no, Coingecko
    prices = get_binance_prices()
    return prices if prices else []

def buscar_ciclo_infinito(k, s):
    return find_n_path_cycle(k, s)

def ejecutar_ruta_dinamica(k, s, r, m):
    return execute_trade_cycle(k, s, r, m)

# Datos de relleno para retail
def get_real_time_opportunities():
    return [{"n": "Monitor Tech", "c": 100, "v": 150}]
