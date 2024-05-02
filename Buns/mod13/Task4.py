import datetime
import sqlite3

def log_bird(c: sqlite3.Cursor, bird_name: str, date_time: str) -> None:
    c.execute("INSERT INTO table_birds (bird_name, date_time) VALUES (?, ?)", (bird_name, date_time))

def check_if_such_bird_already_seen(c: sqlite3.Cursor, bird_name: str) -> bool:
    c.execute("SELECT COUNT(*) FROM table_birds WHERE bird_name = ?", (bird_name,))
    count = c.fetchone()[0]
    return count > 0

if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        log_bird(cursor, name, right_now)

        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
        else:
            print("Это новая птица для нашего заказника!")

        connection.commit()
