#Contar la cantidad de numeros
x = int(input("Dame: "))

c = 0
if 0 <= x < 10:
              print("Cantidad es: 1")
else:
          while x > 0:
                    c += 1
                    x = x // 10
          print("Cantidad es: ", c)

#Forma de hacer en Python
a = input(" Otro: ")
if a.isnumeric():
    print("Cantidad es:", len(a))   

################################################################
#Dado un numero natural, contar la cantidad de dígitos pares e impares

x = int(input("Ingresa número: "))

pares = 0
impares = 0

if x>=0:
    while x > 0:
          digit = x % 10
          if digit % 2 == 0:
                    pares += 1
                    
          else:
              impares += 1
        
print("Pares: ", pares)
print("Impares: ", impares)