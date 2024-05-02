import sqlite3
from collections import defaultdict

SPORT_DAYS = {
    "football": 0,  # Monday
    "hockey": 1,    # Tuesday
    "chess": 2,     # Wednesday
    "SUP surfing": 3,  # Thursday
    "boxing": 4,    # Friday
    "Dota2": 5,     # Saturday
    "chess boxing": 6,  # Sunday
}

def update_work_schedule(c: sqlite3.Cursor) -> None:
    c.execute("SELECT employee_id, shift_day FROM table_work_schedule")
    schedule = c.fetchall()

    employee_preferences = defaultdict(list)

    for employee_id, shift_day in schedule:
        c.execute("SELECT sport FROM table_employee_preferences WHERE employee_id = ?", (employee_id,))
        sport = c.fetchone()[0]
        preferred_day = SPORT_DAYS[sport]
        employee_preferences[employee_id].append(preferred_day)

    if not can_accommodate_preferences(schedule, employee_preferences):
        print("It's not possible to accommodate all employee preferences.")
        return

    updated_schedule = []
    for employee_id, shift_day in schedule:
        preferred_days = employee_preferences[employee_id]
        new_shift_day = find_available_shift_day(shift_day, preferred_days)
        updated_schedule.append((employee_id, new_shift_day))

    c.executemany("UPDATE table_work_schedule SET shift_day = ? WHERE employee_id = ?", updated_schedule)

def can_accommodate_preferences(schedule, employee_preferences):
    day_counts = [0] * 7

    for employee_id, shift_day in schedule:
        preferred_days = employee_preferences[employee_id]
        if shift_day not in preferred_days:
            day_counts[shift_day] += 1

    return all(count <= 10 for count in day_counts)

def find_available_shift_day(current_day, preferred_days):
    for day in preferred_days:
        if day != current_day:
            return day
    return current_day

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        update_work_schedule(cursor)
        conn.commit()
