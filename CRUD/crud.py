from funciones import create, getUser, getAll, upDate, delete_person
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
                    create(db, cursor)
          # Obtener un registro 
               elif opcion == "2":
                    getUser(cursor)

          #Obtener todos los registros
               elif opcion == "3":
                    getAll(cursor)

          # Actualizar los registros
               elif opcion == "4":
                    upDate(db,cursor)
               
               elif opcion == "5":
                    delete_person(db, cursor)

               elif opcion == "6":
                    cursor.close()
                    print("Gracias")
                    break
     else:
          print("Ingresa un número de opción válido")
     

     # Obtener un registro
     # opcion = input("Ingresa una opción: ")

     # if opcion.isnumeric():
     #      if opcion == "2":
     #           # getUser(db, cursor)

     #           pass
     #      else:
     #           print("Ingresa un número de opción válido")


