numero = int(input("Dame número: "))

if numero > 0:
# Ciclo while
          i = 1
          while i <= numero:
                    if i % 2 != 0:
                              print(i, end=", ")
                    i += 1
          # Ciclo for
          print("\n")
          for i in range(1, numero):
                    if i % 2 != 0:

                              print(i, end="-")
                                                      
else:
          print("El numero debe ser mayor que 0")

# en reversa
print("\n")
if numero > 0:
          while i >= 0:
                    print(i, end=" * ")
                    i -= 1