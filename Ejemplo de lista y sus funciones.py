dispositivos = ["computadores", "Celulares", "camaras"] #Listas de ejemplo, los indices se cuentan desde 0 en adelante, para el caso 0 = computadores
herramientas = ["destornilladores", "cautin", "sopladora"] #Listas de ejemplo, los indices se cuentan desde 0 en adelante, para el caso 0 = destornilladores

print(dispositivos, herramientas)

dispositivos.append(input("Ingrese dispositivo nuevo: ")) # Agrega un elemento nuevo al final de la lista
herramientas.append(input("Ingrese herramienta nueva: ")) # Agrega un elemento nuevo al final de la lista
herramientas.extend(input("Ingrese una nueva herramienta: ")) # Agrega elementos nuevos al final de la lista, si es un texto divide cada letra como un elemento
dispositivos.insert(1, input("Ingrese un dispositivo nuevo: ")) #Este método inserta el elemento x en la lista, en el índice i.

print("Dispositivos: ", dispositivos) 
print("Herramienta: ", herramientas)
print("camaras ->", dispositivos.count("camaras")) # Realiza un conteo del elemento que referencia, dentro de la lista
print("cautin -> ", herramientas.count("cautin")) # Realiza un conteo del elemento que referencia, dentro de la lista
print(dispositivos.index("Celulares")) #Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.
print(dispositivos[1]) #Devuelve el elemento que este guardado en el indice señalado dentro de las llaves
print(dispositivos.index("camaras", 1)) #El método admite como argumento adicional un índice inicial a partir de donde comenzar la búsqueda, opcionalmente también el índice final.
print(herramientas.pop()) # Este método devuelve el último elemento de la lista, y lo borra de la misma
print(herramientas)
print(herramientas.pop(8)) # Se puede indicar el indice que se quiere del elemento que se quiere borrar
print(herramientas)
herramientas.remove("t") # Este método recibe como argumento un elemento, y borra su primera aparición en la lista.
print(herramientas)
herramientas.reverse() # Este método invierte el orden de los elementos de una lista.
print(herramientas)
herramientas.sort() # Este método ordena los elementos de una lista.
print(herramientas)
