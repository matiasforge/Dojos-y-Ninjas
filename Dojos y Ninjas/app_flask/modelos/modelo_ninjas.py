from app_flask.configuracion.mysqlconnection import connectToMySQL
from app_flask import BASE_DATOS

class Ninja:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.edad = datos['edad']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.id_dojo = datos['id_dojo']
    
    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO ninjas(nombre, apellido, edad, id_dojo)
                VALUES(%(nombre)s,%(apellido)s,%(edad)s,%(id_dojo)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)