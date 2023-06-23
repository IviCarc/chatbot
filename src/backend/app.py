from flask import Flask, render_template, request, jsonify
from chat import chat

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')
    # return render_template("index.html")
    # return ('TEST3')

@app.route('/process', methods=['POST'])

def process():
    user_message = request.form['userInput']
    # Aquí puedes implementar la lógica de procesamiento del chatbot
    # Por ahora, solo agregaré una respuesta de ejemplo del bot

    print(user_message) 

    chat(user_message)

    response = chat(user_message) 

    bot_message = response

    bot_question = bot_message['choices'][0]['message']['content']


    # response = chat(user_message)  
    # print (bot_message)

    return jsonify({'userMessage': user_message, 'botMessage': bot_message,'botQuestion': bot_question})
    
    
if __name__ == '__main__':
    app.run(debug=True, port=80)

# app.run()