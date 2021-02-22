i = 1
while i<=10:
          print(f"{i} * 10 = {i*10}")
          i += 1

print("\n")          

palabra = input("Dame palabra: ")

largo = len(palabra)-1

while largo >= 0:
          print(palabra[largo])
          largo -=1

print("\n")


frase = input("Dame frase: ")
letra = input("Dame letra: ")

contador = 0
largo = len(frase)
i = 0
while i < largo:
          if frase[i] == letra:
                    contador += 1
          i += 1
print(f"Letra {letra} aparece {contador} veces")   
print("\n")
contador = 0
for item in frase:
    if item == letra:
        contador += 1
print("L aletra ingresada aparece", contador, "veces")      