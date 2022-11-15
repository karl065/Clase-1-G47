
def agregar(productos, producto):
    if producto[0] in productos:
        return False
        
    llave = producto[0]
    producto.pop(0)
    
    productos[llave] = producto
     
    return True

def borrar(productos, producto):
    if not producto[0] in productos:
        return False
    productos.pop(producto[0])
    
    return True

def actualizar(productos, producto):
    if not producto[0] in productos:
        return False
    
    llave = producto[0]
    producto.pop(0)
    
    productos[llave] = producto
    
    return

def leer_datos():
    operacion = input()
    producto = input().split()
    producto[0] = int(producto[0])
    producto[2] = float(producto[2])
    producto[3] = int(producto[3])
    return operacion, producto


def principal ():
    productos = {
            1: ['Manzanas', 5000.0, 25],
            2: ['Limones', 2300.0, 15],
            3: ['Peras', 2700.0, 33],
            4: ['Arandanos', 9300.0, 5],
            5: ['Tomates', 2100.0, 42],
            6: ['Fresas', 4100.0, 3],
            7: ['Helado', 4500.0, 41],
            8: ['Galletas', 500.0, 8],
            9: ['Chocolates', 3500.0, 80],
            10: ['Jamon', 15000.0, 10] 
        }

    operacion, producto = leer_datos()
    
    if operacion == "AGREGAR":
        flag = agregar(productos, producto)
            
    elif operacion == "BORRAR":
        flag = borrar(productos, producto)
            
    elif operacion == "ACTUALIZAR":
        flag = actualizar(productos, producto)
    
    if flag:
        print("dato correcto")
    else:
        print("ERROR")

def impresion_salidas(productos):
    
    
        
    
    return


principal()
impresion_salidas()