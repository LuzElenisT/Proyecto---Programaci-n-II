import clases.bus as bs
from tkinter import ttk
from tkinter import *
import sqlite3 as sql

ventana = Tk()
ventana.title("Ingresar valores")
#Ddatos del bus

datos_bus=LabelFrame(ventana, text="Datos bus", pady=30, padx=50)
datos_bus.grid(row=0,column=0)

b = bs.Bus()

n_ch = StringVar()
idbus = StringVar()

Label(datos_bus, text="Nombre chofer: ").grid(row=1, column=0)
Entry(datos_bus, textvariable=n_ch).grid(row=1, column=1)
b.set_nombre_chofer(n_ch.get())

Label(datos_bus, text="id del bus: ").grid(row=2, column=0)
Entry(datos_bus, textvariable=idbus).grid(row=2, column=1)
b.set_bus_num(idbus.get())

def mostrar():
    b.set_nombre_chofer(n_ch.get())
    b.set_bus_num(idbus.get())
    print(b.bus_num)
    print(b.nombre_chofer)

Button(ventana, text="registrar", command=mostrar).grid(row=3, column=0)

ventana.mainloop()