# 💬 Chatbot PDF 

## 👷️ Architectura

Este documento explicara la arquitectura y conceptos para poder usar facilmente el chatbot. Usando LangChain, ChromaDB y OpenAI's API.

## 💻 Empezando

### Requisitos previos

Se necesitara utilizar la version 3.10 de Python y Pipenv. 

Nota: Para usuarios de **Windows**,  es posible que deba eliminar `Pipfile.lock` antes de continuar con la instalación.

### Archivos de configuración

En el directorio del proyecto, existe un archivo “.env”. Este es un archivo que se encarga de almacenar variables de entorno sensibles, que no pueden figurar en el código ya que comprometen la seguridad del sistema, pero son necesarios. 
El programa se encarga de leerlos directamente desde el archivo.

URL: Esta variable se encarga de definir todos los endpoint a los que debe dirigirse la API.

OPENAI_API_KEY: Esta es la clave brindada por OpenAI para hacer uso de sus servicios. Debe obtenerse desde una cuenta en la misma.

DBPASS: La contraseña de la base de datos.

SQLALCHEMY_DATABASE_URI: El string de conexión que requiere SQLAlchemy para conectarse a la DB.

SECRET_KEY: Es una clave definida para el uso seguro de variables de configuración dentro de Flask.

EMAIL_USER: El correo electrónico desde el cual se enviarán los mails hacia los anfitriones.

EMAIL_PASSWORD: Una contraseña válida para ese mail. En caso de utilizar un Gmail, deberán brindarse permisos especiales a dicho correo electrónico y generar una contraseña de aplicación. Ver la documentación para cada tipo de correo electrónico.


### Instalación

1. Instalar las dependencias requeridas usando Pipenv: 

```bash
pipenv install
```

2. Activar el Pipenv shell:

```bash
pipenv shell
```

3. Empezar a usar el Chatbot:

```bash
pipenv run dev
```

## 🔗 Links utiles

- OpenAI: https://platform.openai.com/ 
- LangChain: https://python.langchain.com/en/latest/index.html  
- Chroma DB: https://docs.trychroma.com/ 




