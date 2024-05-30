import sqlite3

conn = sqlite3.connect('practice_and_homework_db.sqlite')
c = conn.cursor()

c.execute("""
    SELECT AVG(score) AS avg_score
    FROM submissions
    WHERE assignment_id IN (
        SELECT assignment_id
        FROM assignments
        WHERE type = 'reading_and_learn'
    )
""")

result = c.fetchone()
print(f"Средняя оценка за задания, где нужно было что-то прочитать и выучить: {result[0]:.2f}")

conn.close()
