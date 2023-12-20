#!/usr/bin/python3
"""
    this module contains a simple API data gether
"""

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
    import requests
    from sys import argv

    id = int(argv[1])
    NUMBER_OF_DONE_TASKS = 0
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    employee = (requests.get(url)).json()
    task_record = requests.get(url + "/todos").json()
    tasks_completed = [tasks for tasks in task_record if tasks["completed"]]

    print(f"Employee {employee['name']} is done" +
          f" with tasks({len(tasks_completed)}/{len(task_record)}):")
    for task in task_record:
        if task['completed']:
            print(f"\t {task['title']}")
