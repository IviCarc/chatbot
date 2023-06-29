from flask import request, Blueprint, jsonify
from utils.db import db

from models.anfitrion import Anfitrion 
from models.cliente import Cliente
from models.reunion import Reunion 

reuniones = Blueprint("reuniones", __name__)

### METODOS GET ###

@reuniones.route('/reuniones')
def getAllReuniones():
    reuniones = db.session.execute(db.select(Reunion)).scalars()
    return jsonify(Reunion.serialize_list(reuniones))

@reuniones.route('/reunion/<int:id>')
def getReunionById(id):
    reunion = db.get_or_404(Reunion, id)
    return jsonify(Reunion.serialize(reunion))

@reuniones.route('/cliente/<string:nombre>')
def getReunionsByCliente(nombre):

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

def guardarAnfitrion(nombre, correo, telefono):
    anfitrion = Anfitrion(nombre, correo, telefono)
    db.session.add(anfitrion)
    db.session.commit()
    return jsonify(Anfitrion.serialize(anfitrion))


@reuniones.route('/', methods=["POST"])
def agendarReunion():
    form = request.form

    cliente_id = None

    cliente = db.session.execute(db.select(Cliente).filter_by(nombre=form["nombre"])).fetchone()
    
    if cliente == None:
        cliente_id = guardarCliente(form["nombre"], form["correo"], form["telefono"])
    else:
        cliente_id = cliente[0].id

    reunion = Reunion(form["chat"], form["fechaHora"], cliente_id, 1)

    db.session.add(reunion)
    db.session.commit()

    return jsonify(Reunion.serialize(reunion))

@reuniones.route('/<int:id>', methods=["PUT"])
def editarReunion(id):
    form = request.form

    reunion = Reunion.query.get(id)
    reunion.fechaHora = form["fechaHora"]

    db.session.commit()

    return jsonify(Reunion.serialize(reunion))  

@reuniones.route('/<int:id>', methods=["DELETE"])
def eliminarReunion(id):
    reunion = Reunion.query.get(id)
    db.session.delete(reunion)
    db.session.commit()
    return jsonify(Reunion.serialize(reunion))