from clases.consulta import Consulta2 as clt2
import clases.rutas as rt
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

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

class Vruta1(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Ingresar Ruta")
        self.config(padx=30, pady=30)
        self.labl_1 = Label(self, text="Nombre de la ruta:")
        self.labl_1.grid(row=1, column= 0)
        self.nr = Entry(self)
        self.nr.grid(row=1, column=1)

        self.labl_2 = Label(self, text="Parada 1:")
        self.labl_2.grid(row=2, column=0)
        self.p1 = Entry(self)
        self.p1.grid(row=2, column=1)

        self.labl_3 = Label(self, text="Parada 2:")
        self.labl_3.grid(row=3, column=0)
        self.p2 = Entry(self)
        self.p2.grid(row=3, column=1)

        self.labl_4 = Label(self, text="Parada 3:")
        self.labl_4.grid(row=4, column=0)
        self.p3 = Entry(self)
        self.p3.grid(row=4, column=1)

        self.labl_5 = Label(self, text="Parada 4:")
        self.labl_5.grid(row=5, column=0)
        self.p4 = Entry(self)
        self.p4.grid(row=5, column=1)

        self.btn_1 = Button(self, text="Nueva \n Parada", command=self.nParada)
        self.btn_1.grid(row= 6,column=0)
        self.btn_2 = Button(self, text="Registrar", command=self.registrar)
        self.btn_2.grid(row= 6,column=1)
        self.btn_2.config(pady=10)

    def nParada(self):
        pg = Subventana()
        pg.mainloop()
        
    def registrar(self):
        r = rt.Rutas()
        r.set_n_ruta(self.nr.get())
        r.set_paradas(self.p1.get(),self.p2.get(),self.p3.get(), self.p4.get())
        r.ingresarbd()    
        print(messagebox.showinfo(message="Datos registrados con éxito"))    

class Subventana(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title('Ingrese nueva parada')
        self.config(padx=30, pady=30)

        self.lbl = Label(self, text="Nombre\nRuta:")
        self.lbl.grid(row=1, column=0)
        self.nr = Entry(self)
        self.nr.grid(row=1, column=1)

        self.lbl_1= Label(self, text="Nueva\nParada:")
        self.lbl_1.grid(row=2, column=0)
        self.pr = Entry(self)
        self.pr.grid(row=2, column=1)

        self.btn = Button(self, text="Registrar")
        self.btn.grid(row=3, column=0, columnspan=2)

    def regParada(self):
        rt.Rutas().nuevaparada(self.nr.get(),self.pr.get())
        print(messagebox.showinfo(message="Datos registrados con éxito"))

class Vruta2(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Modificar Ruta')
        self.config(padx=30, pady=30)
        
        self.lbf = LabelFrame(self, text="Nombre de ruta a modificar")
        self.lbf.grid(row=0, column=0, columnspan=2)
        self.lbf.config(pady=20, padx= 10)
        self.nr = StringVar()
        OptionMenu(self.lbf,self.nr,*rutas()).grid(row=1, column=0)

        self.labl_2 = Label(self, text="Parada 1:")
        self.labl_2.grid(row=2, column=0)
        self.p1 = Entry(self)
        self.p1.grid(row=2, column=1)

        self.labl_3 = Label(self, text="Parada 2:")
        self.labl_3.grid(row=3, column=0)
        self.p2 = Entry(self)
        self.p2.grid(row=3, column=1)

        self.labl_4 = Label(self, text="Parada 3:")
        self.labl_4.grid(row=4, column=0)
        self.p3 = Entry(self)
        self.p3.grid(row=4, column=1)

        self.labl_5 = Label(self, text="Parada 4:")
        self.labl_5.grid(row=5, column=0)
        self.p4 = Entry(self)
        self.p4.grid(row=5, column=1)

        self.btn_1 = Button(self, text="Modificar", command=self.modRuta)
        self.btn_1.grid(row= 6,column=0)

    def modRuta(self):
        r = rt.Rutas()
        r.modificar_ruta(self.nr.get(),self.p1.get(),self.p2.get(),self.p3.get(),self.p4.get())
        print(messagebox.showinfo(message="Datos modificados con éxito"))

class Vruta3(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.tabla = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5"))
        self.tabla.column("#0",width=50)
        self.tabla.column("col1",width=130,anchor=CENTER)
        self.tabla.column("col2",width=90,anchor=CENTER)
        self.tabla.column("col3",width=90,anchor=CENTER)
        self.tabla.column("col4",width=90,anchor=CENTER)
        self.tabla.column("col5",width=90,anchor=CENTER)
        

        self.tabla.heading("#0",text="Id", anchor=CENTER)
        self.tabla.heading("col1",text="nombre_ruta",anchor=CENTER)
        self.tabla.heading("col2",text="parada 1",anchor=CENTER)
        self.tabla.heading("col3",text="parada 2",anchor=CENTER)
        self.tabla.heading("col4",text="parada 3",anchor=CENTER)
        self.tabla.heading("col5",text="parada 4",anchor=CENTER)
        self.tabla.grid(row=0,column=0)   
        self.datos()
    def datos(self):
        dt = clt2().consulta()
        for r in dt:
            self.tabla.insert("",END,text=r[0],values=(r[1],r[2],r[3],r[4],r[5]))           
if __name__ == "__main__":
    apd = Vruta3()
    apd.mainloop()