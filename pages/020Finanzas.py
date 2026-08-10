import streamlit as st
import time
from datetime import date
import yfinance as yf

from constantes import COPYRIGHT
from funciones import presentar_encabezado

if 'usuario' in st.session_state:
    presentar_encabezado()

    st.subheader('Valor de las acciones de la bolsa de Nueva York NYSE')
    st.divider()
    start_date = '2025-01-01'
    start_date2 = '2026-01-01'
    end_date = date.today().strftime("%Y-%m-%d")

    listaacciones = ['Google','Apple','Microsoft','Amazon','Tesla','Meta','CitiGroup', 'Alibaba','S&P 500','AT&T', 'Intel', 'CocaCola', 'Exxon Mobil', 'Walt Disney', 'Toyota','Cisco','Oracle','Nike']
    listasimbolos = ['GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSLA', 'META', 'C', 'BABA', 'FB', 'T', 'INTC', 'KO', 'XOM', 'DIS', 'TM', 'CSCO', 'ORCL', 'NKE']

    datos = yf.Tickers('GOOGL AAPL MSFT AMZN TSLA META C BABA FB T INTC KO XOM DIS TM CSCO ORCL NKE')
    data = yf.download(listasimbolos, start_date2, end_date)
    rendimientos = (data / data.iloc[0] - 1) * 100
    total = int(len(listaacciones))
    for i in range(0,total,3):
        try:
            seleccion1 = listaacciones[i]
            seleccion2 = listaacciones[i+1]
            seleccion3 = listaacciones[i+2]

            col1, col2, col3 = st.columns(3)

            try:
                indice1 = listaacciones.index(seleccion1)
                simbolo1 = listasimbolos[indice1]
                datos11 = datos.tickers[simbolo1].info
                empresa = datos11['symbol'] + "--" + datos11['shortName']
                col1.write(f"{empresa}")
                try:
                    col1.write(f"**Precio:** USD {datos11['currentPrice']:.2f}")
                except:
                    col1.write(f"**Precio:** No disponible")
                try:
                    col1.write(f"**Volumen:** {datos11['volume']:,}")
                except:
                    col1.write(f"**Volumen:** No disponible")
                try:
                    col1.write(f"**Capitalización de Mercado:** USD {datos11['marketCap']:,}")
                except:
                    col1.write(f"**Capitalización de Mercado:** No disponible")
                stock1 = yf.Ticker(simbolo1)
                data1 = stock1.history(start=start_date, end=end_date)
                col1.line_chart(data1, y='Close', x_label = empresa, y_label= 'Precio USD', width='stretch')
            except:
                col1.write('Sin datos')

            try:
                indice2 = listaacciones.index(seleccion2)
                simbolo2 = listasimbolos[indice2]
                datos22 = datos.tickers[simbolo2].info
                empresa = datos22['symbol'] + "--" + datos22['shortName']
                col2.write(f"{empresa}")
                try:
                    col2.write(f"**Precio:** USD {datos22['currentPrice']:.2f}")
                except:
                    col2.write(f"**Precio:** No disponible")
                try:
                    col2.write(f"**Volumen:** {datos22['volume']:,}")
                except:
                    col2.write(f"**Volumen:** No disponible")
                try:
                    col2.write(f"**Capitalización de Mercado:** USD {datos22['marketCap']:,}")
                except:
                    col2.write(f"**Capitalización de Mercado:** No disponible")
                stock2 = yf.Ticker(simbolo2)
                data2 = stock2.history(start=start_date, end=end_date)
                col2.line_chart(data2, y='Close', x_label = empresa, y_label= 'Precio USD', width='stretch')
            except:
                col2.write('Sin datos')

            try:
                indice3 = listaacciones.index(seleccion3)
                simbolo3 = listasimbolos[indice3]
                datos33 = datos.tickers[simbolo3].info
                empresa = datos33['symbol'] + "--" + datos33['shortName']
                col3.write(f"{empresa}")
                try:
                    col3.write(f"**Precio:** USD {datos33['currentPrice']:.2f}")
                except:
                    col3.write(f"**Precio:** No disponible")
                try:
                    col3.write(f"**Volumen:** {datos33['volume']:,}")
                except:
                    col3.write(f"**Volumen:** No disponible")
                try:
                    col3.write(f"**Capitalización de Mercado:** USD {datos33['marketCap']:,}")
                except:
                    col3.write(f"**Capitalización de Mercado:** No disponible")
                stock3 = yf.Ticker(simbolo3)
                data3 = stock3.history(start=start_date, end=end_date)
                col3.line_chart(data3, y='Close', x_label = empresa, y_label= 'Precio USD', width='stretch')
            except:
                col3.write('Sin datos')

        except:
            break
    st.divider()  
    st.write(COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")    
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 