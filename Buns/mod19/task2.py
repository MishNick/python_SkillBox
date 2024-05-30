import sqlite3

conn = sqlite3.connect('practice_and_homework_db.sqlite')
c = conn.cursor()

c.execute("""
    SELECT student_name, AVG(score) AS avg_score
    FROM submissions
    GROUP BY student_name
    ORDER BY avg_score DESC
    LIMIT 10
""")

print("Топ-10 учеников с самым высоким средним баллом:")
for row in c.fetchall():
    print(f"{row[0]} - средний балл: {row[1]:.2f}")

conn.close()
