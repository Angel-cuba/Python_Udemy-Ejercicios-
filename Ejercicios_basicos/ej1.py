nombre = input("Ingresa nombre: ")
print(nombre.capitalize())
print(nombre.upper())
print(len(nombre))

print("***__6__***************************")
horas =int(input("Horas: "))
costo = int(input("Costo: "))

result = horas *costo

print("El pago es: ", result)

print("**************__7__******************")
valor_producto = int(input("ValorProducto: "))
iva = (valor_producto*21)/100
final= valor_producto + iva

print(f"El valor final es : {final}")

print("**************___8__***********************")

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
          print(f"{n1} es mayor que {n2}")
elif n1 == n2:
          print("Son iguales")               
else:
          print(f"{n1} es menor que {n2}")    