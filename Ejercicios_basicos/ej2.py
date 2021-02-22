edad = int(input("Ingresa edad: "))
if edad >= 18:
          print("Eres mayor de edad")

else:
    print("Eres menor de edad")

print("**********__10__**************")
rep = 0
limit = int(input("Dame numero de limite: "))
texto= input("Dame un texto: ")
while(limit > rep):
          print(rep, "---", texto)
          rep += 1
          if rep == limit:
                    print("End")
                    break

print("**************************3**")
##ciclo for
for i in range(limit):
          a= input("Dame un ejemplo: ")
          print(texto, f"Este es el ejemplo {a} ")
          if a=="ya":
                    print("Final")
                    break  

print("**********")

numero = int(input("Ingresa número:"))

if numero % 2 == 0:
          print("Es par")
else:
    print("Impar")