import clases.lugares as pr
import clases.bus as bs
import clases.Horario as hr
#import clases.rutas as rt
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from clases.consulta import Consulta3 as clt3
from clases.consulta import Consulta1 as clt
class Rutas:

    def __init__(self, b:bs.Bus, h:hr.Horario, l:pr.Lugar):
        self.ruta=[b.bus_num, b.nombre_chofer, b.id_rt,l.lugar_parada, h.h_llegada, h.h_salida, h.fecha]
    def ingresarruta(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()  
        query = f"""INSERT INTO paradas (bus_num, nombre_conductor,id_ruta ,lugar_parada, hora_llegada, hora_salida, fecha) 
                    VALUES ('{self.ruta[0]}','{self.ruta[1]}','{self.ruta[2]}','{self.ruta[3]}','{self.ruta[4]}','{self.ruta[5]}','{self.ruta[6]}')"""
        cursor.execute(query)
        conex.commit()
        conex.close()
    def modificar_ruta(self, id):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()  
        query = f"""UPDATE paradas
                    SET bus_num = '{self.ruta[0]}',
                        nombre_conductor = '{self.ruta[1]}',
                        lugar_parada = '{self.ruta[3]}',
                        hora_llegada = '{self.ruta[4]}',
                        hora_salida =  '{self.ruta[5]}', 
                        fecha = '{self.ruta[6]}'
                    WHERE id = {id}"""
        cursor.execute(query)
        conex.commit()
        conex.close()
    def mostrar_ruta(self):
        print(self.ruta)

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
def ponerid(ruta:str):
    conex = sql.connect("rutas.db")
    cursor = conex.cursor()
    query = f"SELECT id FROM rutas WHERE nombre_ruta = '{ruta}'"
    res = cursor.execute(query).fetchall()
    conex.commit()
    conex.close()
    print(res[0][0])
    return res[0][0]  

class Vparadas1(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Ingresar valores")
        
        #Datos Bus

        self.lbf_1 = LabelFrame(self, text="Datos bus", pady=30, padx=50)
        self.lbf_1.grid(row=0,column=0)

        self.labl_1 =  Label(self.lbf_1, text="Nombre chofer: ")
        self.labl_1.grid(row=1, column=0)
        self.n_ch = Entry(self.lbf_1)
        self.n_ch.grid(row=1, column=1)

        self.labl_2 =  Label(self.lbf_1, text="Id\ndel bus: ")
        self.labl_2.grid(row=2, column=0)
        self.idbus = Entry(self.lbf_1)
        self.idbus.grid(row=2, column=1)

        self.rt = StringVar()
        self.labl_3 = Label(self.lbf_1, text="Tipo\nde ruta: ").grid(row=3, column=0)
        OptionMenu(self.lbf_1,self.rt, *rutas()).grid(row=3, column=1)

        #Datos Parada 

        self.lbf_2 = LabelFrame(self, text="Datos parada", pady=30, padx=50)
        self.lbf_2.grid(row=1,column=0)

        #self.lp = StringVar()
        self.labl_4 = Label(self.lbf_2, text="Lugar\nparada: ")
        self.labl_4.grid(row=1, column=0)
        #OptionMenu(self.lbf_2, self.lp, 'Valledupar', 'Universidad', 'Manaure', 'La Paz', 'Codazzi', 'San Diego').grid(row=1,column=1)
        self.lp = Entry(self.lbf_2)
        self.lp.grid(row=1,column=1)
        #fecha y hora

        self.lbf_3=LabelFrame(self, text="Fecha y Hora", pady=30, padx=50)
        self.lbf_3.grid(row=2,column=0)
        
        self.fch = StringVar()
        self.fch.set(hr.Horario().fecha_str)
        self.labl_5 = Label(self.lbf_3, text="Fecha:")
        self.labl_5.grid(row=1, column=0)
        Entry(self.lbf_3, textvariable=self.fch,).grid(row=1, column=1)

        self.labl_6 = Label(self.lbf_3, text="Hora\nde llegada:")
        self.labl_6.grid(row=2, column=0)
        self.hll = Entry(self.lbf_3)
        self.hll.grid(row=2, column=1)

        self.labl_7 = Label(self.lbf_3, text="Hora de salida:")
        self.labl_7.grid(row=3, column=0)
        self.hs = Entry(self.lbf_3)
        self.hs.grid(row=3, column=1)

        self.btn_1 = Button(self, text="Registrar", command=self.registro)
        self.btn_1.grid(row=3, column=0)

    def registro(self):

        b = bs.Bus()
        b.set_nombre_chofer(self.n_ch.get())
        b.set_bus_num(self.idbus.get())
        b.set_id_rt(ponerid(self.rt.get()))
        p =pr.Lugar()
        p.set_lugar_parada(self.lp.get()) 

        h = hr.Horario()
        h.set_fecha(self.fch.get())
        h.set_h_llegada(self.hll.get())
        h.set_h_salida(self.hs.get())

        r = Rutas(b,h,p)

        r.ingresarruta()


        print(messagebox.showinfo(message=f"Datos registrados con éxito\nid: {self._selult()}"))
        self.destroy()
    def _selult(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()
        query = "SELECT id FROM paradas ORDER BY id DESC LIMIT 1"
        hx = cursor.execute(query).fetchall()
        conex.commit()
        conex.close()
        return hx[0][0]

class Vparadas2(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Modificar Parada")

        self.lbf = LabelFrame(self, text="Id de parada",pady=30, padx=50)
        self.lbf.grid(row=0, column=0)
        self.idp = Entry(self.lbf)
        self.idp.grid(row=0, column=0)

        #Datos Bus

        self.lbf_1 = LabelFrame(self, text="Datos bus", pady=30, padx=50)
        self.lbf_1.grid(row=1,column=0)

        self.labl_1 =  Label(self.lbf_1, text="Nombre chofer: ")
        self.labl_1.grid(row=1, column=0)
        self.n_ch = Entry(self.lbf_1)
        self.n_ch.grid(row=1, column=1)

        self.labl_2 =  Label(self.lbf_1, text="Id del bus: ")
        self.labl_2.grid(row=2, column=0)
        self.idbus = Entry(self.lbf_1)
        self.idbus.grid(row=2, column=1)

        self.rt = StringVar()
        self.labl_3 = Label(self.lbf_1, text="Tipo de ruta: ").grid(row=3, column=0)
        OptionMenu(self.lbf_1,self.rt, *rutas()).grid(row=3, column=1)

        #Datos Parada 

        self.lbf_2 = LabelFrame(self, text="Datos parada", pady=30, padx=50)
        self.lbf_2.grid(row=2,column=0)

        self.labl_4 = Label(self.lbf_2, text="Lugar\nparada: ")
        self.labl_4.grid(row=1, column=0)
        #OptionMenu(self.lbf_2, self.lp, 'Valledupar', 'Universidad', 'Manaure', 'La Paz', 'Codazzi', 'San Diego').grid(row=1,column=1)
        self.lp = Entry(self.lbf_2)
        self.lp.grid(row=1,column=1)
        
        #fecha y hora

        self.lbf_3=LabelFrame(self, text="Fecha y Hora", pady=30, padx=50)
        self.lbf_3.grid(row=3,column=0)
        
        self.fch = StringVar()
        self.fch.set(hr.Horario().fecha_str)
        self.labl_5 = Label(self.lbf_3, text="Fecha:")
        self.labl_5.grid(row=1, column=0)
        Entry(self.lbf_3, textvariable=self.fch,).grid(row=1, column=1)

        self.labl_6 = Label(self.lbf_3, text="Hora\nde llegada:")
        self.labl_6.grid(row=2, column=0)
        self.hll = Entry(self.lbf_3)
        self.hll.grid(row=2, column=1)

        self.labl_7 = Label(self.lbf_3, text="Hora\nde salida:")
        self.labl_7.grid(row=3, column=0)
        self.hs = Entry(self.lbf_3)
        self.hs.grid(row=3, column=1)

        self.btn_1 = Button(self, text="Modificar", command=self.modParada)
        self.btn_1.grid(row=4, column=0)
    def modParada(self):
        id = int(self.idp.get())
        b = bs.Bus()
        b.set_nombre_chofer(self.n_ch.get())
        b.set_bus_num(self.idbus.get())
        b.set_id_rt(ponerid(self.rt.get()))
        p =pr.Lugar()
        p.set_lugar_parada(self.lp.get()) 

        h = hr.Horario()
        h.set_fecha(self.fch.get())
        h.set_h_llegada(self.hll.get())
        h.set_h_salida(self.hs.get())

        r = Rutas(b,h,p)

        r.modificar_ruta(id)
    
class Vparadas3(Tk):
        def __init__(self) -> None:
            super().__init__()
            self.tabla = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5", "col6","col7"))
            self.tabla.column("#0",width=50)
            self.tabla.column("col1",width=60,anchor=CENTER)
            self.tabla.column("col2",width=123,anchor=CENTER)
            self.tabla.column("col3",width=60,anchor=CENTER)
            self.tabla.column("col4",width=90,anchor=CENTER)
            self.tabla.column("col5",width=90,anchor=CENTER)
            self.tabla.column("col6",width=90,anchor=CENTER)
            self.tabla.column("col7",width=60,anchor=CENTER)

            self.tabla.heading("#0",text="Id", anchor=CENTER)
            self.tabla.heading("col1",text="bus_num",anchor=CENTER)
            self.tabla.heading("col2",text="nombre_conductor",anchor=CENTER)
            self.tabla.heading("col3",text="id_ruta",anchor=CENTER)
            self.tabla.heading("col4",text="lugar_parada",anchor=CENTER)
            self.tabla.heading("col5",text="hora_llegada",anchor=CENTER)
            self.tabla.heading("col6",text="hora_salida",anchor=CENTER)
            self.tabla.heading("col7",text="fecha",anchor=CENTER)
            self.tabla.grid(row=0,column=0)
            self.datos()
        def datos(self):
            dt = clt3().consulta()
            for r in dt:
                self.tabla.insert("",END,text=r[0],values=(r[1],r[2],r[3],r[4],r[5],r[6],r[7]))
class Vparadas4(Tk):
        def __init__(self) -> None:
            super().__init__()
            self.tabla = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
            self.tabla.column("#0",width=50)
            self.tabla.column("col1",width=120,anchor=CENTER)
            self.tabla.column("col2",width=90,anchor=CENTER)
            self.tabla.column("col3",width=90,anchor=CENTER)
            self.tabla.column("col4",width=90,anchor=CENTER)
            self.tabla.column("col5",width=90,anchor=CENTER)
            self.tabla.column("col6",width=90,anchor=CENTER)
            

            self.tabla.heading("#0",text="Id", anchor=CENTER)
            self.tabla.heading("col1",text="bus_num",anchor=CENTER)            
            self.tabla.heading("col2",text="id_ruta",anchor=CENTER)
            self.tabla.heading("col3",text="lugar_parada",anchor=CENTER)
            self.tabla.heading("col4",text="hora_llegada",anchor=CENTER)
            self.tabla.heading("col5",text="hora_salida",anchor=CENTER)
            self.tabla.heading("col6",text="fecha",anchor=CENTER)
            self.tabla.grid(row=0,column=0)
            self.datos()
        def datos(self):
            dt = clt().consulta()
            for r in dt:
                self.tabla.insert("",END,text=r[0],values=(r[1],r[2],r[3],r[4],r[5],r[6]))
if __name__ == "__main__":
    app = Vparadas4()
    app.mainloop()
        













