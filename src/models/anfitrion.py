from utils.db import db
from utils.serializer import Serializer

class Anfitrion(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(100))
    reuniones = db.relationship('Reunion', backref='anfitrion', lazy=True)

    def __init__ (self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    def serialize(self):
        d = Serializer.serialize(self)
        return d
