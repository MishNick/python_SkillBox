import requests
import sqlite3
import time

def create_table():
    conn = sqlite3.connect('starwars.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS characters
                 (name TEXT, age INTEGER, gender TEXT)''')
    conn.commit()
    conn.close()

def save_character(character):
    conn = sqlite3.connect('starwars.db')
    c = conn.cursor()
    c.execute("INSERT INTO characters VALUES (?, ?, ?)", character)
    conn.commit()
    conn.close()

def sequential_requests():
    create_table()
    start_time = time.time()

    for i in range(20):
        response = requests.get(f"https://swapi.dev/api/people/{i+1}/")
        data = response.json()
        character = (data['name'], int(data['birth_year']), data['gender'])
        save_character(character)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Sequential requests took {execution_time} seconds")

def parallel_requests():
    create_table()
    start_time = time.time()

    responses = []
    for i in range(20):
        response = requests.get(f"https://swapi.dev/api/people/{i+1}/")
        responses.append(response)

    for response in responses:
        data = response.json()
        character = (data['name'], int(data['birth_year']), data['gender'])
        save_character(character)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Parallel requests took {execution_time} seconds")

if __name__ == "__main__":
    sequential_requests()
    parallel_requests()
