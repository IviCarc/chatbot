from utils.db import db

class Reunion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    chat = db.Column(db.String(500))
    fechaHora = db.Column(db.DateTime)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    idAnfitrion = db.Column(db.Integer, db.ForeignKey('anfitrion.id'))

    def __init__ (self, chat, fechaHora, idCliente, idAnfitrion):
        self.chat = chat
        self.fechaHora = fechaHora
        self.idCliente = idCliente
        self.idAnfitrion = idAnfitrion