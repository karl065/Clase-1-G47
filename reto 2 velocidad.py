distancia_metros, velocidad_maxima, segundos = input().split()

distancia_metros = float(distancia_metros)
velocidad_maxima = float(velocidad_maxima)
segundos = int(segundos)

kilometros = distancia_metros/1000
hora = segundos/3600
multa = (velocidad_maxima) + (velocidad_maxima * 0.20)

km_h = kilometros / hora

if km_h <= velocidad_maxima:
    print("Ok")
if km_h >= velocidad_maxima:
    print("MULTA")
    



