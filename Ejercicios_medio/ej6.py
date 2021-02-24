a = []
b = []


n = int(input("Ingresa número de A: "))
for i in range(n):
          x = int(input("Ingresa número: "))
          a.append(x)

m = int(input("Ingresa número de B: "))
for i in range(m):
          y = int(input("Ingresa número: "))
          b.append(y)
mayor_a = max(a)
if mayor_a in b:
          print("El mayor de A está en B")
else:
          print("El mayor de A no está en B")


########## Mostrar el mayor de los dígitos
mayor = -1
numero = int(input("Dame número: "))
while numero > 0:
          if numero % 10 > mayor:
                    mayor = numero % 10
          numero = numero // 10
print("El mayor es: ", mayor)

################################################################
mayor = -1
numero = int(input("Ingresa número---:"))
print("El mayor es: ", max(numero))