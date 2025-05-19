import math

# Función que saluda con un nombre
def bienvenida(nombre):
    return f"¡Hola, {nombre}! Bienvenido/a."

# Función que calcula el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Ejemplo de uso
nombre_usuario = input("Ingrese su nombre: ")
print(bienvenida(nombre_usuario))

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {area_circulo(radio):.2f}")
