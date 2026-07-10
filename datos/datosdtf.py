import sqlite3
from tkinter import INSERT

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("fabacti.db")

cursor = conn.cursor()

# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251006', '20251012', 8.75)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251013', '20251019', 8.67)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20250929', '20251005', 8.75)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20250922', '20250928', 8.76)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20250915', '20250921', 8.78)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251020', '20251026', 8.65)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251027', '20251102', 8.63)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251103', '20251109', 8.7);");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251124', '20251130', 8.65)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251201', '20251207', 8.65)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251208', '20251214', 8.8)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20251215', '20251221', 8.86)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260105', '20260111', 8.98)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260112', '20260118', 8.89)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260119', '20260125', 8.95)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260126', '20260201', 9.02)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260202', '20260208', 9.15)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260209', '20260215', 9.28)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260216', '20260222', 9.45)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260223', '20260301', 9.59)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260302', '20260308', 9.7)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260309', '20260315', 9.79)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260316', '20260322', 9.82)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260323', '20260329', 9.87)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260413', '20260419', 10.01)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260420', '20260426', 10.1)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260427', '20260503', 10.14)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260504', '20260510', 10.22)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260511', '20260517', 9.98)");
# cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260525', '20260531', 10.05)");

cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260629', '20260705', 9.9)");
cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260601', '20260607', 10.14)");
cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260608', '20260614', 9.93)");
cursor.execute("INSERT INTO dtf (fechainicio, fechafin, valor) VALUES ('20260615', '20260621', 10.14)");

conn.commit()
conn.close()