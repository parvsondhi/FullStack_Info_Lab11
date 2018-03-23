import requests, json
from pprint import pprint


def get_all_tasks():
	print
	print '------- GETTING ALL TASKS -------'
	print

	response = requests.get('http://localhost:5000/todo/api/v1/tasks')
	decodedResponse = response.json()
	pprint(decodedResponse)


def get_task_by_id(task_id):
	print
	print '------- GETTING TASK', task_id, '-------'
	print

	task_id = task_id
	if type(task_id) == int or int(task_id):
		task_id = str(task_id)
	else:
		print '------- ERROR - PLEASE SPECIFY TASK NUMBER AS INT -------'

	response = requests.get('http://localhost:5000/todo/api/v1/tasks/'+task_id)
	decodedResponse = response.json()
	pprint(decodedResponse)

def create_task(title, description=''):
	print
	print '------- CREATING TASK -------'
	print

	data = {
	'title': title,
	'description': description
	}

	response = requests.post('http://localhost:5000/todo/api/v1/tasks', json=data)
	decodedResponse = response.json()
	pprint(decodedResponse)




if __name__ == '__main__':
	get_all_tasks()
	get_task_by_id(1)
	get_task_by_id(3)
	create_task('testing')