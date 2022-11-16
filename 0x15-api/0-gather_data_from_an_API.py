#!/usr/bin/python3
'''Write a Python script that, using this REST API, \
        for a given employee ID, \
        returns information about his/her TODO list progress.'''
import requests
import sys


if __name__ == '__main__':
    u = 'https://jsonplaceholder.typicode.com/users/{}'
    t = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    api_user = u.format(sys.argv[1])
    api_todo = t.format(sys.argv[1])
    r_user = requests.get(api_user)
    r_todo = requests.get(api_todo)

    user = r_user.json()
    todo = r_todo.json()

    num_of_tasks = len(todo)
    completed = 0
    for task in todo:
        if task.get('completed') is True:
            completed += 1

    print('Employee {} is done with tasks({}/{}):'.format(
          user.get('name'), completed, num_of_tasks))
    for task in todo:
        if task.get('completed') is True:
            print('\t {}'.format(task.get('title')))
