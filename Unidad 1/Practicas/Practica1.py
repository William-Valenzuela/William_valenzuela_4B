#Diagnostico_nombre.py
#Simulador de pedidos
#Conceptos basicos: variables, imputs, condicionales, funciones y bucles

#Elegir una tematica de tienda y escribir 3 productos
productos = ["latte", "Capuchino", "Americano"]
precios = [50, 70, 40]

#Funciones para calcular total
def calcular_total(cantidad, precios):
    total = 0
    for i in range(len(cantidad)):
        total += cantidad[i] * precios[i]
    return total

#Menu para usuario (Outputs)
print("Menu de cafeteria Bienvenido")
nombre = input("ingresar nombre: ")

cantidad = []

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad_agregar = int(input(f"¿cuantos {productos[i]} deseas? "))
    cantidad.append(cantidad_agregar)

total = calcular_total(cantidad, precios)
print("Total a pagar:", total)
