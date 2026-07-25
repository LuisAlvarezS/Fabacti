import pandas as pd
from streamlit import cursor

import sqlite3

# # Leer todo el contenido del archivo
# with open("HistoricoTRM.txt", "r") as archivo:
#    for linea in archivo:
#        print(linea.strip(','))  # Imprime cada línea sin espacios en blanco al inicio y al final   
#   contenido = archivo.read()
#   print(contenido)

conn = sqlite3.connect("fabacti.db")
cursor = conn.cursor()

# df = pd.read_csv("libros.txt", sep=",", header=0, names=["id_libros", "isbn", "titulo", "autor", "leidom", "leidoa", "portada", "resumen", "categoria", "fechapublicacion", "editorial", "paginas", "comentario"])
# for index, row in df.iterrows():
#     cursor.execute("INSERT INTO libros (id_libros, isbn, titulo, autor, leidom, leidoa, portada, resumen, categoria, fechapublicacion, editorial, paginas, comentario) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row["id_libros"], row["isbn"], row["titulo"], row["autor"], row["leidom"], row["leidoa"], row["portada"], row["resumen"], row["categoria"], row["fechapublicacion"], row["editorial"], row["paginas"], row["comentario"]))
# #print(df)
conn.commit()
conn.close()