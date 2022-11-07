import clases.lugares as pr
import clases.bus as bs
import clases.Horario as hr
import clases.usuario as usr

from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
vent = Tk()

vent.title("Rutas bus")
marco = Frame(vent, width=700,height=200)
marco.pack()

nm = StringVar()
Label(marco, text="Nombre:",pady=20, padx=10).grid(row=1, column=0)
Entry(marco, textvariable= nm).grid(row=1, column=1)

id = StringVar()
Label(marco, text="id:",pady=20).grid(row=2, column=0)
Entry(marco, textvariable= id).grid(row=2, column=1)

crg = StringVar()
Label(marco, text="Cargo:",pady=20).grid(row=3, column=0)
OptionMenu(marco,crg, "Administrativo", "Estudiante", "Otro").grid(row=3, column=1)

class VentanaSec(Toplevel):
    def __init__(self, *args,  **kwargs) -> None:
        super().__init__(*args, **kwargs)    
        self.title("Elija una opción")
        self.boton1= Button(self, text="Registrar datos de parada")
        self.boton2 = Button(self, text="Consultar Rutas ")

    def acc_boton1(self):
        import Ventanaz.v_registrar as v_registrar
    def acc_boton2(self):
        pass


    
def registro():
    u = usr.Usuario()
    u.set_nombre(nm.get())
    u.set_id(id.get())
    u.set_cargo(crg.get())
    u.registrardatos()
    if crg.get()== "Administrativo":
        pass
    import Ventanaz.v_registrar as v_registrar
    #vent.withdraw()

Button(marco, text="Registrar", command=registro).grid(row=4,column=0, columnspan=2)
#Button(marco, text="cerrar", command=cerrar).grid(row=5,column=0, columnspan=2)

vent.mainloop()
