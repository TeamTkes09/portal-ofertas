import requests
import streamlit as st

@st.cache_data(ttl=3600) # Memoriza la ubicación por 1 hora para ir rápido
def get_market_context():
    try:
        # Consultamos la API de geolocalización
        r = requests.get('https://ipapi.co/json/', timeout=3).json()
        
        # Mapeo de países a dominios de Amazon
        suffixes = {
            "ES": ".es",      # España
            "MX": ".com.mx",   # México
            "US": ".com",      # Estados Unidos
            "AR": ".com.be",   # Argentina (vía Global/Generic)
            "CL": ".cl",       # Chile
            "CO": ".com.co",   # Colombia
            "BR": ".com.br"    # Brasil
        }
        
        pais = r.get('country_name', 'Global')
        codigo = r.get('country_code', 'US')
        
        return {
            "n": pais,
            "s": suffixes.get(codigo, ".com"), # Si no está en la lista, usa el .com por defecto
            "cur": r.get('currency', 'USD')
        }
    except:
        # Si la API falla, devolvemos un valor seguro por defecto
        return {"n": "Global", "s": ".com", "cur": "USD"}
