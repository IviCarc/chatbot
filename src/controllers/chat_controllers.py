from flask import render_template, request, jsonify, Blueprint
from chat import chat

bot = Blueprint("bot", __name__)

@bot.route('/')
def bot_chat():
    return render_template("index.html")


@bot.route('/process', methods=["POST"])
def process():
    user_message = request.form["userInput"]
    print(user_message)
    answer = chat(user_message)
    print(answer)

    return jsonify({'userMessage' : user_message, 'botMessage' : answer})

@bot.route('/loadPDF', methods=["POST", "GET"])
def loadPDF():
    if request.method == "POST":
        return

    return render_template("loadPDF.html")

    
