from tkinter import *

salario = Tk()
salario.title("Calculadora de Salario")
salario.iconbitmap("pesos.ico")
salario.geometry("800x800")
salario.config(bg = "blue")

enunciado1 = Tk.Label(salario, text="Ingrese salario base", bg = "black", fg = "white")
enunciado1.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = Tk.X)
entrada_salario = Tk.E
entrada_salario.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = Tk.X)


Salario_base = float(input())
Horas_extras = int(input())
Bonificaciones = int(input())
valor_Hora_normal = Salario_base / 192
valor_Hora_Extra = float((Horas_extras * valor_Hora_normal) * 1.25)
valor_bonificaciones = float(Salario_base * 0.05)

salario_neto = Salario_base + valor_Hora_Extra

if Bonificaciones == 1:
    salario_total = salario_neto + valor_bonificaciones
if Bonificaciones == 0:
    salario_total = salario_neto  

salud = salario_total * 0.035 
pension = salario_total * 0.04 
Caja = salario_total * 0.01

Deducciones = salud + pension + Caja 
Total_a_pagar = round(salario_total - Deducciones , 1)

       
print(Total_a_pagar)    

salario.mainloop()