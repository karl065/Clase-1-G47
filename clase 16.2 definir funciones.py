def calcular(precio, descuento):
    return precio - (precio * descuento / 100)

precio_1 = int(input("Ingrese un precio: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))

print(calcular(precio_1, porcentaje_descuento))