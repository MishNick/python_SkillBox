import sqlite3

conn = sqlite3.connect('practice_and_homework_db.sqlite')
c = conn.cursor()

c.execute("""
    SELECT teacher_name, AVG(score) AS avg_score
    FROM submissions
    GROUP BY teacher_name
    ORDER BY avg_score ASC
    LIMIT 1
""")

result = c.fetchone()

if result:
    print(f"Преподаватель, который задает самые сложные задания: {result[0]}")
else:
    print("Не удалось найти информацию о преподавателях.")

conn.close()
