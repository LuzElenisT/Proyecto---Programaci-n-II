from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import clases.usuario as usr
from V_Registro import *
from V_Registro2 import *

class Subventana1(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Opciones')
        self.geometry('300x200+50+50')
        
        #Botones
        
        self.btn_1 = Button(self, text="Opciones de Ruta", command=self.abrirOpRuta)
        self.btn_1.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.btn_2 = Button(self, text="Opciones de Parada", command=self.abrirOpParadas)
        self.btn_2.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    def abrirOpRuta(self):
        self.withdraw()
        pg = Subventana2()
        pg.mainloop()
        
    
    def abrirOpParadas(self):
        self.withdraw()
        pg = Subventana3()
        pg.mainloop()
        

class Subventana2(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title('Opciones de Ruta')
        self.geometry('300x200+50+50')
        self.btn_1 = Button(self, text="Ingresar Nueva Ruta", command=self.ingRuta)
        self.btn_1.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.btn_2 = Button(self, text="Modificar Ruta", command=self.modRuta)
        self.btn_2.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btn_3 = Button(self, text="Consultar Rutas existentes", command=self.cltRutas)
        self.btn_3.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    def ingRuta(self):
        pg = Vruta1()
        pg.mainloop()
    
    def modRuta(self):
        pg = Vruta2()
        pg.mainloop()
    
    def cltRutas(self):
        pg = Vruta3()
        pg.mainloop()


class Subventana3(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title('Opciones de Paradas')
        self.geometry('300x200+50+50')
        self.btn_1 = Button(self, text="Ingresar nueva parada", command=self.ingParada)
        self.btn_1.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.btn_2 = Button(self, text="Modificar parada existente", command=self.modParada)
        self.btn_2.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btn_3 = Button(self, text="Consultar paradas existentes",command=self.cltParadas)
        self.btn_3.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    def ingParada(self):
        pg = Vparadas1()
        pg.mainloop()

    def modParada(self):
        pg = Vparadas2()
        pg.mainloop()
    
    def cltParadas(self):
        pg = Vparadas3()
        pg.mainloop()
            
class Subventana4(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title('Opciones')
        self.geometry('300x200+50+50')
        self.btn_1 = Button(self, text="Consultar Rutas \n existentes", command=self.cltRutas)
        self.btn_1.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.btn_2 = Button(self, text="Consultar Paradas\n del día", command=self.cltParadas)
        self.btn_2.place(relx=0.5, rely=0.7, anchor=CENTER)

    def cltRutas(self):
        pg = Vruta3()
        pg.mainloop()

    def cltParadas(self):
        pg = Vparadas4()
        pg.mainloop()




class Vusuario(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Registro Usuario")
        self.geometry('250x200+50+50')
        self.crg = StringVar()
        self.labl_1 = Label(self, text="Nombre:",pady=20, padx=10)
        self.labl_1.grid(row=1, column=0)
        self.nm = Entry(self)
        self.nm.grid(row=1, column=1)

        self.labl_2 = Label(self, text="id:",pady=20)
        self.labl_2.grid(row=2, column=0)
        self.id = Entry(self)
        self.id.grid(row=2, column=1)

        self.labl_3 = Label(self, text="Cargo:",pady=20)
        self.labl_3.grid(row=3, column=0)
        OptionMenu(self,self.crg, "Administrativo", "Estudiante", "Otro").grid(row=3, column=1)

        self.btn_1 = Button(self, text="Registrar", command=self.registro)
        self.btn_1.grid(row=4,column=0, columnspan=2)
    
    def registro(self):
        u = usr.Usuario()
        u.set_nombre(self.nm.get())
        u.set_id(self.id.get())
        u.set_cargo(self.crg.get())
        u.registrardatos()
        
        if self.crg.get()== "Administrativo":
            pg = Subventana1()
            pg.mainloop()
        else:
            pg = Subventana4()
            pg.mainloop()



app = Vusuario()
app.mainloop()

