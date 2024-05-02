import sqlite3


def get_number_of_luckers(c: sqlite3.Cursor, month: int) -> int:
    c.execute("""
        SELECT COUNT(*)
        FROM table_occult_car_repair
        WHERE car_brand IN ('Lada', 'BMW')
          AND car_color = 'black'
          AND strftime('%d', visit_date) = '13'
          AND strftime('%m', visit_date) = ?
          AND strftime('%w', visit_date) = '5'
    """, (str(month),))

    count = c.fetchone()[0]
    return count


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        number_of_luckers = get_number_of_luckers(cursor, 6)
        print(f"В июне скидкой могли бы воспользоваться {number_of_luckers} клиентов.")
