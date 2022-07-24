from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.autor import Autor

@app.route('/')
def index():
    autoress = Autor.todos_autores()
    print("segundo testeo:", autoress) #Ssegundo testeo
    return render_template('index.html', autores=autoress)

@app.route('/crear/autor', methods= ['POST'])
def crear_autor():
    Autor.crear_autor(request.form)
    return redirect('/')
