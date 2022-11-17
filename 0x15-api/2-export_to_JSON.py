#!/usr/bin/python3
'''Retrieves data using a RESTful API'''


if __name__ == '__main__':
    import json
    import requests
    import sys

    id = sys.argv[1]
    filename = id + '.json'
    site = 'https://jsonplaceholder.typicode.com'
    user_url = site + '/users/' + id
    task_url = site + '/todos?userId=' + id

    user = requests.get(user_url)
    todos = requests.get(task_url)
    name = user.json().get('username')

    task_data = []
    for i in todos.json():
        item = {'task': i.get('title'),
                'completed': i.get('completed'),
                'username': name}
        task_data.append(item)

    user_dict = {id: task_data}

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(user_dict, f)
