from utils.db import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(500))
    password = db.Column(db.String(500))
    
    def __init__ (self, username, password):
        self.username = username
        self.password = password