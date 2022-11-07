import sqlite3 as sql
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

app = Tk()
app.config(width=300,height=200)
#marco = Frame(app, width=700,height=800)
#marco.pack(fill="both", expand=1)
"""def consultar(parada):
    conex = sql.connect("rutas.db") 
    cursor = conex.cursor()
    query = f"SELECT * FROM rutas WHERE lugar_parada = '{parada}"
    cursor.execute(query)
    conex.commit()
    conex.close()"""
def abrir_registro():
    import Ventanaz.v_registrar as v_registrar
Button(text="Registrar", command=abrir_registro).place()
Button(text="Consultar").place(x=122, y=120 )
#marco.pack(fill="both", expand=1)
app.mainloop()