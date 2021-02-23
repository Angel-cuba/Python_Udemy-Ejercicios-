#Dado una lista de numeros, demuestra cuál es el menor
lista = []
n = int(input("Dame la cantidad: "))

for i in range(n):
          lista1 = int(input("Numeros:    "))
          lista.append(lista1)
aux1 = 999999999999999999999999999999999999999999
for item in lista:
              if item < aux1:
                        aux1 = item    
print(lista)
print("el menor es: ", aux1)  

print("\n")
print(f"E menor es---------- {min(lista)}")
print(f"El mayor es ---------{max(lista)}")