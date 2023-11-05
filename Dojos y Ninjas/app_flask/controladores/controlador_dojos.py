from flask import render_template, redirect, request
from app_flask.modelos.modelo_dojos import Dojo
from app_flask import app

@app.route('/formulario/dojo', methods=['GET'])
@app.route('/dojos', methods=['GET'])
def desplegar_formulario_dojo():
    lista_dojos = Dojo.seleccionar_todos()
    return render_template('formulario_dojo.html', lista_dojos=lista_dojos)

@app.route('/nuevo/dojo', methods=['POST'])
def crear_dojo():
    nuevo_dojo = {
        "nombre": request.form['nombre']
    }
    Dojo.agregar_uno(nuevo_dojo)
    return redirect('/dojos')

@app.route('/dojos/<int:id>', methods=['GET'])
def desplegar_dojo_con_ninjas(id):
    datos = {
        "id_dojo" : id
    }
    dojo = Dojo.seleccionar_uno_con_ninjas(datos)
    hay_ninjas = True
    if len(dojo.ninjas) == 0:
        hay_ninjas = False
    return render_template("dojo.html", dojo=dojo, hay_ninjas=hay_ninjas)