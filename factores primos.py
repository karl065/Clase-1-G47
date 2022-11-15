primos = []

def num_primo():
    
def obtener_primos():
    n = int(input("inserte un numero: "))
    while n >= 0:
        contador = n
        x = n
        while contador >= 0:
            if n % contador == 0:
                x = x - 1
            contador = contador - 1
        
            for i in range(2, n):
                if n % i == 0:
                    print("No es primo")
                    return False
            primos.append(n)
            return True
    else:
        print("Ingrese un numero mayor que 1")
        num_primo()
        
if __name__ == '__main__':
    while(True):
        num_primo()