from app import myapp
from flask import request, abort, jsonify, make_response, render_template, redirect
import requests, json
from pprint import pprint

@myapp.route('/')
@myapp.route('/index')
def index():
    return render_template('base.html', data='Click one of the above links to test your API!')

@myapp.route('/get-all-students')
def get_all_students():
    pprint('------- GETTING ALL STUDENTS -------')
    response = requests.get('http://localhost:5000/class/api/v1/students')
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=json.loads(response.text))

#Requirement 1: Be able to search student by their ID
@myapp.route('/get-student-by-id', methods=['GET', 'POST'])
def get_student_by_id(student_id=1):
    student_id = str(request.form.get("id"))
    pprint('------- GETTING STUDENT -------')
    print(student_id)
    student_id = student_id

    if type(student_id) == int or int(student_id):
        student_id = str(student_id)
    else:
        pprint('------- ERROR - Please Specify Student Number as INT -----')

    response = requests.get('http://localhost:5000/class/api/v1/students/'+student_id)
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=json.loads(response.text))

@myapp.route('/get-student-by-id-error')
def get_student_by_id_error(student_id=100):
    pprint('------- GETTING TASK -------')

    student_id = student_id
    if type(student_id) == int or int(student_id):
        student_id = str(student_id)
    else:
        pprint('------- ERROR - PLEASE SPECIFY TASK NUMBER AS INT -------')

    response = requests.get('http://localhost:5000/class/api/v1/students/'+student_id)
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=json.loads(response.text))

#Requirement 2: Use the API you created and use the data from the form to create new student
@myapp.route('/create-new-student', methods=['GET', 'POST'])
def create_new_student(name='who this guy?', description='u should not be here!', favorite_class='who cares'):
    data = {
        'id': '',
        'name': name,
        'description': description,
        'favorite_class': favorite_class
    }

    response = requests.post('http://localhost:5000/class/api/v1/students', json=data)
    return render_template('base.html', data=json.loads(response.text))

@myapp.route('/create-new-student-error')
def create_new_student_error():
    pprint('------- CREATING TASK -------')

    data = {
    'description': ''
    }

    response = requests.post('http://localhost:5000/class/api/v1/students', json=data)
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=json.loads(response.text))
