from flask_app.config.mysqlconnection import connectToMySQL

class Libro:
    def __init__(self,data):

        self.nombre = data['titulo']
        self.numero_paginas = data['numero_paginas']

    @classmethod
    def crear_libro(cls, data):
        query = "INSERT INTO libros (titulo, numero_paginas, creado_en, actualizado_en) VALUES (%(titulo)s, %(numero_paginas)s, NOW(), NOW());"
        return connectToMySQL('esquema_libros').query_db(query, data)

    @classmethod
    def todos_libros(cls):
        query = "SELECT titulo, numero_paginas FROM libros;"
        libros_db= connectToMySQL('esquema_libros').query_db(query)
        libros = []
        for i in libros_db:
            libros.append(cls(i))
        return libros

