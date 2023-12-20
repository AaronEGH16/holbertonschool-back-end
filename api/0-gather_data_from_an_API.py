#!/usr/bin/python3
"""
    this module contains a simple API data gether
"""

import requests
from sys import argv

if __name__ == "__main__":
    """
        (execute function only if __name__ is == "__main__")

        get from user id:
            - user name
            - number of tasks
            - tasks completed
            - task title
        and print text
    """

    id = int(argv[1])
    url = f"https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + f"users/{id}").json()
    task_record = requests.get(url + f"users/{id}/todos").json()
    tasks_completed = [tasks for tasks in task_record if tasks["completed"]]

    print(f"Employee {employee['name']} is done with ", end="")
    print(f"tasks({len(tasks_completed)}/{len(task_record)}):")
    for task in tasks_completed:
        print(f"\t {task['title']}")
