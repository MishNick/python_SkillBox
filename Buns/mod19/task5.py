import sqlite3

conn = sqlite3.connect('practice_and_homework_db.sqlite')
c = conn.cursor()

# Общее количество учеников
c.execute("""
    SELECT class_name, COUNT(DISTINCT student_name) AS total_students
    FROM submissions
    GROUP BY class_name
""")
class_student_counts = {row[0]: row[1] for row in c.fetchall()}

# Средняя оценка
c.execute("""
    SELECT class_name, AVG(score) AS avg_score
    FROM submissions
    GROUP BY class_name
""")
class_avg_scores = {row[0]: row[1] for row in c.fetchall()}

# Не сдали работу
c.execute("""
    SELECT class_name, COUNT(DISTINCT student_name) AS missed_assignments
    FROM submissions
    WHERE score IS NULL
    GROUP BY class_name
""")
class_missed_assignments = {row[0]: row[1] for row in c.fetchall()}

# Просрочили дедалйн
c.execute("""
    SELECT class_name, COUNT(DISTINCT student_name) AS late_assignments
    FROM submissions
    WHERE is_late = 1
    GROUP BY class_name
""")
class_late_assignments = {row[0]: row[1] for row in c.fetchall()}

# повторные попытки
c.execute("""
    SELECT class_name, COUNT(*) AS resubmissions
    FROM submissions
    WHERE resubmission_count > 0
    GROUP BY class_name
""")
class_resubmissions = {row[0]: row[1] for row in c.fetchall()}

print("Анализ групп:")
for class_name in class_student_counts:
    print(f"класс: {class_name}")
    print(f"Общее количество учеников: {class_student_counts[class_name]}")
    print(f"Средняя оценка: {class_avg_scores[class_name]:.2f}")
    print(f"не сдали работы: {class_missed_assignments.get(class_name, 0)}")
    print(f"просрочили дедлайн: {class_late_assignments.get(class_name, 0)}")
    print(f"повторно сдают: {class_resubmissions.get(class_name, 0)}")
    print()

conn.close()
