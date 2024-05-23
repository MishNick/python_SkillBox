import sqlite3

conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# Таблица "actors"
c.execute("""CREATE TABLE actors (
    act_id INTEGER PRIMARY KEY,
    act_first_name TEXT,
    act_last_name TEXT,
    act_gender TEXT
)""")

# Таблица "movie_cast"
c.execute("""CREATE TABLE movie_cast (
    act_id INTEGER,
    mov_id INTEGER, 
    role TEXT,
    FOREIGN KEY (act_id) REFERENCES actors(act_id),
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
)""")

# Таблица "movie"
c.execute("""CREATE TABLE movie (
    mov_id INTEGER PRIMARY KEY,
    mov_title TEXT
)""")

# Таблица "oscar_awarded"
c.execute("""CREATE TABLE oscar_awarded (
    award_id INTEGER PRIMARY KEY,
    mov_id INTEGER,
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
)""")

# Таблица "director"
c.execute("""CREATE TABLE director (
    dir_id INTEGER PRIMARY KEY,
    dir_first_name TEXT,
    dir_last_name TEXT
)""")

# Таблица "movie_direction"
c.execute("""CREATE TABLE movie_direction (
    dir_id INTEGER,
    mov_id INTEGER,
    FOREIGN KEY (dir_id) REFERENCES director(dir_id),
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
)""")

conn.commit()
conn.close()
