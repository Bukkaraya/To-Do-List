from flask import (Flask, render_template, url_for, g)
from models import models

app = Flask(__name__)
app.secret_key = 'sldkfj39482lkjfi30234fskdjf3498!@jjklse'

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return "Login In or Sign Up!"

@app.route('/boards', methods=('GET', 'POST'))
def display_boards():
    boards = models.Board.select()
    return render_template('boards.html', boards=boards)

@app.route('/b/<board_name>', methods=('GET', 'POST'))
def show_board_content(board_name):
    lists = (models.List.select(models.List, models.Board)
            .join(models.Board)
            .where(models.Board.board_name == board_name)
            .order_by(models.List.created_at.asc()))
    tasks = []
    for l in lists:
        tasks.append(models.Task.select(models.List, models.Task).join(models.List).where(models.List.name == l.name))

    return render_template('lists.html', lists=lists, tasks=tasks, board_name=board_name)

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
