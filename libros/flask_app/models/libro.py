from flask_app.config.mysqlconnection import connectToMySQL
#Acá debes de importar el modelo del autor con from flask_app.models import autor (Y luego llegar a todo lo del módulo a través de su clase con autor.Autor)

class Libro:
    def __init__(self,data):

        self.nombre = data['titulo']
        self.numero_paginas = data['numero_paginas']
        #acá debes de agregar la relación, con un "self.fans = []" en donde los fans son los autores que le dieron un favorito

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

    @classmethod
    def traer_libro_con_fans(cls, data):
        query = #Una query que tenga ambos diccionarios a través de un LEFT JOIN de un libro específico con un WHERE hacia su id (debe ser en específico o todo se complicará, pero se puede también),
        libro_con_autores = connectToMySQL('esquema_libros').query_db(query) #Esta query tiene repetidas en todas las filas al mismo libro, y en cada fila, tiene adherido cada autor, esto por el WHERE hacia el libro
        libro = cls(libro_con_autores[0]) #Esto porque como todas las filas tienen el mismo libro, tomas cualquier índice del array de diccionarios el array de filas), pero es necesario que sea la primera posición con ese [0], para evitar excepciones por si hay una sola fila como respuesta, en el caso en donde un libro sea puesto como favorito por una sola persona
        #Tip bacán: Si es que no hubiera ningún libro con tal id, por alguna razón, puedes poner "if libro_con_autores:", ese if será verdadero si es que la query te devuelve un resultado
        #Luego de crear el libro, hacemos un bucle sobre las filas
        for fila in libro_con_autores:
            #Acá generas un diccionario desde la query, para instanciar cada fila (cada autor/fan) con ese diccionario
            diccionario = {
                'atributo_del_modelo_autor': fila['nombre de la columna en tu base de datos, es decir, en la query']
            } #En este diccionario pones cada atributo
            #Y luego, terminas instanciando ese objeto/auto/fan, y se lo metes en el array del atributo de la línea 9 de este documento
            libro.fans.append(autor.Autor(diccionario))
            #Este proceso se repetirá en todos los autores asociados a tal libro
        #Y cuando se termine todo, retornar ese libro con los autores adentro
        return libro #Y listo! Luego haces lo mismo cnn el modelo de autores, es decir, trayendo libros dentro de un autor
            
