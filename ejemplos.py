import tkinter as tk

app = tk.Tk()
app.geometry("800x800")

def callback(event):
    label["text"] = "You pressed Enter"

app.bind('<Return>', callback)

boton_enter = tk.Button(app, text = "Enter", width = 2, height = 2, command = lambda: callback())

label = tk.Label(app, text="")
label.pack()

app.mainloop()