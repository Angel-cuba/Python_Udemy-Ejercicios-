nombre = input("Ingresa nombre: ")
numero = int(input("Numero: "))

#Concatenando un salto de linea
print((nombre + "\n")* numero)

# Ciclo while
print("************************************************")
while (numero > 0):
          print(nombre)
          numero -= 1

# Ciclo for
print("************************************************")
for i in range(numero):
          print(nombre)

print("************************************************")
print(nombre.capitalize())