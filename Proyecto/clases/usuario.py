import sqlite3 as sql

class Usuario:
    def __init__(self) -> None:
        self.nombre = ""
        self.id_usuario = ""
        self.cargo = ""
    def set_nombre(self, nm):
        self.nombre = nm
    def set_id(self, id):
        self.id = id
    def set_cargo(self, crg):
        self.cargo = crg 
    def registrardatos(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()  
        query = f"""INSERT INTO usuario (id_usuario, nombre, cargo) VALUES ('{self.id_usuario}', '{self.nombre}', '{self.cargo}')"""
        cursor.execute(query)
        conex.commit()
        conex.close()