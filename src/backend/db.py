import mysql.connector
from dotenv import load_dotenv
import os

DBPASS = os.getenv("DBPASS")

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password=DBPASS,
    database='AsistenciaTecnica',
    auth_plugin='mysql_native_password'
)