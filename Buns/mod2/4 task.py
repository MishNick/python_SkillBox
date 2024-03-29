"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask

app = Flask(__name__)


@app.route('/hello-world/<name>')
def hello_world(name):
    day_of_week = "пятницу"
    return f"Привет, {name}. Хорошей {day_of_week}!"


if __name__ == '__main__':
    app.run(debug=True)
