import sqlite3 as sql

class Lugar: 

    def __init__(self) -> None:
        self.lugar_parada = ""       

    def set_lugar_parada(self, l:str): 
        self.lugar_parada = l
    
    def insertardatos(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()
        #query = f"INSERT INTO paradas(lugar_parada) VALUES ('{self.lugar_parada}')"
        query = f"INSERT INTO ruta(lugar_parada) VALUES ('{self.lugar_parada}')"
        cursor.execute(query)
        conex.commit()
        conex.close()