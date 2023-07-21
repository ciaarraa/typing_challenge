import os
import sqlite3

from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__) 

@app.route('/leaderboard')
def leaderboard():
    conn = get_db_connection()
    leaderboard = conn.execute('SELECT * FROM leaderboard').fetchall()
    conn.close()
    return render_template('leaderboard.html', leaderboard=leaderboard)

@app.route('/how-to-play')
def how_to_play():
    return render_template('how_to_play.html')

@app.route('/')
def index():
    return render_template('index.html')
