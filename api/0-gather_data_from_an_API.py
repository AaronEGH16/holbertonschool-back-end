#!/usr/bin/python3
"""
    this module contains a simple API gether
"""

if __name__ == "__main__":
    """
        main function
    """
    import requests
    from sys import argv

    id = argv[1]
    user_id = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo = f"https://jsonplaceholder.typicode.com/todos/"
    tasks = 0
    completed = 0
    completed_list = []
    user = requests.get(user_id).json()
    name = user.get("name")
    task_record = requests.get(todo).json()
    for task in task_record:
        if task.get("userId") == int(id):
            if task["completed"]:
                completed_list.append(task["title"])
                completed += 1
            tasks += 1

    print(f"Employee {name} is done with tasks({completed}/{tasks}):")
    for title in completed_list:
        print(f"\t {title}")
