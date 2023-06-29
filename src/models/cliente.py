from utils.db import db
from utils.serializer import Serializer

class Cliente(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(100))
    telefono = db.Column(db.Integer)

    reuniones = db.relationship('Reunion', backref='cliente', lazy=True)

    def __init__ (self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    def serialize(self):
        d = Serializer.serialize(self)
        return d

