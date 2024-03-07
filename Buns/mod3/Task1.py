from datetime import datetime

from flask import Flask

app = Flask(__name__)

def test_day_of_week():
    assert day_of_week(0) == 'понедельник'
    assert day_of_week(1) == 'вторник'
    assert day_of_week(2) == 'среда'
    assert day_of_week(3) == 'четверг'
    assert day_of_week(4) == 'пятница'
    assert day_of_week(5) == 'суббота'
    assert day_of_week(6) == 'воскресенье'


def day_of_week(weekday: int) -> str:
    if weekday < 0 or weekday > 6:
        return 'некорректный день недели'

    return GREETINGS[weekday]


@app.route('/hello-world/<name>')
def hello_world(name: str) -> str:
    weekday: int = datetime.datetime.today().weekday()
    greeting: str = day_of_week(weekday)
    return f'Привет, {name}. {greeting}!'


if __name__ == '__main__':
    app.run(debug=True)
