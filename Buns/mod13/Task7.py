import sqlite3
import random
from typing import List, Tuple

TEAMS_NAMES = [
    "Real Madrid", "Barcelona", "Bayern Munich", "Manchester United", "Liverpool",
    "Juventus", "Paris Saint-Germain", "Chelsea", "Atlético Madrid", "Borussia Dortmund",
    "Inter Milan", "Tottenham Hotspur", "Arsenal", "Ajax", "Manchester City",
    "AC Milan", "Napoli", "Sevilla", "Valencia", "Benfica",
    "Porto", "Zenit St. Petersburg", "Shakhtar Donetsk", "CSKA Moscow", "Dinamo Zagreb",
    "Galatasaray", "Fenerbahçe", "Olympiacos", "PAOK", "AEK Athens"
]

COUNTRIES = [
    "Spain", "Spain", "Germany", "England", "England",
    "Italy", "France", "England", "Spain", "Germany",
    "Italy", "England", "England", "Netherlands", "England",
    "Italy", "Italy", "Spain", "Spain", "Portugal",
    "Portugal", "Russia", "Ukraine", "Russia", "Croatia",
    "Turkey", "Turkey", "Greece", "Greece", "Greece"
]

TEAM_STRENGTHS = ["Strong", "Medium", "Weak"]

def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    if number_of_groups < 4 or number_of_groups > 16:
        raise ValueError("Number of groups must be between 4 and 16")

    c.execute("DELETE FROM uefa_commands")
    c.execute("DELETE FROM uefa_draw")

    teams = generate_teams(len(TEAMS_NAMES))

    c.executemany("INSERT INTO uefa_commands (team_id, name, country, strength) VALUES (?, ?, ?, ?)", teams)

    groups = assign_teams_to_groups(teams, number_of_groups)

    c.executemany("INSERT INTO uefa_draw (team_id, group_id) VALUES (?, ?)", groups)

def generate_teams(num_teams: int) -> List[Tuple[int, str, str, str]]:
    teams = []
    for team_id in range(1, num_teams + 1):
        name = TEAMS_NAMES[team_id - 1]
        country = COUNTRIES[team_id - 1]
        strength = random.choice(TEAM_STRENGTHS)
        teams.append((team_id, name, country, strength))
    return teams

def assign_teams_to_groups(teams: List[Tuple[int, str, str, str]], num_groups: int) -> List[Tuple[int, int]]:
    group_assignments = []
    strong_teams = [team for team in teams if team[3] == "Strong"]
    medium_teams = [team for team in teams if team[3] == "Medium"]
    weak_teams = [team for team in teams if team[3] == "Weak"]

    for group_id in range(1, num_groups + 1):
        strong_team = strong_teams.pop(0)
        medium_team1 = medium_teams.pop(0)
        medium_team2 = medium_teams.pop(0)
        weak_team = weak_teams.pop(0)

        group_assignments.append((strong_team[0], group_id))
        group_assignments.append((medium_team1[0], group_id))
        group_assignments.append((medium_team2[0], group_id))
        group_assignments.append((weak_team[0], group_id))

    return group_assignments

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        number_of_groups = int(input("Enter the number of groups (4-16): "))
        generate_test_data(cursor, number_of_groups)

        conn.commit()
