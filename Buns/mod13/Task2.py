import sqlite3

def check_if_vaccine_has_spoiled(c: sqlite3.Cursor, truck_number: str) -> bool:
    c.execute("SELECT temperature, timestamp FROM table_truck_with_vaccine WHERE truck_number = ? ORDER BY timestamp", (truck_number,))
    temperature_records = c.fetchall()


    if not temperature_records:
        return False

    #температурный режим
    bad_temperature_hours = 0
    for temperature, timestamp in temperature_records:
        if temperature < -20 or temperature > -16:
            bad_temperature_hours += 1
        else:
            bad_temperature_hours = 0

        if bad_temperature_hours >= 3:
            return True

    return False