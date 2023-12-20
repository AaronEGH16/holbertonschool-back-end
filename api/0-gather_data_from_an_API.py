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
    from sys import argv
    import requests

    id = argv[1]
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    EMPLOYEE_NAME = (requests.get(url)).json()["name"]
    task_record = requests.get(url + "/todos").json()
    for tasks in task_record:
        TOTAL_NUMBER_OF_TASKS += 1
        if tasks["completed"]:
            NUMBER_OF_DONE_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done" +
          f" with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in task_record:
        if task['completed']:
            print(f"\t {task['title']}")
