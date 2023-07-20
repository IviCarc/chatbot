import smtplib,  os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
def enviarCorreo(destinatario, nombre, telefono, fechaHora, asunto, reunion_id, correoCliente):

    load_dotenv("./")
    
    remitente = os.getenv("EMAIL_USER")  # Coloca tu dirección de correo electrónico
    clave = os.getenv("EMAIL_PASSWORD")  # Coloca tu contraseña
    fecha, hora = fechaHora.split(' ')

    # Crea el objeto SMTP y establece la conexión
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(remitente, clave)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"{asunto}"
    msg['From'] = remitente
    msg['To'] = destinatario


    # Crea el mensaje de correo electrónico
    html = f"""
            <html>
            <head></head>
            <body>
                <h2>Se ha agendado una reunion con {nombre} el dia {fecha} a las {hora}<h2>
                <h3>Telefono: {telefono}</h3> 
                <h3>Correo: {correoCliente}</h3>
                <button><a href='http://{os.getenv('URL')}/reuniones/{reunion_id}'>Repogramar reunion</a></button>
            </body>
            </html>
            """

    msg.attach(MIMEText(html, 'html'))

    # Envía el correo electrónico
    server.sendmail(remitente, destinatario, msg.as_string())

    # Cierra la conexión SMTP
    server.quit()