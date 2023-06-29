from utils.db import db
from utils.serializer import Serializer

class Reunion(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key = True)
    chat = db.Column(db.String(500))
    fechaHora = db.Column(db.DateTime)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    idAnfitrion = db.Column(db.Integer, db.ForeignKey('anfitrion.id'))

    __table_args__ = (
        db.UniqueConstraint('fechaHora', 'idCliente'),
        db.UniqueConstraint('fechaHora', 'idAnfitrion'),
      )

    def __init__ (self, chat, fechaHora, idCliente, idAnfitrion):
        self.chat = chat
        self.fechaHora = fechaHora
        self.idCliente = idCliente
        self.idAnfitrion = idAnfitrion

    def serialize(self):
        d = Serializer.serialize(self)
        del d["anfitrion"]
        del d["cliente"]
        return d