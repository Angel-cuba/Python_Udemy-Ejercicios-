def create(db, cursor):
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
          db.commit()
     else:
          print("Ingresa los datos correctamente")

def getUser(db, cursor):
     pass