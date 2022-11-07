import sqlite3 as sql

def rutas():
    lista = []
    conex = sql.connect("rutas.db")
    cursor = conex.cursor()
    query = f"SELECT nombre_ruta FROM rutas"
    res = cursor.execute(query).fetchall()
    conex.commit()
    conex.close()
    for i in range(0,len(res)):
        lista.append(res[i][0])
    print(lista)
    return lista    

def ponerid(ruta:str):
    conex = sql.connect("rutas.db")
    cursor = conex.cursor()
    query = f"SELECT id FROM rutas WHERE nombre_ruta = '{ruta}'"
    res = cursor.execute(query).fetchall()
    conex.commit()
    conex.close()
    print(res[0][0])
    return res[0][0]

ponerid("R.Circular")


