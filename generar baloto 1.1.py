import random

while (True):

    balotas = list(range(1, 44))
    super_balota = list(range(1, 17))
    
    balotas_a_apostar = []
    super_balota_a_apostar = []
    
          
    for i in range(5):
        def balotas_apostar(): 
            balota_random = random.choice(balotas)
            if balota_random not in balotas_a_apostar:    
                balotas_a_apostar.append(balota_random)
            else:
                balotas_apostar()
                
        balotas_apostar()

    

    for i in range(1):
        super_balota_random = random.choice(super_balota)
        super_balota_a_apostar.append(super_balota_random)
 

    balotas_a_apostar = str(balotas_a_apostar)[1: -1]
    super_balota_a_apostar = str(super_balota_a_apostar)[1: -1]

   
    print('Tus numeros ganadores de Baloto son: ' + balotas_a_apostar.replace(",", ""))
    print("Tu super Balota ganadora es: " + super_balota_a_apostar.replace(",", ""))
   
    menu = """
    !Desea generar otro numero de Suerte¡:
    [1] Si
    [2] No
    """ 
    print(menu)
    while (True):
        opcion = input("Ingrese una Opcion: ")
        if opcion == "1":
            break
        elif opcion == "2":
            break
        else:
            print("Opcion erronea, seleccione si o no")
            print("x" * 34)
            print(menu)
    if opcion == "1":
        continue
    elif opcion == "2":
        break
        
        