
import sqlite3 as sql

"""class Rutas:

    def __init__(self, b:bs.Bus, h:hr.Horario, l:pr.Lugar):
        self.ruta=[b.bus_num, b.nombre_chofer, l.lugar_parada, h.h_llegada, h.h_salida, h.fecha]
    def ingresarruta(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()  
        
        query = f""" """INSERT INTO ruta(bus_num, nombre_conductor, lugar_parada, hora_llegada, hora_salida, fecha) 
                    VALUES ('{self.ruta[0]}','{self.ruta[1]}','{self.ruta[2]}','{self.ruta[3]}','{self.ruta[4]}','{self.ruta[5]}')""" """
        cursor.execute(query)
        conex.commit()
        conex.close()
    def modificar_ruta(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()  
        query = f""" """UPDATE ruta 
                    SET bus_num = '{self.ruta[0]}'
                        nombre_conductor = '{self.ruta[1]}'
                        lugar_parada = '{self.ruta[2]}'
                        hora_llegada = '{self.ruta[3]}'
                        hora_ salida =  '{self.ruta[4]}' 
                        fecha = '{self.ruta[5]}'""" """
        cursor.execute(query)
        conex.commit()
        conex.close()"""

class Rutas:
    def __init__(self) -> None:
        self.n_ruta = " "
        
        self.ruta = [ ]
    
    def set_n_ruta(self,n:str):
        self.n_ruta = f"R.{n}"

    def set_paradas(self, *p):
        for i in p:
            self.ruta.append(i)           
        if len(p) == 0:
            self.ruta = [" ", " ", " ", " "]
        if len(p)<4 and len(p)>0:
            n_r=4-len(self.ruta)
            for i in range(0,n_r):
                self.ruta.append(" ")
        
        print(self.ruta)
    
    def ingresarbd(self):
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()
        query = f"INSERT INTO rutas(nombre_ruta,parada_1,parada_2,parada_3,parada_4) VALUES ('{self.n_ruta}','{self.ruta[0]}','{self.ruta[1]}','{self.ruta[2]}','{self.ruta[3]}')"
        cursor.execute(query)
        conex.commit()
        conex.close()
    
    def nuevaparada(self, nr:str, pr:str):
        parada = f"parada_{len(self.ruta)+1}"
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()
        query = f"ALTER TABLE rutas ADD {parada} DEFAULT ' '"
        cursor.execute(query)
        query2 = f"UPDATE rutas SET {parada}={pr} WHERE nombre_ruta = {nr}"
        cursor.execute(query2)
        conex.commit()
        conex.close()
        self.ruta.append(pr)
    

    def modificar_ruta(self, nr:str   , p1:str = " ", p2:str = " " , p3:str = " ", p4:str = " "):        

        r = [p1,p2,p3,p4]
        
        for i in range(0,len(r)):
            if r[i] == " ":
                r[i] = self.ruta[i]
        
        
        conex = sql.connect("rutas.db")
        cursor = conex.cursor()
        query2 = f"UPDATE rutas SET parada_1 = '{r[0]}', parada_2 = '{r[1]}', parada_3='{r[2]}', parada_4='{r[3]}' WHERE nombre_ruta = '{nr}'"
        cursor.execute(query2)
        conex.commit()
        conex.close()

"""#Ruta Circular
rc = Rutas()
rc.set_n_ruta("R.Circular")
rc.set_paradas("Valledupar", "La Paz", "Universidad")
rc.ingresarbd()

#Ruta Manaure
rm = Rutas()
rm.set_n_ruta("R.Manaure")
rm.set_paradas("Manaure", "La Paz", "Universidad")
rm.ingresarbd()

#Ruta Codazzi 

rco = Rutas()
rco.set_n_ruta("R.Codazzi")
rco.set_paradas("Codazzi", "San Diego", "La Paz", "Universidad")
rco.ingresarbd()"""






