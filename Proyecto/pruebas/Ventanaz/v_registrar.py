import clases.lugares as pr
import clases.bus as bs
import clases.Horario as hr
#import clases.rutas as rt
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

class Rutas:

    def __init__(self, b:bs.Bus, h:hr.Horario, l:pr.Lugar):
        self.ruta=[b.bus_num, b.nombre_chofer, l.lugar_parada, h.h_llegada, h.h_salida, h.fecha]
    def ingresarruta(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()  
        query = f"""INSERT INTO ruta(bus_num, nombre_conductor, lugar_parada, hora_llegada, hora_salida, fecha) 
                    VALUES ('{self.ruta[0]}','{self.ruta[1]}','{self.ruta[2]}','{self.ruta[3]}','{self.ruta[4]}','{self.ruta[5]}')"""
        cursor.execute(query)
        conex.commit()
        conex.close()
    def modificar_ruta(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()  
        query = f"""UPDATE paradas
                    SET bus_num = '{self.ruta[0]}'
                        nombre_conductor = '{self.ruta[1]}'
                        lugar_parada = '{self.ruta[2]}'
                        hora_llegada = '{self.ruta[3]}'
                        hora_ salida =  '{self.ruta[4]}' 
                        fecha = '{self.ruta[5]}'
                    WHERE id = """
        cursor.execute(query)
        conex.commit()
        conex.close()
    def mostrar_ruta(self):
        print(self.ruta)
    

ventana = Tk()
ventana.title("Ingresar valores")
#Ddatos del bus

datos_bus=LabelFrame(ventana, text="Datos bus", pady=30, padx=50)
datos_bus.grid(row=0,column=0)



n_ch = StringVar()
idbus = StringVar()
rt = StringVar()

def rutas():
    lista = []
    conex = sql.connect("rutas.db")
    cursor = conex.cursor()
    query = f"SELECT nombre_ruta FROM rutas"
    res = cursor.execute(query).fetchall()
    conex.commit()
    conex.close()
    for i in range(0,len(res)):
        lista.append(res[i][0])
    print(lista)
    return lista

Label(datos_bus, text="Nombre chofer: ").grid(row=1, column=0)
Entry(datos_bus, textvariable=n_ch).grid(row=1, column=1)


Label(datos_bus, text="id del bus: ").grid(row=2, column=0)
Entry(datos_bus, textvariable=idbus).grid(row=2, column=1)

Label(datos_bus, text="tipo de ruta: ").grid(row=3, column=0)
OptionMenu(datos_bus,rt, *rutas()).grid(row=3, column=1)

#Datos Parada
datos_pr=LabelFrame(ventana, text="Datos parada", pady=30, padx=50)
datos_pr.grid(row=1,column=0)



lp = StringVar()

Label(datos_pr, text="lugar parada: ").grid(row=1, column=0)
OptionMenu(datos_pr, lp, 'Valledupar', 'Universidad', 'Manaure', 'La Paz', 'Codazzi', 'San Diego').grid(row=1,column=1)


#fecha y hora
datos_fyh=LabelFrame(ventana, text="Fecha y Hora", pady=30, padx=50)
datos_fyh.grid(row=2,column=0)



fch = StringVar()
fch.set(hr.Horario().fecha_str)
hll = StringVar()
hs = StringVar()

Label(datos_fyh, text="Fecha:").grid(row=1, column=0)
x =Entry(datos_fyh, textvariable=fch,).grid(row=1, column=1)



Label(datos_fyh, text="Hora de llegada:").grid(row=2, column=0)
Entry(datos_fyh, textvariable=hll).grid(row=2, column=1)


Label(datos_fyh, text="Hora de salida:").grid(row=3, column=0)
Entry(datos_fyh, textvariable=hs).grid(row=3, column=1)

def ponerid(ruta:str):
    conex = sql.connect("rutas.db")
    cursor = conex.cursor()
    query = f"SELECT id FROM rutas WHERE nombre_ruta = '{ruta}'"
    res = cursor.execute(query).fetchall()
    conex.commit()
    conex.close()
    print(res[0][0])
    return res[0][0]  


def registro():

    b = bs.Bus()
    b.set_nombre_chofer(n_ch.get())
    b.set_bus_num(idbus.get())

    p =pr.Lugar()
    p.set_lugar_parada(lp.get()) 

    h = hr.Horario()
    h.set_fecha(fch.get())
    h.set_h_llegada(hll.get())
    h.set_h_salida(hs.get())

    rut = ponerid(rt.get())
    r = Rutas(b,h,p)

    r.ingresarruta()
    print(messagebox.showinfo(message="Datos registrados con éxito"))
    ventana.destroy()
boton = Button(ventana, text="registrar", command=registro).grid(row=3, column=0)

ventana.mainloop()



