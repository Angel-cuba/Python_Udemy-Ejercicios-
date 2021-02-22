numero = int(input("Dame número: "))

triangulo = "*"
i = 0

while i < numero:
          print(triangulo)
          triangulo += "*"
          i += 1

print("\n")

triangulo = "*"
for rep in range(numero):
          print(triangulo)
          triangulo += "*"