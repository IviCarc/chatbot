from Flask import render_template, request, jsonify
from chat import chat

def bot_chat():
    return render_template("index.html")

def process():
    user_message = request.form["usesrInput"]
    response = chat(user_message)

    return jsonify({'userMessage' : user_message, 'botMessage' : bot_message})