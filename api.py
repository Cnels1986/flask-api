from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify

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
    return 'Home page'


@app.route('/games')
def index():
    cursor.execute('SELECT * FROM games')
    test = cursor.fetchall()
    print(test)

    return "whatever"
    # return jsonify(id=g.test.id,
    #                name=g.test.name,
    #                year=g.test.year,
    #                console=g.test.console)

@app.route('/games/<int:game_id>')
def show(game_id):
    cursor.execute('SELECT * FROM games WHERE id = %d' % game_id)
    test = cursor.fetchone()
    print(test)
    return 'Show game %d' % game_id

@app.route('/delete/<int:game_id>')
def delete(game_id):
    cursor.execute('DELETE FROM games WHERE id = %d' % game_id)
    return 'Delete %d' % game_id

@app.route('/update/<int:game_id>')
def update(game_id):
    return 'Update %d' % game_id

@app.route('/create')
def create():
    return 'Create'
