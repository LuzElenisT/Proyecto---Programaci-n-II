import sqlite3 as sql
from datetime import datetime

hoy = datetime.today().date()
class Consulta1:
    def __init__(self) -> None:
        self.conex = sql.connect("rutas.db")
        
        
    def __str__(self) -> str:
        datos = self.consulta()
        aux=" "
        for r in datos:
            aux = aux+str(r)+"\n"
        return aux

    def consulta(self):
        self.cursor = self.conex.cursor()
        query = f"SELECT id, bus_num, id_ruta, lugar_parada, hora_llegada, hora_salida, fecha FROM paradas WHERE fecha = '{hoy}'"
        datos = self.cursor.execute(query).fetchall()
        self.conex.commit()
        self.conex.close()
        return datos



class Consulta2:
    def __init__(self) -> None:
        self.conex = sql.connect("rutas.db")
        
        
    def __str__(self) -> str:
        datos = self.consulta()
        aux=" "
        for r in datos:
            aux = aux+str(r)+"\n"
        return aux

    def consulta(self):
        self.cursor = self.conex.cursor()
        query = "SELECT * FROM rutas"
        datos = self.cursor.execute(query).fetchall()
        self.conex.commit()
        self.conex.close()
        return datos

class Consulta3:
    def __init__(self) -> None:
        self.conex = sql.connect("rutas.db")
        
        
    def __str__(self) -> str:
        datos = self.consulta()
        aux=" "
        for r in datos:
            aux = aux+str(r)+"\n"
        return aux

    def consulta(self):
        self.cursor = self.conex.cursor()
        query = "SELECT * FROM paradas"
        datos = self.cursor.execute(query).fetchall()
        self.conex.commit()
        self.conex.close()
        return datos


f = Consulta1()
print(f)