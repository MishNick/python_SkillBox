import datetime
from flask import Flask
import random
from datetime import datetime, timedelta
import os
import re


app = Flask(__name__)

cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['VISITS'] = 0 #хранение значения счетчика

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def get_cars():
    return ', '.join(cars)


@app.route('/cats')
def get_random_cat():
    random_cat = random.choice(cats)
    return random_cat


@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_after_hour():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    words = get_word_list_from_file()
    random_word = random.choice(words)
    return random_word


@app.route('/counter')
def counter():
    return f'Страница была посещена {app.config["VISITS"]} раз(а)'

@app.before_request
def increment_counter():
    app.config['VISITS'] += 1

counter.visits = 0


if __name__ == '__main__':
    app.run(debug=True)

def get_word_list_from_file():
    book_file = os.path.join(BASE_DIR, 'war_and_peace.txt')
    with open(book_file) as book:
        text = book.read()
        words = re.findall(r'\b\w+\b', text)
        return words