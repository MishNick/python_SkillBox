import sqlite3

with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("Ваш SQL-запрос")
    results = cursor.fetchone()

poverty_percentage = results[0]
average_salary = results[1]
median_salary = results[2]
inequality_percentage = results[3]

print(f"Процент населения, находящегося за чертой бедности: {poverty_percentage:.2f}%")
print(f"Средняя зарплата по острову: {average_salary:.2f}")
print(f"Медианная зарплата по острову: {median_salary:.2f}")
print(f"Процент социального неравенства F: {inequality_percentage:.2f}%")
