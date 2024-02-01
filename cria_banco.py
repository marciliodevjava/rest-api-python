import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis(hotel_id text Primary KEY NOT NULL, nome text NOT NULL, estrelas real NOT NULL, diaria real NOT NULL, cidade text NOT NULL);"

cria_hotel = "INSERT INTO hoteis VALUES('alfa', 'Hotel Alfa', 4.2, 310.59, 'Rio de Janeiro')," \
             "('bravo', 'Hotel Brabo', 4.3, 340.23, 'São Paulo')," \
             "('charlie', 'Hotel Charlie', 2.2, 100.00, 'Belo Horozonte')," \
             "('delta', 'Hotel Delta', 3.8, 265.44, 'Brasília')," \
             "('echo', 'Hotel Echo', 3.5, 110.19, 'Goias')," \
             "('Fosktrot', 'Hotel Fosktrot', 4.8, 350.33, 'Brasilia');"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)
connection.commit()
connection.close()
