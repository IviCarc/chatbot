from flask import Flask, render_template, request, jsonify
from frontend.chat import *

app = Flask(__name__)

@app.route('/')
def index():
    print("GET")
    return render_template('index.html')
    # return render_template("index.html")
    # return ('TEST3')

@app.route('/process', methods=['POST'])
def process():
    user_message = request.form['userInput']
    # Aquí puedes implementar la lógica de procesamiento del chatbot
    # Por ahora, solo agregaré una respuesta de ejemplo del bot
    bot_message = '¡Hola! Soy un chatbot. ¿En qué puedo ayudarte?'
    return jsonify({'userMessage': user_message, 'botMessage': bot_message})

# @app.route('/execute', methods=['POST'])
# def execute():
#     print("test")
    
if __name__ == '__main__':
    app.run(debug=True, port=80)

# app.run()