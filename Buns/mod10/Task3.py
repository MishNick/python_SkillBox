import sqlite3

#Task1
with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM table_1")
    table_1_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM table_2")
    table_2_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM table_3")
    table_3_count = cursor.fetchone()[0]

print(f"Количество записей в таблице table_1: {table_1_count}")
print(f"Количество записей в таблице table_2: {table_2_count}")
print(f"Количество записей в таблице table_3: {table_3_count}")

#Task2
with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT value) FROM table_1")
    unique_table_1_count = cursor.fetchone()[0]

print(f"Количество уникальных записей в таблице table_1: {unique_table_1_count}")

#Task3
with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM table_1 WHERE id IN (SELECT id FROM table_2)")
    common_table_1_2_count = cursor.fetchone()[0]

print(f"Количество записей из таблицы table_1, встречающихся в table_2: {common_table_1_2_count}")

#Task4
with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM table_1 WHERE id IN (SELECT id FROM table_2) AND id IN (SELECT id FROM table_3)")
    common_table_1_2_3_count = cursor.fetchone()[0]

print(f"Количество записей из таблицы table_1, встречающихся и в table_2, и в table_3: {common_table_1_2_3_count}")
