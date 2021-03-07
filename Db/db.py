import sqlite3

db = sqlite3.connect("Base.db")
cursor = db.cursor()

# Para leer tabla Personas
# cursor.execute("SELECT * FROM Personas")

registro = ('ejemplo', 'person', 987661, '06/07/81')
# Declarar un registro
cursor.execute("INSERT INTO Personas(nombre, apellido, dni, nacimiento) VALUES(?, ?,?,?)", registro)

# cursor.execute("INSERT INTO Personas VALUES(NULL,'Aniina', 'Yarvi', '322132', '4/6/6')")

# Con esta linea se cargan los datos a la base de datos
db.commit()

# print(cursor.fetchall())




cursor.close()