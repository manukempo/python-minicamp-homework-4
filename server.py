from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods=['POST'])
def movie():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()

    name=request.form['name']
    year=request.form['year']

    try:
        cursor.execute('INSERT INTO movies(name,year) VALUES(?,?)', (name,year))
        connection.commit()
        message = 'Successfully inserted into movies'
    except:
        connection.rollback()
        message = 'There was an issue inserting data'
    finally:
        connection.close()
        return message

@app.route('/movies')
def movies():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM movies')
    moviesList=cursor.fetchall()
    connection.close()
    return jsonify(moviesList)

@app.route('/search')
def search():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    name=request.args['name']
    cursor.execute('SELECT * FROM movies WHERE name=?',(name,))
    movie=cursor.fetchone()
    return jsonify(movie)

app.run(debug=True)
