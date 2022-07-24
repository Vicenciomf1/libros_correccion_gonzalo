from flask_app.config.mysqlconnection import connectToMySQL

class Autor:
    def __init__(self,data):

        self.nombre = data['nombre']

    @classmethod
    def crear_autor(cls, data):
        query = "INSERT INTO autores (nombre, creado_en, actualizado_en) VALUES (%(nombre)s, NOW(), NOW());"
        return connectToMySQL('esquema_libros').query_db(query, data)

    @classmethod
    def todos_autores(cls):
        query = "SELECT nombre FROM autores;"
        autores_db= connectToMySQL('esquema_libros').query_db(query)
        autores = []
        for i in autores_db:
            autores.append(cls(i))
        return autores


    