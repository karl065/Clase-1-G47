registros = input()
registros = int(registros)

pedalier_limites = list(range(240, 301))
bielas_limites = list(range(160, 181))
sillines_limites = list(range(240, 276))
manilares_limites = list(range(51))

pedalieres_datos = []
bielas_datos = []
sillines_datos = []
manilar_datos = []
precios_datos = []

for i in range(registros):
        pedalier_mm, bielas, sillin, manilar, dolares = input().split()

        pedalier_mm = int(pedalier_mm)
        bielas = int(bielas)
        sillin = int(sillin)
        manilar = int(manilar)
        dolares = int(dolares)
        
        if pedalier_mm in pedalier_limites and bielas in bielas_limites and sillin in sillines_limites and manilar in manilares_limites:
              pedalieres_datos.append(pedalier_mm)
              bielas_datos.append(bielas)
              sillines_datos.append(sillin)
              manilar_datos.append(manilar)
              precios_datos.append(dolares)
        
        if pedalier_mm in list(range(240, 301)) and bielas in list(range(160, 181)) and sillin in list(range(240, 276)) and manilar in list(range(51)):
          print(dolares)
          

if len(pedalieres_datos) != 1 and len(bielas_datos) != 1 and len(sillines_datos) != 1 and len(manilar_datos) != 1 :
      print("NO DISPONIBLE") 
