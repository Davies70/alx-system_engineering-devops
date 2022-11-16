#!/usr/bin/python3
'''Retrieves data using a RESTful API'''


if __name__ == '__main__':
    import csv
    import requests
    import sys

    id = sys.argv[1]
    filename = id + '.csv'
    site = 'https://jsonplaceholder.typicode.com'
    user_url = site + '/users/' + id
    task_url = site + '/todos?userId=' + id

    user = requests.get(user_url)
    todos = requests.get(task_url)
    name = user.json().get('username')
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    data_list = []

    for i in todos.json():
        item = {'USER_ID': id,
                'USERNAME': name,
                'TASK_COMPLETED_STATUS': i.get('completed'),
                'TASK_TITLE': i.get('title')
                }
        data_list.append(item)

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"',
                           quoting=csv.QUOTE_ALL)
        w.writerows(data_list)
