from flask import render_template, request, jsonify, Blueprint
from chat import chat

bot = Blueprint("bot", __name__)

bot.route('')
def bot_chat():
    return render_template("index.html")

bot.route('process', methods=["POST"])
def process():
    user_message = request.form["usesrInput"]
    response = chat(user_message)

    bot_message = ""

    return jsonify({'userMessage' : user_message, 'botMessage' : bot_message})
