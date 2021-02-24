# Dados los números, A, B Y C, mostrar los múltiplos de A, menores que B y que no sean
#divisores de C

a = int(input("Ingresa número A: "))
b = int(input("Ingresa número B: "))
c = int(input("Ingresa número C: "))

for i in range(1, a+1):
          result = a % i
          if result == 0 and i < b and c % i != 0:
                    print("El número que cumple es:", i)
          if result == 0 and i < b and c % i == 0:
                    print("El número que-----:", i)
          else:
                    print("No hay número")