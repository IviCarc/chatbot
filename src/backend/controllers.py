from flask import request
import db as db
import json
import datetime

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

# def getReunionByCliente():
    # cursor = db.database.cursor()
    # id = request.args.get("id")
    # cursor.execute("SELECT * FROM reuniones WHERE ID = %s", [id])
    # row_headers=[x[0] for x in cursor.description]
    # reunion = cursor.fetchall()

    # return serialize(reunion, row_headers)

def agendarReunion():
    req = request.get_json()
    return req

def editarReunion():
    return "REUNION EDITADA"

def eliminarReunion():
    return "REUNION ELIMINADA"