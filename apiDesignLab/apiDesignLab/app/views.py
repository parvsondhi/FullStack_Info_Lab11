from app import myapp
from flask import request, abort, jsonify, make_response, render_template, redirect, json

@myapp.route('/')
@myapp.route('/class/api')
def index():
    return render_template('api.html')

#return all students
@myapp.route('/class/api/v1/students', methods=['GET'])
def get_students():
    returned_object = {}
    returned_object['students'] = students
    print(returned_object)
    return json.dumps({'students': students})

#return a specific student given an id
@myapp.route('/class/api/v1/students/<int:student_id>', methods=['GET', 'POST'])
def get_student(student_id):
    for student in students:
        if student.get('id')==student_id:
            return json.dumps(student)
    return redirect(404)

@myapp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#Requirement 2: Create an API for creating a new student in our memory database
@myapp.route('/class/api/v1/students', methods=['POST'])
def create_student():
    if not request.json or not 'name' in request.json:
        abort(400)

    # Step 1 - Create a dictionary named return here with id, name, description, and favorite_class
    # fields filled out. Use request.json function to get the data coming from the client request

    # Step 2 - Append this to the list students

    return json.dumps(return_json)

@myapp.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request - make sure to specify a student name'}), 400)

students = [
    {
        'id': 1,
        'name': u'Mattew Bayley',
        'description': u'likes littlest bear',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 2,
        'name': u'Bo Brandt',
        'description': u'likes financial data',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 3,
        'name': u'Bo Brandt',
        'description': u'likes pokemon',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 4,
        'name': u'Michelle Carney',
        'description': u'likes plants and coconut octopus',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 5,
        'name': u'Nolan Chao',
        'description': u'likes NOSQL',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 6,
        'name': u'Michael Peter Froehlich',
        'description': u'likes edge cases',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 7,
        'name': u'Roham Ghotbi',
        'description': u'likes blockchain',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 8,
        'name': u'Amy Huang',
        'description': u'likes hats',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 9,
        'name': u'Devin Huang',
        'description': u'likes flask',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 10,
        'name': u'Conner Hunihan',
        'description': u'likes javascript',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 11,
        'name': u'Eric Huynh',
        'description': u'likes Carlos Hawaian Shirt',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 12,
        'name': u'Dimitris Hytiroglou',
        'description': u'loves ajax but hates JQuery',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 13,
        'name': u'Daphne Jong',
        'description': u'only writes in vanilla javascript',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 14,
        'name': u'Jin Kweon',
        'description': u'only drinks with flask',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 15,
        'name': u'Ching-Yi Lin',
        'description': u'likes napping under the sun',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 16,
        'name': u'Yu-Cheng Lin',
        'description': u'loves late night class',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 17,
        'name': u'Andrew Liu',
        'description': u'likes the campanille',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 18,
        'name': u'Nicolas Mon',
        'description': u'likes Object Recognition and the Lakers',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 19,
        'name': u'Joshua Park',
        'description': u'likes jinja templates',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 20,
        'name': u'Peter Rowland',
        'description': u'likes trees and graphs',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 21,
        'name': u'Bonney Ruan',
        'description': u'likes database modeling',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 22,
        'name': u'Carina Sauter',
        'description': u'likes Jacob Hall',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 23,
        'name': u'Haile Shavers',
        'description': u'likes Google Chrome Developer Tool',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 24,
        'name': u'Sheng Tan',
        'description': u'likes JSON',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 25,
        'name': u'Natalia Timakova',
        'description': u'likes the last semester of school',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 26,
        'name': u'Matthew Waliman',
        'description': u'likes image recognition',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 27,
        'name': u'Sipian Wang',
        'description': u'likes coding',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 28,
        'name': u'Jing Xiong',
        'description': u'likes Mayday',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 29,
        'name': u'Peiyu Yang',
        'description': u'likes California weather',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 30,
        'name': u'Jeffery Yu',
        'description': u'loves traveling',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 31,
        'name': u'Yue Zhang',
        'description': u'loves to picnic',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 32,
        'name': u'Parv Sondhi',
        'description': u'does not buy tickets on Stubhubs',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 33,
        'name': u'Carlo Liquido',
        'description': u'loves Hawaii music',
        'favorite_class': u'INFO 290T'
    },
    {
        'id': 34,
        'name': u'Daniel Chen',
        'description': u'loves blockchain',
        'favorite_class': u'INFO 290T'
    }
]
