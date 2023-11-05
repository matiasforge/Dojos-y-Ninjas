from flask import render_template, redirect, request
from app_flask.modelos.modelo_dojos import Dojo
from app_flask.modelos.modelo_ninjas import Ninja
from app_flask import app

@app.route('/formulario/ninja', methods=['GET'])
def desplegar_formulario_ninja():
    lista_dojos = Dojo.seleccionar_todos()
    return render_template('formulario_ninja.html', lista_dojos=lista_dojos)

@app.route('/nuevo/ninja', methods=['POST'])
def crear_ninja():
    nuevo_ninja = {
        "nombre" : request.form['nombre'],
        "apellido" : request.form['apellido'],
        "edad" : request.form['edad'],
        "id_dojo" : request.form['id_dojo']
    }
    Ninja.agregar_uno(nuevo_ninja)
    return redirect(f'/dojos/{request.form["id_dojo"]}')