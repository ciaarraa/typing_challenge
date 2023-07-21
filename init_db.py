import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO leaderboard (name, accuracy, score, time) VALUES (?, ?, ?, ?)", ( 'Ciara', 1.1, 1.1, 1.1)
        )
connection.commit()
connection.close()

