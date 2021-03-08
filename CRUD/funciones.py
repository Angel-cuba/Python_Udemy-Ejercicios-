import sqlite3


def conection():
     try:
          db = sqlite3.connect("Base.db")
          return db, db.cursor()
     except:
          print("No se pudo establecer la conexión")


def create():
     db, cursor = conection()


     nombre = input("Ingresa nombre: ")
     apellido = input("Ingresa apellido: ")
     dni = input("Ingresa dni: ")
     nacimiento = input("Ingresa nacimiento: ")

     if (nombre.isalpha() and
          apellido.isalpha() and
          dni.isnumeric() and
          # nacimiento.isnumeric() and
          5 <= len(dni) <= 8 and    
          3 <= len(nombre) <= 50 and
          3 <= len(apellido) <= 50
     ):
          cursor.execute(
               "INSERT INTO Personas(nombre,apellido, dni, nacimiento) VALUES(?, ?,?,?)", 
               (nombre, apellido, dni, nacimiento)
               # db.session.commit()
          )
          cursor.close()
          db.commit()
          print(f"{nombre} {apellido} ha sido ingresado con éxito!")
     else:
          print("ERROR: Ingresa los datos correctamente")
     #conexión finalizada
     db.close()

def getUser():
     db, cursor = conection()
     id = input("Ingresa id: ")

     if id.isnumeric():
          cursor.execute(f"SELECT * FROM Personas WHERE id ={id}")
          # print(f"Datos: {cursor.fetchone()}")
          dato = cursor.fetchone()
          cursor.close()
          db.close()
          if dato is not None:
               # print("error")
               print(f"Datos: {dato}")
          else:
               print(f"Id number: {id} is not found")
     else:
          print("ERROR: Ingresa ID válido")

def getAll():
     db, cursor = conection()
     cursor.execute(f"SELECT * FROM Personas")
     print(cursor.fetchall())
     cursor.close()
     db.close()

def upDate():
     db, cursor = conection()
     dato = getUser(cursor)
     if dato:
          nombre = input("Ingresa el nuevo nombre: ")
          apellido = input("Ingresa el nuevo apellido: ")
          cursor.execute(f"UPDATE Personas SET nombre='{nombre}',apellido='{apellido}' WHERE id={dato[0]}")
          db.commit()
     cursor.close()
     db.close()
     
def deleteUser():
     db, cursor = conection()
     dato = getUser()
     if dato:
          cursor.execute(f"DELETE FROM Personas WHERE id={dato[0]}")
          db.commit()

     cursor.close()
     
     db.close()