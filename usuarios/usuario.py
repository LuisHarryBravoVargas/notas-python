#import re
#from sqlite3 import connect
#from tkinter import _Cursor
#from unittest import result
#import mysql.connector
import hashlib
import datetime
#from unittest import result
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

#print(database)
class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        #cifrar contraseña
        cifrado = hashlib.sha256() #usamos de la libreria haslib el metodo sha256 para cifrar
        cifrado.update(self.password.encode('utf8')) #aqui, el metodo update no puede cifrar como tal el self.password por eso le añadimos el metodo encode y utf8
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha) #aqui le pasamos el cifrado con el metodo hexdigest

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
        
    def identificar(self):
        #consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        #cifrar contraseña
        cifrado = hashlib.sha256() #usamos de la libreria haslib el metodo sha256 para cifrar
        cifrado.update(self.password.encode('utf8')) #aqui, el metodo update no puede cifrar como tal el self.password por eso le añadimos el metodo encode y utf8
        #datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result
