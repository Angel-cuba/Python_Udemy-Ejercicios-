# #Dado un número natural, sumar sus digitos

# x = int(input("Ingresa número: "))

# suma = 0

# while x > 0:
#           digito = x % 10
#           suma += digito
#           x = x//10
#           print("Suma: ", suma)

# Python
x = input("Ingresa número: ")
suma = 0
for digit in x:
          suma += int(digit)
          print("Suma: ", suma)

# Di si es capicua........Noooooooooooooooooooooooooooooooooo
y = input("Ingresa número: ")
primer = y
capicua = 0

if y[0] == y[-1]:
          print("iguales")
else:
    print("repite")