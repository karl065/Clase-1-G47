# Horas Extras

Horas_trabajadas = input("Introducir Horas Trabajadas: ")
Precio_por_hora = input("Precio por hora: ")

if Horas_trabajadas <= 40:
    tiempo_pagado = Horas_trabajadas * Precio_por_hora
else:
    horas_extras = Horas_trabajadas - 40
    if horas_extras <= 8:
        precio_extras = horas_extras * Precio_por_hora * 2
    else:
        pago_dia = 8 * Precio_por_hora * 2
        pago_tiempo = (horas_extras - 8) * Precio_por_hora * 3
        pago_extras = pago_dia + precio_extras
        
