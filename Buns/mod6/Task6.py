from flask import Flask, request

app = Flask(__name__)

def track_pages(f):
    if not hasattr(app, 'pages'):
        app.pages = set()

    app.pages.add(f.__name__)
    return f

@app.route('/')
@track_pages
def index():
    return 'Добро пожаловать на главную страницу!'

@app.route('/about')
@track_pages
def about():
    return 'О нас'

@app.route('/contact')
@track_pages
def contact():
    return 'Контакты'

@app.errorhandler(404)
def page_not_found(error):
    requested_url = request.path
    app.pages.add(requested_url)

    available_pages = '\n'.join(f'<a href="{page}">{page}</a>' for page in sorted(app.pages))
    return f'Страницы не найдена. Доступные страницы:\n{available_pages}', 404

if __name__ == '__main__':
    app.run()
