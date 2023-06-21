def preguntar (pregunta):
    respuesta = input("\n" + pregunta + "\n")
    return respuesta

def agendar (reunion):

    reunion["nombre"] = preguntar("Cuál es tu nombre?")
    reunion["email"] = preguntar("Cuál es tu email?")
    reunion["telefono"] = preguntar("Cuál es tu teléfono?")

    print(reunion)