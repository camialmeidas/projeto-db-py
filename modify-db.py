#!/bin/python

# bibliotecas
import mysql.connector
from mysql.connector import Error
import pandas as pd

# conectando ao banco
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )   
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
        
    return connection

user = "" # Insira o usuario do banco
pwd  = "" # Insira a senha do usuario do banco
db   = "" # Insira o nome do banco que ira criar

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        
# atribuindo comando SQL para uma variavel / criando tabela
create_name_table = """
CREATE TABLE movies (
    number INT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    genre VARCHAR(40) NOT NULL,
    director VARCHAR(40) NOT NULL,
    year VARCHAR(4)
);
"""

# preenchendo tabelas
pop_movies = """
INSERT INTO movies VALUES
(1, 'A Hora do Pesadelo', 'Terror/Slasher', 'Wes Craven', '1984'),
(2, 'Interestelar', 'Ficcao Cientifica', 'Christopher Nolan', '2014'),
(3, 'O Rei Leao', 'Musical/Infantil', 'Rob Minkoff e Roger Allers', '1994'),
(4, 'Corra!', 'Terror/Thriller', 'Jordan Peele', '2017'),
(5, 'Forrest Gump', 'Drama/Romance', 'Robert Zemeckis', '1994');
"""

connection = create_db_connection("localhost", user, pwd, db) # conecta ao banco
execute_query(connection, create_name_table) # executa ou define a query
execute_query(connection, pop_movies) # executa ou define a query
