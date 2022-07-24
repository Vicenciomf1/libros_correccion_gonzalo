from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.libro import Libro

@app.route('/libros')
def nuevo_libro():
    libross = Libro.todos_libros()
    print("segundo testeo libros:", libross) #Segundo testeo
    return render_template('libros.html', libros=libross)

@app.route('/crear/libro', methods= ['POST'])
def crear():
    Libro.crear_libro(request.form)
    return redirect('/libros')
