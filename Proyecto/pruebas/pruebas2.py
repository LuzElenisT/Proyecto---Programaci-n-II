from tkinter import ttk
from tkinter import *
"""class Pr:
    def __init__(self) -> None:
        self.pruf = "x"
    def set_pruf(self,n):
        self.pruf = n   
def aceptar():
    try:
        n = int(var_texto.get())  # Obtenemos el número de la StringVar
    except ValueError:            # Si lo ingresado no es un entero
        var_lbl.set(f"No escogiste un número válido")
        
    else:                         # Si lo ingresado es un entero
        var_lbl.set(f"Escogiste el número: {n}")       
        print(f.pruf)

root = tk.Tk()

var_texto = tk.StringVar()
var_lbl = tk.StringVar()

mi_label = tk.Label(root, textvariable=var_lbl)
var_lbl.set("Escoge un número") # Contenido inicial del Lable
mi_label.grid(row=0, column=0, columnspan=3)
f = Pr()
cuadro_texto = tk.Entry(root, textvariable=var_texto)
cuadro_texto.grid(row=1, column=0, columnspan=2)
f.set_pruf(var_texto.get())
btn_aceptar = tk.Button(root, text="Aceptar", command=aceptar)
btn_aceptar.grid(row=1, column=2)

root.mainloop()"""
app = Tk()
f = Frame(app,bg="yellow",width=50,height=50)
f.grid(row=0,column=0,sticky="NW")
f.grid_propagate(0)
f.update()
l = Label(app,text="123",bg="yellow")
l.place(x=25, y=25, anchor="center")
app.mainloop()