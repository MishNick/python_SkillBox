import json

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')

    if path == '/hello':
        status = '200 OK'
        response_headers = [('Content-Type', 'application/json')]
        start_response(status, response_headers)
        return [json.dumps({'message': 'Hello, World!'}).encode()]
    elif path.startswith('/hello/'):
        name = path.split('/')[-1]
        status = '200 OK'
        response_headers = [('Content-Type', 'application/json')]
        start_response(status, response_headers)
        return [json.dumps({'message': f'Hello, {name}!'}).encode()]
    else:
        status = '404 Not Found'
        response_headers = [('Content-Type', 'application/json')]
        start_response(status, response_headers)
        return [json.dumps({'error': 'Not found'}).encode()]

'''Задание 2:
Для того, чтобы Nginx мог обслуживать статические файлы, нужно добавить следующую конфигурацию в ваш Nginx-конфиг:
location /static/ {
    alias /path/to/your/static/files/; - заменить путь на фактический
    
}'''
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


#задание 3
import time
from flask import Flask, jsonify

app = Flask(name)


@app.route('/long_task)
def long_task():
   proxy_read_timeout 300; #устанавливает таймаут на 5 мин
   return jsonify(message='We did it!')