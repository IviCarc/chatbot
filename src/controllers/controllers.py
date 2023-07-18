from flask import request, Blueprint, jsonify, render_template, redirect, url_for, jsonify, session
from utils.db import db
import hashlib
from utils.mail import enviarCorreo
from models.anfitrion import Anfitrion 
from models.cliente import Cliente
from models.reunion import Reunion 
from models.usuario import Usuario
import random
from datetime import date, datetime

reuniones = Blueprint("reuniones", __name__)

@reuniones.before_request
def middleware():
    print("Middleware")

### METODOS GET ###

@reuniones.route('/reuniones')
def getAllReuniones():
    if not 'loggedin' in session:
        return redirect(url_for('reuniones.login'))
    reuniones = db.session.execute(db.select(Reunion).order_by(Reunion.fechaHora)).scalars()
    return render_template('layout.html', reuniones=reuniones)

@reuniones.route('/reunion/<int:id>')
def getReunionById(id):
    if not 'loggedin' in session:
        return redirect(url_for('reuniones.login'))
    reunion = db.get_or_404(Reunion, id)
    return jsonify(Reunion.serialize(reunion))

@reuniones.route('/cliente/<string:nombre>')
def getReunionsByCliente(nombre):
    if not 'loggedin' in session:
        return redirect(url_for('reuniones.login'))

    cliente = db.session.execute(db.select(Cliente).filter_by(nombre=nombre)).fetchone()

    if cliente == None:
        return '404'

    reuniones = db.session.execute(db.select(Reunion).filter_by(idCliente=cliente[0].id)).scalars()

    return jsonify(Reunion.serialize_list(reuniones))

### METODOS POST ###

def guardarCliente(nombre,correo, telefono):
    cliente = Cliente(nombre,correo, telefono)
    db.session.add(cliente)
    db.session.commit()
    return cliente.id

def guardarAnfitrion(nombre, correo):
    anfitrion = Anfitrion(nombre, correo)
    db.session.add(anfitrion)
    db.session.commit()
    return jsonify(Anfitrion.serialize(anfitrion))


@reuniones.route('/', methods=["POST"])
def agendarReunion():
    form = request.form

    # Formato al telefono
    telefono = f"{form['telefono'][:-10]} {form['telefono'][-10:-7]}-{form['telefono'][-7:-4]}-{form['telefono'][-4:]} "
    # Formato a la fecha
    fechaHora = datetime.strptime(form["fechaHora"], "%d/%m/%Y %H:%M:%S")

    # Agregar el cliente si no existe
    cliente_id = None

    cliente = db.session.execute(db.select(Cliente).filter_by(nombre=form["nombre"])).fetchone()
    
    if cliente == None:
        cliente_id = guardarCliente(form["nombre"], form["correo"], telefono)
    else:
        cliente_id = cliente[0].id

    # Seleccionar el anfitrion de forma random

    anfitriones = db.session.execute(db.select(Anfitrion)).fetchall()
    print(len(anfitriones))
    anfitrion = anfitriones[random.randint(0, len(anfitriones)-1)][0]

    reunion = Reunion(form["chat"], fechaHora, cliente_id, anfitrion.id)

    db.session.add(reunion)
    db.session.commit()

    # print(form["chat"])

    enviarCorreo(anfitrion.correo, form["nombre"],  telefono, form["fechaHora"], form["chat"], reunion.id, form["correo"])
    
    return jsonify(Reunion.serialize(reunion))

@reuniones.route('/reuniones/<int:id>', methods=["GET", "PUT"])
def editarReunion(id):
    if not 'loggedin' in session:
        return redirect(url_for('reuniones.login'))
    reunion = Reunion.query.get(id)

    anfitriones = db.session.execute(db.select(Anfitrion)).scalars()

    if request.method == "PUT":
        body = request.get_json()

        reunion.fechaHora = body["fechaHora"]

        id_anfitrion = db.session.execute(db.select(Anfitrion).filter_by(nombre=body["anfitrion"])).fetchone()[0].id
        reunion.idAnfitrion = id_anfitrion

        db.session.commit()
        return "editado"

    return render_template("update.html", reunion = reunion, anfitriones = anfitriones)

@reuniones.route('/reuniones/<int:id>/chat', methods=["GET"])
def verChat(id):    
    if not 'loggedin' in session:
        return redirect(url_for('reuniones.login'))
    reunion = Reunion.query.get(id)

    cliente = db.session.execute(db.select(Cliente).filter_by(id=reunion.idCliente)).fetchone()[0]

    return render_template("chat.html", chat = reunion.chat.split("/"), cliente = cliente.nombre)

@reuniones.route('/<int:id>', methods=["DELETE"])
def eliminarReunion(id):
    if not 'loggedin' in session:
        return redirect(url_for('reuniones.login'))
    print(id)
    reunion = Reunion.query.get(id)
    db.session.delete(reunion)
    db.session.commit()
    return "eliminado"

## Login

@reuniones.route('/login', methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Retrieve the hashed password
        # hash = password
        # hash = hashlib.sha1(hash.encode())
        # password = hash.hexdigest()
        
        # Check if account exists using MySQL
        try:
            account = db.session.execute(db.select(Usuario).filter_by(username=username)).fetchone()[0]
        except:
            msg = 'No existe un usuario con ese nombre'
            return render_template("login.html", msg=msg)
         # Create session data, we can access this data in other routes
        if account.password != password:
            msg = "La contraseña no es correcta"
        else:
            session['loggedin'] = True
            session['id'] = account.id
            print(session['id'])
            session['username'] = account.username
            # Redirect to home page
            print("LOGGED")
            return redirect(url_for('reuniones.getAllReuniones'))

    if 'loggedin' in session:
        return redirect(url_for('reuniones.getAllReuniones'))
    return render_template("login.html", msg=msg)

@reuniones.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('reuniones.login'))

@reuniones.route('/reuniones/fechas_ocupadas', methods=['GET'])
def obtener_fechas_ocupadas():
    fechas_ocupadas = []
    reuniones = Reunion.query.filter(Reunion.fechaHora >= date.today()).all()

    for reunion in reuniones:
        fecha_ocupada = reunion.fechaHora.strftime("%d/%m/%Y %H:%M:%S")
        print(fecha_ocupada) 
        fechas_ocupadas.append(fecha_ocupada)

    return jsonify(fechas_ocupadas)
