import sqlite3 as sql


class Bus:
   
    nombre_chofer:str = ""
    bus_num:str = ""
    id_rt:str = ""
    def set_nombre_chofer(self, n:str): 
        self.nombre_chofer = n

    def set_bus_num(self, num:str): 
        self.bus_num = num

    def set_id_rt(self, id):
        self.id_rt = id
    def insertardatos(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()
        #query = f"INSERT INTO bus(bus_num, nombre_conductor) VALUES ('{self.bus_num}','{self.nombre_chofer}')"
        query = f"INSERT INTO ruta(bus_num, nombre_conductor) VALUES ('{self.bus_num}','{self.nombre_chofer}')"
        cursor.execute(query)
        conex.commit()
        conex.close()
        
