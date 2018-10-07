from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'apidb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('index.html')

# route used for getting all the games within the table to creating a new entry to the table
@app.route('/games')
def index():
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
    # print(games)
    # response = jsonify(games)
    return render_template('gamesPage.html', games=games)
    # return response


# route is used to get a game by its id from the table
@app.route('/games/<int:game_id>')
def show(game_id):
    cursor.execute('SELECT * FROM games WHERE id = %d' % game_id)
    game = cursor.fetchone()
    response = jsonify(game)
    # return response
    return render_template('gameShow.html', game=game)
#
# # route is used to delete a row in the table based on the give id
@app.route('/delete/<int:game_id>')
def delete(game_id):
    cursor.execute('DELETE FROM games WHERE id = %d' % game_id)
    conn.commit()
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
    # response = jsonify(games)
    return render_template('gamesPage.html', games=games)
    # return response
#
# # route is used to update a row within the table
@app.route('/update/<int:game_id>')
def update(game_id):
    cursor.execute('SELECT * FROM games WHERE id = %d' % game_id)
    game = cursor.fetchone()
    return render_template('gameEdit.html', game=game)



@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        console = request.form['console']
        year = request.form['year']
        print('INSERT INTO games (name, year, console) VALUES (%s, %s, %s)' % (name, int(year), console))
        # cursor.execute('INSERT INTO games (name, year, console) VALUES (%s, %d, %s)' % (name, int(year), console))
        cursor.execute("INSERT INTO games (name, year, console) VALUES ('{}','{}','{}')".format(name, int(year), console))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('gameForm.html')
