from app_flask.configuracion.mysqlconnection import connectToMySQL
from app_flask.modelos import modelo_ninjas
from app_flask import BASE_DATOS

class Dojo:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.ninjas = []
    
    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO dojos(nombre)
                VALUES (%(nombre)s);
                """

        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @classmethod
    def seleccionar_todos(cls):
        query = """
                SELECT *
                FROM dojos;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_dojos = []
        for renglon in resultado:
            lista_dojos.append(cls(renglon))
        return lista_dojos

    @classmethod
    def seleccionar_uno_con_ninjas(cls, datos):
        query = """
                SELECT *
                FROM dojos LEFT JOIN ninjas
                    ON dojos.id = ninjas.id_dojo
                WHERE dojos.id = %(id_dojo)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        dojo = Dojo(resultado[0])
        for renglon in resultado:
            if renglon['edad'] != None:
                ninja = {
                    'id' : renglon['ninjas.id'],
                    'nombre' : renglon['ninjas.nombre'],
                    'apellido' : renglon['apellido'],
                    'edad' : renglon['edad'],
                    'fecha_creacion' : renglon['ninjas.fecha_creacion'],
                    'fecha_actualizacion' : renglon['ninjas.fecha_actualizacion'],
                    'id_dojo' : renglon['id']
                }
                dojo.ninjas.append(modelo_ninjas.Ninja(ninja))
        return dojo