print('Calculadora de potencias de numeros enteros')
while (True):
       
    numero=int(input('introducir un numero: '))
    potencia=int(input('introducir potencia: '))
    print('La potencia de:',numero,'elevado al: ', potencia, 'es:',numero**potencia)

        
    menu = """
    Seleccione una opcion para poder continuar
    [1] Continuar
    [2] Salir
    """   
    print(menu)
    while (True):
        opcion = input('digita una opcion: ')
        if opcion == '1' :
            break
        elif opcion == '2' :
             break
        else:
          print('Debes digitar una de las dos opciones')
          print('=-='*20)
          print(menu)
    if opcion == '1' :
        pass
    elif opcion == '2' :
         break
        
        