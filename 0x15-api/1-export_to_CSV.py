#!/usr/bin/python3
"""a script that returns info about employee's TODO list progress"""
import re
import requests
import sys
import csv

URL = 'https://jsonplaceholder.typicode.com'
"""API url"""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user = requests.get('{}/users/{}'.format(URL, id)).json()
            todo_list = requests.get('{}/todos'.format(URL)).json()
            user_name = user.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todo_list))
            done_todos = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(done_todos),
                    len(todos)
                )
            )
            for todo_done in done_todos:
                print('\t {}'.format(todo_done.get('title')))

"""Export data in the CSV format"""
filename = f"{id}.csv"
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for todo in todos:
        writer.writerow({
            'USER_ID': id,
            'USERNAME': user_name,
            'TASK_COMPLETED_STATUS': todo.get('completed'),
            'TASK_TITLE': todo.get('title')
        })
