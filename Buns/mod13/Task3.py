import sqlite3
import csv

def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, 'r') as file:
        reader = csv.reader(file)
        wrong_fees = [(date, number) for date, number in reader]

    for date, number in wrong_fees:
        c.execute("DELETE FROM table_fees WHERE date = ? AND number = ?", (date, number))

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, "wrong_fees.csv")
        conn.commit()
