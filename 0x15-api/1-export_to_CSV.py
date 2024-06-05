#!/usr/bin/python3
"""a script that returns info about employee's TODO list progress"""
import re
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

"""Export data in the CSV format"""
filename = f"{user_id}.csv"
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for todo in todos:
        writer.writerow({
            'USER_ID': user_id,
            'USERNAME': username,
            'TASK_COMPLETED_STATUS': todo.get('completed'),
            'TASK_TITLE': todo.get('title')
        })
