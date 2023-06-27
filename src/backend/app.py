from flask import Flask, render_template

from controllers import getAllReuniones,getReunionById, getReunionsByCliente, agendarReunion, editarReunion, eliminarReunion
from bot_chat import bot_chat, process
app = Flask(__name__)

# API
app.add_url_rule('/chat', 'bot_chat',bot_chat, methods=["GET"])
app.add_url_rule('/process', 'process',process, methods=["GET"])

app.add_url_rule('/reuniones', 'getAllReuniones',getAllReuniones, methods=["GET"])
app.add_url_rule('/reunion', 'getReunionById',getReunionById, methods=["GET"])
app.add_url_rule('/cliente', 'getReunionsByCliente',getReunionsByCliente, methods=["GET"])
app.add_url_rule('/', 'agendarReunion',agendarReunion, methods=["POST"])
app.add_url_rule('/', 'editarReunion',editarReunion, methods=["PUT"])
app.add_url_rule('/', 'eliminarReunion',eliminarReunion, methods=["DELETE"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
