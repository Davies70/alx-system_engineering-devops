#!/usr/bin/python3
'''Retrieves data using a RESTful API'''


if __name__ == '__main__':
    import requests
    import sys

    id = sys.argv[1]
    site = 'https://jsonplaceholder.typicode.com'
    user_url = site + '/users/' + id
    task_done_url = site + '/todos?userId=' + id + '&completed=true'
    task_not_done_url = site + '/todos?userId=' + id + '&completed=false'

    user = requests.get(user_url)
    todos = requests.get(task_done_url)
    todos_undone = requests.get(task_not_done_url)
    task_done = len(todos.json())
    task_not_done = len(todos_undone.json())
    task_tot = task_done + task_not_done
    name = user.json().get('name')

    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          task_done,
                                                          task_tot))
    for i in todos.json():
        print('\t ' + i.get('title'))
