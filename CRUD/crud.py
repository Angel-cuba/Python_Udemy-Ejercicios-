from funciones import create, getUser, getAll, upDate, deleteUser
# import sqlite3


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
                    create()
          # Obtener un registro 
               elif opcion == "2":
                    getUser()

          #Obtener todos los registros
               elif opcion == "3":
                    getAll()

          # Actualizar los registros
               elif opcion == "4":
                    upDate()
               
               elif opcion == "5":
                    deleteUser()

               elif opcion == "6":
                    print("Gracias")
                    break
     else:
          print("Ingresa un número de opción válido")
     


