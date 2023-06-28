from flask import request, Blueprint
from utils.db import db

from models.anfitrion import Anfitrion 
from models.cliente import Cliente
from models.reunion import Reunion 
import json
import datetime

from datetime import datetime

reuniones = Blueprint("reuniones", __name__)

### METODOS GET ###

# Las siguientes dos funciones reciben un array de tuplas desde un cursor.fetchall normalmente.
# Lo que consiguen es devolver un json cuyas keys son los mismos nombres de las columnas en la DB
# Puede mejorar la complejidad, posiblemente es muy lenta debido al uso de ZIP y MAP
# Tener en cuenta que siempre devuelve un json que comienza con un array => [{datos}, {datos}]

def formatearFechas(campo):
        if isinstance(campo, datetime.date):
            print(campo)
            return campo.strftime("%Y/%m/%d")
        elif isinstance(campo, datetime.timedelta):
            return str(campo)
        return campo

def serialize(data, headers):
    json_data=[]
    for result in data:
        json_data.append(dict(zip(headers,list(map(formatearFechas, result)))))
    return json.dumps(json_data)

# Devuelve un array con los nombres de las columnas en la DB

def getHeaders(cursor):
    row_headers=[x[0] for x in cursor.description]
    return row_headers

@reuniones.route('/reuniones')
def getAllReuniones():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM reuniones")

    headers = getHeaders(cursor)
    rv = cursor.fetchall()

    return serialize(rv, headers)

@reuniones.route('/reunion')
def getReunionById():
    cursor = db.database.cursor()
    id = request.args.get("id")
    cursor.execute("SELECT * FROM reuniones WHERE ID = %s", [id])
    headers = getHeaders(cursor)
    reunion = cursor.fetchall()

    return serialize(reunion, headers)

@reuniones.route('/cliente')
def getReunionsByCliente():
    cursor = db.database.cursor()
    cliente = request.args.get("cliente")
    cursor.execute("SELECT ID FROM clientes WHERE nombre = %s", [cliente])
    id = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM reuniones WHERE ID = %s", [id])

    row_headers=[x[0] for x in cursor.description]
    reuniones = cursor.fetchall()

    return serialize(reuniones, row_headers)

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
    return anfitrion.id


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

    return form


@reuniones.route('/', methods=["PUT"])
def editarReunion():
    return "REUNION EDITADA"

@reuniones.route('/', methods=["DELETE"])
def eliminarReunion():
    cursor = db.database.cursor()
    id = request.args.get("id")
    cursor.execute("DELETE FROM reuniones WHERE ID = %s", [id])
    db.database.commit()
    return "REUNION ELIMINADA"