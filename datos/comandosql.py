import sqlite3

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("fabacti.db")
cursor = conn.cursor()

#cursor.execute("update eventos set evento = 'Aniversario 42 de bodas Luz Miriam y Luis Albeiro' where id_evento = 4")

# # Comando consulta registros
# cursor.execute("select * from eventos  ")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# Comando consulta registros
cursor.execute("select * from usuarios  ")
rows = cursor.fetchall()
for row in rows:
    print(row)


# # Comandos borrar registros
#cursor.execute("delete from eventos where id_evento >= 13 ")

#cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260526', 'Aniversario 42 de bodas Luz Miriam y Luis Albeiro' )");

# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260903', 'Vence SOAT FQT317')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261114', 'Cumpleaños Ana Carolina Alvarez Builes')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260727', 'Cumpleaños Juan David Alvarez Builes')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260516', 'Cumpleaños Luz Miriam Builes Zapata')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261213', 'Cumpleaños Luis Albeiro Alvarez Sierra')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261022', 'Cumpleaños Juan Cartlos Escobar Gaviria')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260610', 'Cumpleaños Matias Escobar Alvarez')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261228', 'Cumpleaños Samuel Escobar Alvarez')");

#conn.commit()
# Cerrar la conexión
#conn.close()
