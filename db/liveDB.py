import sqlite3

DATABASE = "db/database.db"

CREATE_SCHEMA = '''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_title TEXT NOT NULL,
    rating FLOAT NOT NULL,
    certified_fresh BOOL NOT NULL
)
'''
VIEW_FOR_TOP = '''
    CREATE VIEW IF NOT EXISTS top AS
    SELECT movie_title, rating
    FROM movies
    WHERE certified_fresh = 1
    ORDER BY rating DESC
    LIMIT 10;
'''

INSERT_QUERY = "INSERT INTO movies (rating, movie_title, certified_fresh) VALUES (?, ?, ?)"

#Default fuction for SQL lite
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


def close_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(CREATE_SCHEMA)
    dataWithOutID = [row[1:] for row in data]
    #print(dataWithOutID)
    cursor.executemany(INSERT_QUERY, dataWithOutID)
    conn.commit()
    cursor.execute(VIEW_FOR_TOP)
    conn.commit()
    conn.close()

def getMovies():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Enables dict-like access
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    conn.close()
    #Make it readble for the json response
    movies = [dict(row) for row in rows]
    return movies

def getMoviesTop():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Enables dict-like access
    cur = conn.cursor()
    cur.execute("SELECT * FROM top")
    rows = cur.fetchall()
    conn.close()
    #Make it readble for the json response
    movies = [dict(row) for row in rows]
    return movies