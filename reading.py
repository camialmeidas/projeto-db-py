#!/bin/python

import mysql.connector
from mysql.connector import Error
import pandas as pd


# conectando database movies
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conectado ao banco de dados MOVIES. Lendo dados...")
    except Error as err: 
        print(f"Error: '{err}'")

    return connection

user = "" # Insira o usuario do banco
pwd  = "" # Insira a senha do usuario do banco
db   = "" # Insira o nome do banco que ira criar

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

q1 = """
SELECT * 
FROM movies;
"""

connection = create_db_connection("localhost", user, pwd, db) # conecta ao banco
results = read_query(connection, q1) # executa results

for result in results:
    print(result)
