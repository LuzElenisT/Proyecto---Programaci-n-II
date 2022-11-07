import sqlite3 as sql


tabla_parada = """CREATE TABLE paradas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    bus_num text,
                    nombre_conductor text,
                    id_ruta INTEGER,
                    lugar_parada text,
                    hora_llegada text,
                    hora_salida text,
                    fecha text,
                    CONSTRAINT fk_rutas
                    FOREIGN KEY (id) 
                    REFERENCES rutas(id_ruta)
                )"""

tabla_usuario = """CREATE TABLE usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario text,
                    nombre text,
                    cargo text
                )"""

tabla_rutas = """CREATE TABLE rutas(
                    id INTEGER PRIMARY KEY ,
                    nombre_ruta text UNIQUE,
                    parada_1 text,
                    parada_2 text,
                    parada_3 text,
                    parada_4 text
                )"""
conex = sql.connect("rutas.db")
cursor = conex.cursor()

#cursor.execute(tabla_rutas)
cursor.execute(tabla_parada)
#cursor.execute(tabla_usuario)
#cursor.execute("DROP table rutas")
#cursor.execute("DROP table paradas")
#cursor.execute("DROP table usuario")
conex.commit()
conex.close()