from flask import request
import db as db
import json
import datetime

from datetime import datetime

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

def getAllReuniones():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM reuniones")

    headers = getHeaders(cursor)
    rv = cursor.fetchall()

    return serialize(rv, headers)

def getReunionById():
    cursor = db.database.cursor()
    id = request.args.get("id")
    cursor.execute("SELECT * FROM reuniones WHERE ID = %s", [id])
    headers = getHeaders(cursor)
    reunion = cursor.fetchall()

    return serialize(reunion, headers)

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

def guardarCliente(cliente,correo, cursor):
    print(cliente)
    cursor.execute("INSERT INTO clientes (nombre, correo) values (%s, %s)", [cliente, correo])
    db.database.commit()
    print(cursor.lastrowid)
    return cursor.lastrowid

def guardarAnfitrion(anfitrion, correo, cursor):
    cursor.execute("INSERT INTO anfitriones (nombre, correo) values (%s, %s)", [anfitrion, correo])
    db.database.commit()
    print(cursor.lastrowid)
    return cursor.lastrowid

def agendarReunion():
    req = request.get_json()
    cliente, correoCliente, anfitrion, correoAnfitrion, chat, fecha, hora = req.values()

    fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
    hora = datetime.strptime(hora, '%H:%M:%S').time()

    cursor = db.database.cursor()   
    # Chequear si el cliente existe
    cursor.execute("SELECT ID FROM clientes WHERE nombre = %s", [cliente])
    ID_cliente = cursor.fetchone()[0]

    if (ID_cliente == None):
        ID_cliente = guardarCliente(cliente, correoCliente, cursor)

    # Chequear si el anfitrion existe
    cursor.execute("SELECT ID FROM anfitriones WHERE nombre = %s", [anfitrion])
    ID_anfitrion = cursor.fetchone()[0]

    if (ID_anfitrion == None):
        ID_anfitrion = guardarAnfitrion(anfitrion, correoAnfitrion, cursor)

    #Insertar la reunión
    cursor.execute("INSERT INTO reuniones (chat, fecha, hora, ID_cliente, ID_anfitrion) VALUES (%s, %s, %s, %s, %s)", (chat, fecha, hora, ID_cliente, ID_anfitrion))
    db.database.commit()
    return req

def editarReunion():
    return "REUNION EDITADA"

def eliminarReunion():
    cursor = db.database.cursor()
    id = request.args.get("id")
    cursor.execute("DELETE FROM reuniones WHERE ID = %s", [id])
    db.database.commit()
    return "REUNION ELIMINADA"