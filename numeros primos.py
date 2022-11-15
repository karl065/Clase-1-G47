def num_primo():
    n = int(input("inserte un numero: "))
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                print("No es primo")
                return False
        print("Es primo")
        return True
    else:
        print("Ingrese un numero mayor que 1")
        num_primo()
        
if __name__ == '__main__':
    while(True):
        num_primo()
    
