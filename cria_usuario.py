import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS usuario(user_id INTEGER Primary KEY NOT NULL, nome VARCHAR(100) NOT NULL, login VARCHAR(100) NOT NULL, senha VARCHAR(100) NOT NULL);"


cursor.execute(cria_tabela)
connection.commit()
connection.close()
