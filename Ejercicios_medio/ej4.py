#Dado un número natural, mostrar sus N potencias
x = int(input("Dame un numero: "))
n = int(input("Ingresa n(potencia): "))

c= 0
while c <= n:
          print(f"{x} ** {c} = ", x**c)
          #  print(f"{x} ** {c} =  {x**c}")
          c += 1

# con el for    
for c in range(n):
          print(f"{x} ** {c} ={x ** c}")

##Dado un número natural, mostrar todos sus divisores

y = int(input("Ingresa número: "))

a = 1

print("Divisores: ", end=" ")
while a < y:
          if y % a == 0:
                    print(a, end=" ")
          a += 1

# Dada una lista de numeros, mostrar el mayor de ellos
print("\n")
N = int(input("Ingresa la cantidad de numeros: "))
aux = -1

for v in range(N):
          v = int(input("Ingresa los números: "))
          if v > aux:
                    aux = v
print("El mayor es: ", aux)

########Con una lista
lista= []
b = int(input("Ingresa cantidad: "))
for item in range(b):
          b_lista = int(input("Dame numeros: "))
          lista.append(b_lista)
aux1 = -1
for item in lista:
              if item > aux1:
                            aux1 = item
print(lista)
print("El mayor es :", aux1)    