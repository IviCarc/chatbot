from flask import Flask
from chat import chat

from controllers.controllers import reuniones
from controllers.chat_controllers import bot_chat, process

from utils.db import db

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)


# Configuracion de flash_sqlalchemy
load_dotenv("./")
SQLALCHEMY_DATABASE_URI =  os.getenv("SQLALCHEMY_DATABASE_URI")

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)
# SQLAlchemy(app)

with app.app_context():
    db.create_all()


# API
# app.add_url_rule('/', 'bot_chat',bot_chat, methods=["GET"])
# app.add_url_rule('/process', 'process',process, methods=["GET"])

# app.add_url_rule('/reuniones', 'getAllReuniones',getAllReuniones, methods=["GET"])
# app.add_url_rule('/reunion', 'getReunionById',getReunionById, methods=["GET"])
# app.add_url_rule('/cliente', 'getReunionsByCliente',getReunionsByCliente, methods=["GET"])
# app.add_url_rule('/', 'agendarReunion',agendarReunion, methods=["POST"])
# app.add_url_rule('/', 'editarReunion',editarReunion, methods=["PUT"])
# app.add_url_rule('/', 'eliminarReunion',eliminarReunion, methods=["DELETE"])


# Añadir routes como blueprints
app.register_blueprint(reuniones)

if __name__ == '__main__':
    app.run(debug=True, port=80)