#!/usr/bin/python3
"""a Python script that returns information about their TODO list progress."""
import re
import requests
import sys

URL = 'https://jsonplaceholder.typicode.com'
"""The API's URL."""

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
