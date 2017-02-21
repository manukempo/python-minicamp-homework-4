import sqlite3

connection=sqlite3.connect('database.db')
print ('We\'re connected!')

connection.execute('CREATE TABLE IF NOT EXISTs movies(name TEXT, year INTEGER)')
print ('Table created')

connection.close()
