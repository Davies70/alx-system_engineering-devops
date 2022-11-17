#!/usr/bin/python3
'''Retrieves data using a RESTful API'''


if __name__ == '__main__':
    import json
    import requests

    filename = 'todo_all_employees.json'
    site = 'https://jsonplaceholder.typicode.com'

    users_url = site + '/users'
    users = requests.get(users_url)
    user_list = []
    for i in users.json():
        user_list.append(i.get('id'))

    users_dict = {}

    for id in user_list:
        task_url = site + '/todos?userId=' + str(id)
        user_url = users_url + '/' + str(id)
        todos = requests.get(task_url)
        user = requests.get(user_url)
        name = user.json().get('username')

        task_data = []
        for i in todos.json():
            item = {'username': name,
                    'task': i.get('title'),
                    'completed': i.get('completed')
                    }
            task_data.append(item)

        users_dict.update({str(id): task_data})

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(users_dict, f)
