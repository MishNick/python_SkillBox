"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
import subprocess
from threading import Timer


app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField()
    timeout = IntegerField()


def run_python_code_in_subproccess(code: str, timeout: int):
    timer = Timer(timeout, subprocess.TimeoutExpired)

    try:
        proc = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

        timer.start()
        stdout, stderr = proc.communicate()
        timer.cancel()

        if proc.returncode == 0:
            return stdout.decode()
        else:
            return stderr.decode()
    except subprocess.TimeoutExpired:
        proc.kill()
        return 'Execution time exceeded the specified timeout'


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data

        result = run_python_code_in_subproccess(code, timeout)

        return result
    else:
        return 'Invalid data'


if __name__ == '__main__':
    app.run(debug=True)

