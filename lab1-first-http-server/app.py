#imports
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

#data
students = [['student1', 5], ['student2', 4], ['student3', 3], ['student4', 2]]
courses = ['course1', 'course2', 'course3', 'course4']

#base log (time/method/path)
@app.before_request
def log_request():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] {request.method} {request.path}")

#main route endpoint
@app.route('/')
def home():
    return 'welcome to the base server'

#students
@app.route('/api/students')
def all_students():
    return jsonify({'students': students})

#courses
@app.route('/api/courses')
def all_courses():
    return jsonify({'courses': courses})

#students info
@app.route('/api/students/<int:student_id>')
def get_student(student_id):
    if (student_id>=0 and student_id<len(students)):
        return jsonify({'student_name': students[student_id][0], 'student_grade': students[student_id][1]})
    else:
        return jsonify({'no info for that student': 'try 0, 1, 2 or 3'})

#404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    app.run(port = 3000, debug=True)