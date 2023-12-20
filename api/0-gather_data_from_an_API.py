#!/usr/bin/python3
"""
    this module contains a simple API gether
"""

if __name__ == "__main__":
    """main function"""
    import requests
    from sys import argv

    id = int(argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    EMPLOYEE_NAME = requests.get(url).json()["name"]
    task_record = requests.get(url + "/todos").json()
    task_completed = [task for task in task_record if task["completed"]]

    print(f"Employee {EMPLOYEE_NAME} is done", end="")
    print(f" with tasks({len(task_completed)}/{len(task_record)}):")
    for task in task_completed:
        print(f"\t {task['title']}")
