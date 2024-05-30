import sqlite3

conn = sqlite3.connect('practice_and_homework_db.sqlite')
c = conn.cursor()

c.execute("""
    SELECT
        class_name,
        AVG(late_assignments) AS avg_late_assignments,
        MAX(late_assignments) AS max_late_assignments,
        MIN(late_assignments) AS min_late_assignments
    FROM (
        SELECT
            class_name,
            COUNT(*) AS late_assignments
        FROM submissions
        WHERE is_late = 1
        GROUP BY class_name
    )
    GROUP BY class_name
""")

print("Статистика по просроченным заданиям:")
for row in c.fetchall():
    print(f"класс: {row[0]}")
    print(f"среднее: {row[1]:.2f}")
    print(f"максимальное: {row[2]}")
    print(f"минимальное: {row[3]}")
    print()

conn.close()

#усложненная задача

c.execute("""
    SELECT
        class_name,
        AVG(late_assignments) AS avg_late_assignments,
        MAX(late_assignments) AS max_late_assignments,
        MIN(late_assignments) AS min_late_assignments
    FROM (
        SELECT
            s.class_name,
            COUNT(CASE WHEN s.is_late = 1 THEN 1 END) AS late_assignments
        FROM submissions s
        GROUP BY s.class_name
    ) AS class_stats
    GROUP BY class_name
""")

print("Статистика по просроченным заданиям:")
for row in c.fetchall():
    print(f"класс: {row[0]}")
    print(f"среднее: {row[1]:.2f}")
    print(f"максимальное: {row[2]}")
    print(f"минимальное: {row[3]}")
    print()
