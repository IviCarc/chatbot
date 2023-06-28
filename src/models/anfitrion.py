from utils.db import db

class Anfitrion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(100))
    telefono = db.Column(db.Integer)
    reuniones = db.relationship('Reunion', backref='anfitrion', lazy=True)

    def __init__ (self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

