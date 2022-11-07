import sqlite3 as sql

tabla_bus = """CREATE TABLE bus (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bus_num text,
            nombre_conductor text
        )"""
tabla_lugar = """CREATE TABLE lugar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lugar_parada text
                )"""
tabla_horario = """CREATE TABLE horario (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   hora_llegada text,
                   hora_salida text  
                )"""
tabla_fecha = """CREATE TABLE fecha (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   fecha text                    
                )"""
tabla_paradas = """CREATE TABLE paradas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                     text,
                    nombre_conductor text,
                    lugar_parada text,
                    hora_llegada text,
                    hora_salida text,
                    fecha text
                )"""

tabla_usuario = """CREATE TABLE usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario text,
                    nombre text,
                    cargo text
                )"""

tabla_rutas = 0
conex = sql.connect("rutas.db")
cursor = conex.cursor()
#cursor.execute(tabla_bus)
#cursor.execute(tabla_paradas)
#cursor.execute(tabla_horario)
#cursor.execute(tabla_fecha)
#cursor.execute(tabla_ruta)
#cursor.execute(tabla_usuario)
#cursor.execute("DROP table bus")
#cursor.execute("DROP table paradas")
#cursor.execute("DROP table horario")
#cursor.execute("DROP table fecha")
cursor.execute("DROP table rutas")
conex.commit()
conex.close()