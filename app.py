from flask import Flask, jsonify, request

app = Flask(__name__)


# 1. Home
@app.route('/')
def home():
    return "Welcome to John Michael Apostol's API!"


# 2. Student Information
@app.route('/my-information')
def student():
    return jsonify({
        "name": "John Michael Apostol",
        "student_id": "24-00143",
        "program": "BSIT",
        "year": 3,
        "section": "DIJKSTRA"
    })


# 3. Greeting
@app.route('/say-hello')
def hello():
    name = request.args.get('name', 'John Michael Apostol')

    return jsonify({
        "message": f"Hello, {name}!"
    })


# 4. Course Information
@app.route('/my-course')
def course():
    return jsonify({
        "course_code": "IT 3120",
        "course_title": "Activity 3",
        "instructor": "Rene Arduo",
        "semester": "First Semester",
        "academic_year": "2026-2027"
    })


# 5. Welcome Message
@app.route('/student-welcome')
def greet():
    name = request.args.get('name', 'John Michael Apostol')
    section = request.args.get('section', 'DIJKSTRA')

    return jsonify({
        "message": f"Hello {name} from {section}!"
    })


# 6. Student Details
@app.route('/student-details')
def profile():
    return jsonify({
        "student_id": "24-00143",
        "name": "John Michael Apostol",
        "program": "BSIT",
        "year": 3,
        "section": "DIJKSTRA",
        "religion": "Baptist",
        "email": "johnmichaelapostol.isufst.edu.ph",
        "hobbies": "Reading"
    })


# Run the API
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )