from datetime import datetime
import sqlite3
import pandas as pd

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("fabacti.db")
cursor = conn.cursor()

# # Lista de tablas en la base de datos
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# print("Tablas en la base de datos:")
# for table in tables:
#     print(table[0])

#cursor.execute("update eventos set evento = 'Aniversario 42 de bodas Luz Miriam y Luis Albeiro' where id_evento = 4")

# # Comando consulta registros eventos
# cursor.execute("select * from eventos  ")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Comando consulta registros eventos
# cursor.execute("select * from eventos  ")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


# Comando consulta registros de usuarios
cursor.execute("select * from usuarios  ")
rows = cursor.fetchall()
for row in rows:
    print(row)

# # Comando consulta registros de indicadores
# cursor.execute("select * from valores_indicadores  ")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Comando consulta registros de indicadores
# cursor.execute("select * from valores_indicadores  ")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Comando consulta registros de indicadores
# indicador = 'TRM'
# fecha = datetime.now()
# wfecha = fecha.strftime("%Y%m%d")
# #cursor.execute("select fechainicio, fechafin, valor from valores_indicadores where indicador = '" + indicador + "' and " + wfecha + " between fechainicio and fechafin")
# cursor.execute("select fechainicio, fechafin, valor from valores_indicadores where indicador = '" + indicador + "' order by fechainicio desc limit 1")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Comando consulta registros de indicadores
#cursor.execute("select * from trm  ")
#rows = cursor.fetchall()
#for row in rows:
#    print(row)

# Comando consulta indicar DTF hoy
# fecha = datetime.now()
# wfecha = fecha.strftime("%Y%m%d")
# consulta= 'select count(*) as total from valores_indicadores where  indicador = "DTF" and ' + wfecha + ' between fechainicio and fechafin' 
# df = pd.read_sql_query(consulta, conn)
# print(df.iloc[0]['total'])

# # Comando consulta registros de indicadores
# cursor.execute("select * from libros  ")
# rows = cursor.fetchall()
# for row in rows:
#      print(row)


cursor.execute("""
SELECT sql 
FROM sqlite_master 
WHERE type='table' AND name='usuarios';
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
# Cerrar la conexión
conn.close()
