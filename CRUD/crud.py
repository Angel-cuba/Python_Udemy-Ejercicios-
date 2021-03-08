import sqlite3
from funciones import (create, getUser)


db = sqlite3.connect("Base.db")
cursor = db.cursor()

print("Starting CRUD")
while True:
     print("""
     [1] Crea un nuevo registro
     [2] Obten un registro
     [3] Obten los registros
     [4] Actualizar el registro
     [5] Borra el registro
     [6] Salir del CRUD
     """)
     opcion = input("Ingresa una opcion: ")
     if opcion.isnumeric():
          # if opcion.isnumeric():
               if opcion == "1":
                    create(db, cursor)
     else:
          print("Ingresa un número de opción válido")
     

     # Obtener un registro
     opcion = input("Ingresa una opción: ")

     if opcion.isnumeric():
          if opcion == "2":
               getUser(db, cursor)
          else:
               print("Ingresa un número de opción válido")


cursor.close()