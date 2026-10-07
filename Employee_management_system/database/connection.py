import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():

    connection= pyodbc.connect(os.getenv("DATABASE_URL"))

    print("Connected!")
    return connection
