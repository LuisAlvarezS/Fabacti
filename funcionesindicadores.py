import yfinance as yf
import streamlit as st

def valor_oro():
    try:
        oro = yf.Ticker("GC=F")
        data_oro = oro.history(period="1d")
        return data_oro['Open'].iloc[-1]
    except Exception as e:
        print(f"Error al obtener el valor del oro: {e}")
        return None

def valor_euro():
    try:
        euro = yf.Ticker("EURCOP=X")
        data_euro = euro.history(period="1d")
        return data_euro['Open'].iloc[-1]    
    except Exception as e:
        print(f"Error al obtener el valor del euro: {e}")
        return None

def valor_cafe():
    try:
        cafe = yf.Ticker("KC=F")
        data_cafe = cafe.history(period="1d")
        return data_cafe['Open'].iloc[-1] / 100
    except Exception as e:
        print(f"Error al obtener el valor del café: {e}")
        return None

def valor_petroleo():
    try:
        petroleo = yf.Ticker("BZ=F")
        data_petroleo = petroleo.history(period="1d")
        return data_petroleo['Open'].iloc[-1]
    except Exception as e:
        print(f"Error al obtener el valor del petróleo: {e}")
        return None

