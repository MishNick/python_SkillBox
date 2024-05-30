from datetime import datetime
from flask import jsonify, app
from numpy import extract
from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from task1 import Author, Student, Book, ReceivingBooks


@app.route('/books_by_author/<int:author_id>', methods=['GET'])
def get_books_by_author(author_id):
    session = Session()
    author = session.query(Author).get(author_id)
    if author:
        return jsonify([book.__dict__ for book in author.books])
    else:
        return 'Author not found', 404

@app.route('/unread_books_by_author/<int:student_id>', methods=['GET'])
def get_unread_books_by_author(student_id):
    session = Session()
    student = session.query(Student).get(student_id)
    if student:
        read_books = [rb.book for rb in student.receiving_books]
        unread_books = session.query(Book).filter(~Book.id.in_([b.id for b in read_books])).all()
        return jsonify([book.__dict__ for book in unread_books])
    else:
        return 'Student not found', 404

@app.route('/average_books_per_month', methods=['GET'])
def get_average_books_per_month():
    session = Session()
    current_year = datetime.now().year
    current_month = datetime.now().month
    receiving_books = session.query(ReceivingBooks) \
                      .filter(extract('year', ReceivingBooks.date_of_issue) == current_year) \
                      .filter(extract('month', ReceivingBooks.date_of_issue) == current_month) \
                      .all()
    total_books = len(receiving_books)
    total_students = session.query(Student).count()
    average_books_per_month = total_books / total_students
    return jsonify({'average_books_per_month': average_books_per_month})

@app.route('/most_popular_book_for_high_score', methods=['GET'])
def get_most_popular_book_for_high_score():
    session = Session()
    high_score_students = session.query(Student).filter(Student.average_score > 4.0).all()
    receiving_books = session.query(ReceivingBooks) \
        .filter(ReceivingBooks.student_id.in_([s.id for s in high_score_students])) \
        .group_by(ReceivingBooks.book_id) \
        .order_by(func.count(ReceivingBooks.book_id).desc()) \
        .first()
    if receiving_books:
        book = session.query(Book).get(receiving_books.book_id)
        return jsonify(book.__dict__)
    else:
        return 'No books found for high score students', 404


@app.route('/top_reading_students', methods=['GET'])
def get_top_reading_students():
    session = Session()
    current_year = datetime.now().year
    top_students = session.query(Student, func.count(ReceivingBooks.id).label('total_books')) \
        .join(ReceivingBooks) \
        .filter(extract('year', ReceivingBooks.date_of_issue) == current_year) \
        .group_by(Student.id) \
        .order_by(desc('total_books')) \
        .limit(10) \
        .all()
    return jsonify([{'name': s.name, 'surname': s.surname, 'total_books': tb} for s, tb in top_students])
