
while(True):

    precio = int(input("Ingrese el precio del prducto: "))

    def descuento(precio):
        porcentaje_descuento = int(input("Ingrese en descuento: "))
        
        valor_descuento = (porcentaje_descuento * precio)/100
        descuento = precio - valor_descuento
        
        return descuento

    print(descuento(precio))