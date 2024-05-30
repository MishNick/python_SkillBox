import csv
from flask import app, request
from sqlalchemy.orm import Session
from task1 import Student


@app.route('/upload_students', methods=['POST'])
def upload_students():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        session = Session()
        reader = csv.DictReader(file, delimiter=';')
        students = []
        for row in reader:
            student = Student(
                name=row['name'],
                surname=row['surname'],
                phone=row['phone'],
                email=row['email'],
                average_score=float(row['average_score']),
                scholarship=bool(row['scholarship'])
            )
            students.append(student)

        session.bulk_insert_mappings(Student, [s.__dict__ for s in students])
        session.commit()
        return 'Students uploaded successfully'
