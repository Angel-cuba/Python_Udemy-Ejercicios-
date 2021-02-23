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