from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/games')
def index():
    return 'Games page'

@app.route('/games/<int:game_id>')
def show(game_id):
    return 'Show game %d' % game_id

@app.route('/delete/<int:game_id>')
def delete(game_id):
    return 'Delete %d' % game_id

@app.route('/update/<int:game_id>')
def update(game_id):
    return 'Update %d' % game_id

@app.route('/create')
def create():
    return 'Create'
