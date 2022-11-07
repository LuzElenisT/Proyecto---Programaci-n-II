from tkinter import ttk
from tkinter import *
import sqlite3 as sql
import clases.bus as bs

ventana = Tk()

ventana.title("Ingresar valores")
#Marco de datos del bus
n_ch = StringVar()
idbus =StringVar()
datos_bus=LabelFrame(ventana, text="Datos bus", pady=30, padx=50)
datos_bus.grid(row=0,column=0)
Label(datos_bus, text="Nombre chofer: ").grid(row=1, column=0)
v1=Entry(datos_bus, textvariable=n_ch).grid(row=1, column=1)
Label(datos_bus, text="id del bus: ").grid(row=2, column=0)
v2=Entry(datos_bus).grid(row=2, column=1)
"""#Datos Parada
valor = StringVar()
datos_pr=LabelFrame(ventana, text="Datos parada", pady=30, padx=50)
datos_pr.grid(row=1,column=0)
Label(datos_pr, text="lugar parada: ").grid(row=1, column=0)
lp= OptionMenu(datos_pr, valor, 'Valledupar', 'Universidad', 'Manaure', 'La Paz', 'Codazzi', 'San Diego')
lp.grid(row=1,column=1)
#fecha y hora
datos_fyh=LabelFrame(ventana, text="Fecha y Hora", pady=30, padx=50)
datos_fyh.grid(row=2,column=0)
Label(datos_fyh, text="Fecha:").grid(row=1, column=0)
fch=Entry(datos_fyh).grid(row=1, column=1)
Label(datos_fyh, text="Hora de llegada:").grid(row=2, column=0)
hll=Entry(datos_fyh).grid(row=2, column=1)
Label(datos_fyh, text="Hora de salida:").grid(row=3, column=0)
hs=Entry(datos_fyh).grid(row=3, column=1)
"""
ventana.mainloop()