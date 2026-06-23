import sqlite3

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("fabacti.db")
cursor = conn.cursor()

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

# Crear table usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS "usuarios" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL UNIQUE,
	"clave"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
""");

conn.commit()
conn.close()