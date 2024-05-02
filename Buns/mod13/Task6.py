import sqlite3

def ivan_sovin_the_most_effective(c: sqlite3.Cursor, name: str) -> None:
    c.execute("SELECT salary FROM table_effective_manager WHERE name = ?", (name,))
    employee_salary = c.fetchone()[0]

    c.execute("SELECT salary FROM table_effective_manager WHERE name = 'Иван Совин'")
    ivan_sovin_salary = c.fetchone()[0]

    new_employee_salary = employee_salary * 1.1

    if new_employee_salary > ivan_sovin_salary:
        c.execute("DELETE FROM table_effective_manager WHERE name = ?", (name,))
        print(f"Сотрудник {name} уволен, так как его новая зарплата больше зарплаты Ивана Совина.")
    else:
        c.execute("UPDATE table_effective_manager SET salary = ? WHERE name = ?", (new_employee_salary, name))
        print(f"Зарплата сотрудника {name} повышена до {new_employee_salary}.")

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        employee_name = input("Введите имя сотрудника: ")
        ivan_sovin_the_most_effective(cursor, employee_name)

        conn.commit()
