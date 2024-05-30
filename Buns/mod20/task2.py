from datetime import datetime
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, ReceivingBooks, Student

app = Flask(__name__)

# Подключение к базе данных
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/books', methods=['GET'])
def get_books():
    session = Session()
    books = session.query(Book).all()
    return jsonify([book.__dict__ for book in books])

@app.route('/debtors', methods=['GET'])
def get_debtors():
    session = Session()
    debtors = session.query(ReceivingBooks).filter(ReceivingBooks.date_of_return == None).filter(ReceivingBooks.count_date_with_book > 14).all()
    return jsonify([debtor.__dict__ for debtor in debtors])

@app.route('/issue_book', methods=['POST'])
def issue_book():
    book_id = request.form['book_id']
    student_id = request.form['student_id']
    session = Session()
    book = session.query(Book).get(book_id)
    student = session.query(Student).get(student_id)
    if book and student:
        receiving_book = ReceivingBooks(book_id=book_id, student_id=student_id, date_of_issue=datetime.now())
        session.add(receiving_book)
        session.commit()
        return 'Book issued successfully'
    else:
        return 'Invalid book or student ID', 400

@app.route('/return_book', methods=['POST'])
def return_book():
    book_id = request.form['book_id']
    student_id = request.form['student_id']
    session = Session()
    receiving_book = session.query(ReceivingBooks).filter_by(book_id=book_id, student_id=student_id, date_of_return=None).first()
    if receiving_book:
        receiving_book.date_of_return = datetime.now()
        session.commit()
        return 'Book returned successfully'
    else:
        return 'Invalid book or student ID', 400

    @app.route('/search_books', methods=['GET'])
    def search_books():
        query = request.args.get('query')
        session = Session()
        books = session.query(Book).filter(Book.name.contains(query)).all()
        return jsonify([book.__dict__ for book in books])

    if __name__ == '__main__':
        app.run(debug=True)
