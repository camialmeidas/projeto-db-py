#!/usr/bin/python

# Importando bibliotecas
import mysql.connector
from mysql.connector import Error
import pandas as pd

# Conectando ao MySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )   
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
        
    return connection

user = "" # insira o usuario do banco
pwd = "" # insira a senha do banco

connection = create_server_connection("localhost", user, pwd)

# Criando o banco de dados
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE movies" # variavel aplicada
create_database(connection, create_database_query) # executando a query
