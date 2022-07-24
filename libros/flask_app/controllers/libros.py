from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.libro import Libro

@app.route('/libros')
def nuevo_libro():
    return render_template('libros.html', libros=Libro.todos_libros())

@app.route('/crear/libro', methods= ['POST'])
def crear():
    Libro.crear_libro(request.form)
    return redirect('/libros')
