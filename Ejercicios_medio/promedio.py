# Calcular promedio en una lista
n = int(input("Ingresa: "))
sum = 0
for i in range(n):
          x = int(input("Ingresa número: "))
          sum += x
print("el promedio es: ", sum/n)

print("\n")
#############
lista = []
m = int(input("Ingresa cantidad: "))
for i in range(m):
          c = int(input(f"Ingresa {m} numero: "))
          lista.append(c)
suma = 0
for item in lista:
          suma += item
print("promedio es: ", suma/n)

#############################
print("\n")
from statistics import mean

lista = []
m = int(input("Ingresa cantidad: "))
for i in range(m):
          c = int(input(f"Ingresa {m} numero: "))
          lista.append(c)
print("El promedio es: ", mean(lista))