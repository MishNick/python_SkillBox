import sqlite3

conn = sqlite3.connect('practice_and_homework_db.sqlite')
c = conn.cursor()

c.execute("""
    SELECT teacher_name
    FROM submissions
    GROUP BY teacher_name
    ORDER BY AVG(score) DESC
    LIMIT 1
""")
best_teacher = c.fetchone()[0]

c.execute("""
    SELECT student_name
    FROM submissions
    WHERE teacher_name = ?
    GROUP BY student_name
""", (best_teacher,))

print(f"Ученики преподавателя, который задает самые простые задания ({best_teacher}):")
for row in c.fetchall():
    print(row[0])

conn.close()


#усложненная задача
c.execute("""
    SELECT teacher_name
    FROM submissions
    GROUP BY teacher_name
    ORDER BY AVG(score) DESC
    LIMIT 1
""")
best_teacher = c.fetchone()[0]

c.execute("""
    SELECT DISTINCT student_name
    FROM submissions
    WHERE teacher_name = (
        SELECT teacher_name
        FROM submissions
        GROUP BY teacher_name
        ORDER BY AVG(score) DESC
        LIMIT 1
    )
""")

print(f"Ученики преподавателя, который задает самые простые задания ({best_teacher}):")
for row in c.fetchall():
    print(row[0])


