lista = [1,2,3,1,2]

repeticiones = {}

for n in lista:
      if n in repeticiones :
        repeticiones[n] += 1
      else:
         repeticiones[n] = 0

print(repeticiones)

print(len(repeticiones))