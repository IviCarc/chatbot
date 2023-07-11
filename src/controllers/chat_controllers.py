from flask import render_template, request, jsonify, Blueprint
from chat import chat
from ingest.ingest import parse_pdf

import os

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
        file = request.files['documentos']
        print(file)

        folder_path = "src/carpetapdfs/"  
        temp_path = os.path.join(folder_path, "test.pdf")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # os.makedirs(folder_path)
        # temp_path = "test.pdf"

        file.save(temp_path)

        # Llamar a la función parse_pdf para procesar el archivo PDF
        pages, metadata = parse_pdf(temp_path)


        # Eliminar el archivo temporal
        # os.remove(temp_path)

        # Devolver el resultado del procesamiento
        return "Procesamiento completado"

    return render_template("loadPDF.html")

# @bot.route('/upload', methods=['POST'])
# def upload():
#     file = request.files
#     print(file)
#     temp_path = "temp.pdf"
#     file.save(temp_path)

#     # Llamar a la función parse_pdf para procesar el archivo PDF
#     pages, metadata = parse_pdf(temp_path)

#     # Realizar cualquier otro procesamiento adicional aquí

#     # Eliminar el archivo temporal
#     os.remove(temp_path)

#     # Devolver el resultado del procesamiento
#     return "Procesamiento completado"

    
