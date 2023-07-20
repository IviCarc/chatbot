from flask import Flask

from controllers.controllers import reuniones
from controllers.chat_controllers import bot

from utils.db import db
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)


CORS(app)
# Configuracion de flash_sqlalchemy
load_dotenv("./")
SQLALCHEMY_DATABASE_URI =  os.getenv("SQLALCHEMY_DATABASE_URI")


app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


app.secret_key = os.getenv("SECRET_KEY")

db.init_app(app)
# SQLAlchemy(app)

with app.app_context():
    db.create_all()

# Añadir routes como blueprints
app.register_blueprint(reuniones)
app.register_blueprint(bot)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0') 