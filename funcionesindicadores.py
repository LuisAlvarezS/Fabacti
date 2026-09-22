import yfinance as yf
import streamlit as st

def valor_oro():
    try:
        oro = yf.Ticker("GC=F")
        info_oro = oro.info
        roro = info_oro.get('regularMarketPreviousClose', None)
        return roro
    except Exception as e:
        print(f"Error al obtener el valor del oro: {e}")
        return None

def valor_euro():
    try:
        euro = yf.Ticker("EURCOP=X")
        info_euro = euro.info
        reuro = info_euro.get('regularMarketPreviousClose', None)
        return reuro
    except Exception as e:
        print(f"Error al obtener el valor del euro: {e}")
        return None

def valor_cafe():
    try:
        cafe = yf.Ticker("KC=F")
        info_cafe = cafe.info
        rcafe = info_cafe.get('regularMarketPreviousClose', None) / 100
        return rcafe
    except Exception as e:
        print(f"Error al obtener el valor del café: {e}")
        return None

def valor_petroleo():
    try:
        petroleo = yf.Ticker("BZ=F")
        info_petroleo = petroleo.info
        rpetroleo = info_petroleo.get('regularMarketPreviousClose', None) 
        return rpetroleo
    except Exception as e:
        print(f"Error al obtener el valor del petróleo: {e}")
        return None

