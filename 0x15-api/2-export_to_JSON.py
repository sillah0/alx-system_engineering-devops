#!/usr/bin/python3
"""a script that returns info about employee's TODO list progress"""
import re
import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    """Exporting data to json"""
    filename = f"{user_id}.json"
    data = {
        user_id: [
            {
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            for todo in todos
        ]
    }
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
