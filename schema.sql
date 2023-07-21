DROP TABLE IF EXISTS leaderboard;

CREATE TABLE leaderboard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    name TEXT NOT NULL,
    accuracy FLOAT NOT NULL,
    score FLOAT NOT NULL,
    time FLOAT NOT NULL
);