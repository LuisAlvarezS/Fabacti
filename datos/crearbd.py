import sqlite3

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("fabacti.db")
cursor = conn.cursor()

# cursor.execute("""
#                 DROP TABLE "indicadores"
#                 """)
               
# # Crear tabla dtf
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS "dtf" (
# 	"iddtf"	INTEGER NOT NULL UNIQUE,
# 	"fechainicio"	TEXT,
# 	"fechafin"	INTEGER,
# 	"valor"	REAL,
# 	PRIMARY KEY("iddtf" AUTOINCREMENT)
# );
# """)

# # Crear tabla de eventos
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS "eventos" (
# 	"id_evento"	INTEGER NOT NULL UNIQUE,
# 	"fecha"	TEXT,
# 	"evento"	TEXT,
# 	PRIMARY KEY("id_evento" AUTOINCREMENT)
# );	
# """);

# # Crear table usuarios
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS "usuarios" (
# 	"id"	INTEGER NOT NULL UNIQUE,
# 	"nombre"	TEXT NOT NULL UNIQUE,
# 	"clave"	TEXT NOT NULL UNIQUE,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# );
# """);

# # Crea tabla de valores indicadores
# cursor.execute("""
# CREATE TABLE "valores_indicadores" (
# 	"id_valor_indicador"	INTEGER NOT NULL UNIQUE,
#     "indicador" TEXT,
# 	"fechainicio"	TEXT,
# 	"fechafin"	INTEGER,
# 	"valor"	REAL,
# 	PRIMARY KEY("id_valor_indicador" AUTOINCREMENT)
#  );
#   """)

# cursor.execute("""
#     CREATE TABLE "indicadores" (
#  	"id_indicador"	INTEGER NOT NULL UNIQUE,
#  	"indicador"	TEXT,
#      "unidad"	TEXT,
#  	"descripcion"	TEXT,
#  	"periodicidad"	TEXT,
#  	PRIMARY KEY("id_indicador" AUTOINCREMENT)
#  );
#   """)

# cursor.execute("""
#     DROP TABLE "valores_indicadores"
#           """)


cursor.execute("""
               CREATE TABLE "libros" (
	"id_libros"	INTEGER NOT NULL UNIQUE,
	"isbn"	TEXT,
	"titulo"	TEXT,
	"autor"	TEXT,
	"leidom"	TEXT,
	"leidoa"	TEXT,
	"portada"	TEXT,
	"resumen"	TEXT,
	"categoria"	INTEGER,
	"fechapublicacion"	TEXT,
	"editorial"	TEXT,
	"paginas"	INTEGER,
	"comentario"	TEXT,
	PRIMARY KEY("id_libros" AUTOINCREMENT)
)
               """)

conn.commit()
conn.close()
