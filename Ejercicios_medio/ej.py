# Dado un número natural x, muestra su último dígito.
x = int(input("Ingresa número: "))
if x>= 0:
 last = x % 100
 print("El último dígito es: ", last)
else:
          print("mayor a 0")


print("\n")
a = input("Ingresa #: ")
if a.isnumeric():
          print("Last: ", a[-1])
else:
    print("Just numbers")