from datetime import datetime
import sqlite3 as sql

class Fecha:
    def __init__(self) -> None:
        self.fecha = ""
    def set_fecha(self, fecha:str):
        try:  
            obj_fecha = datetime.strptime(fecha, "%d/%m/%Y")
            self.fecha = obj_fecha.date() 
        except TypeError:
            print("Formato de fecha incorrecto")  
    def ingresardatos(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()
        #query = f"INSERT INTO fecha(fecha) VALUES ('{self.fecha}')"
        query = f"INSERT INTO ruta(fecha) VALUES ('{self.fecha}')"
        cursor.execute(query)
        conex.commit()
        conex.close()