import sqlite3 as sql
import paradas as pr
import bus as bs
import Horario as hr
import fecha as fc
from tkinter import ttk
from tkinter import *


ventana = Tk()

ventana.title("Ingresar valores")
#Marco de datos del bus
var = StringVar()
datos_bus=LabelFrame(ventana, text="Datos bus", pady=30, padx=50)
datos_bus.grid(row=0,column=0)
Label(datos_bus, text="Nombre chofer: ").grid(row=1, column=0)
b = bs.Bus()
n_ch= Entry(datos_bus, textvariable=var).grid(row=1, column=1)
b.set_nombre_chofer(var.get())
def ingresar():
    b.set_nombre_chofer(var.get())
    b.insertardatos()


boton = Button(ventana, text='registrar', command=ingresar ).grid(row=1,column=0)
ventana.mainloop()