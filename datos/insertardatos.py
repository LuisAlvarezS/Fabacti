import sqlite3
#from tkinter import INSERT

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("fabacti.db")

cursor = conn.cursor()

#cursor.execute("insert into indicadores (indicador, unidad, descripcion, periodicidad) values ('DTF', 'Porcentaje', 'Tasa de Interés de Depósitos a Término Fijo', 'Semanal')")

# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('TRM', '20260714', '20260714',3248.87)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('TRM', '20260713', '20260713',3248.87)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('TRM', '20260712', '20260712',3248.87)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('TRM', '20260710', '20260710',3305.38)");

# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251013', '20251019', 8.67)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20250929', '20251005', 8.75)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20250922', '20250928', 8.76)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20250915', '20250921', 8.78)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251020', '20251026', 8.65)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251027', '20251102', 8.63)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251103', '20251109', 8.7)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251124', '20251130', 8.65)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251201', '20251207', 8.65)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251208', '20251214', 8.8)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20251215', '20251221', 8.86)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260105', '20260111', 8.98)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260112', '20260118', 8.89)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260119', '20260125', 8.95)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260126', '20260201', 9.02)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260202', '20260208', 9.15)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260209', '20260215', 9.28)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260216', '20260222', 9.45)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260223', '20260301', 9.59)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260302', '20260308', 9.7)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260309', '20260315', 9.79)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260316', '20260322', 9.82)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260323', '20260329', 9.87)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260413', '20260419', 10.01)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260420', '20260426', 10.1)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260427', '20260503', 10.14)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260504', '20260510', 10.22)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260511', '20260517', 9.98)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260525', '20260531', 10.05)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260629', '20260705',9.9)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260601', '20260607', 10.14)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260608', '20260614', 9.93)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260615', '20260321', 10.14)");
# cursor.execute("INSERT INTO valores_indicadores (indicador, fechainicio, fechafin, valor) VALUES ('DTF', '20260713', '20260719', 10.16)");

# # Comandos borrar registros
#cursor.execute("delete from valores_indicadores where id_valor_indicador in (39,40,41) " );
# cursor.execute("delete from valores_indicadores where indicador = 'IBR' and valor = 11.184  " );

#cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260526', 'Aniversario 42 de bodas Luz Miriam y Luis Albeiro' )");

# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260903', 'Vence SOAT FQT317')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261114', 'Cumpleaños Ana Carolina Alvarez Builes')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260727', 'Cumpleaños Juan David Alvarez Builes')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260516', 'Cumpleaños Luz Miriam Builes Zapata')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261213', 'Cumpleaños Luis Albeiro Alvarez Sierra')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261022', 'Cumpleaños Juan Cartlos Escobar Gaviria')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260610', 'Cumpleaños Matias Escobar Alvarez')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20261228', 'Cumpleaños Samuel Escobar Alvarez')");

# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260720', 'Subir a Cerro Tusa COMFAMA')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260710', 'Natacion COMFAMA La Estrella')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260717', 'Natacion COMFAMA La Estrella')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260724', 'Natacion COMFAMA La Estrella')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260731', 'Natacion COMFAMA La Estrella')");

# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260807', 'Natacion COMFAMA La Estrella')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260814', 'Natacion COMFAMA La Estrella')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260821', 'Natacion COMFAMA La Estrella')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260828', 'Natacion COMFAMA La Estrella')");
# cursor.execute("INSERT INTO eventos (fecha, evento) VALUES ('20260904', 'Natacion COMFAMA La Estrella')");

# cursor.execute("UPDATE libros SET autor = 'Sin autor' where titulo = 'Fabulas Colombianas'");
# cursor.execute("UPDATE libros SET autor = 'Rhonda Byme' where titulo = 'El secreto'");
# cursor.execute("UPDATE libros SET autor = 'Robin Norwood' where titulo = 'Las mujeres que aman demasiado'");


cursor.execute("UPDATE usuarios SET nombre  = 'Luz Miriam Builes Zxapata' where id = 3")

# cursor.execute(
#             "INSERT INTO usuarios (nombre, clave, correo) VALUES (?, ?, ?)",
#             ("admin", hashed.decode("utf-8", "albeiro.alvarez.sierra@gmail.com"))
#         )


conn.commit()
conn.close()