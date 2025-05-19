# Función que calcula el precio final con descuento
def descuento(precio, porcentaje_descuento=10):
    return precio - (precio * porcentaje_descuento / 100)

# Ejemplo de uso
precio = float(input("Ingrese el precio del producto: "))
desc = input("Ingrese el porcentaje de descuento (deje vacío para usar 10%): ")

if desc:
    precio_final = descuento(precio, float(desc))
else:
    precio_final = descuento(precio)

print(f"El precio final después del descuento es: {precio_final:.2f}")
