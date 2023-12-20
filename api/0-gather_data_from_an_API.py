#!/usr/bin/python3
"""
    this module contains a simple API data gether

    get from user and todo lists:
        - user name
        - number of tasks
        - tasks completed
        - task title
    and print text
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/"

    id = int(argv[1])
    employee = requests.get(url + f"users/{id}").json()
    tasks_record = requests.get(url + f"users/{id}/todos").json()

    tasks_completed = [tasks for tasks in tasks_record if tasks["completed"]]

    print(f"Employee {employee['name']} is done with ", end="")
    print(f"tasks({len(tasks_completed)}/{len(tasks_record)}):")
    for task in tasks_completed:
        print(f"\t {task['title']}")
