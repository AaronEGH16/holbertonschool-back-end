#!/usr/bin/python3
"""
    this module contains a simple API gether
    and json exporter
"""


if __name__ == "__main__":
    """main function"""
    import json
    import requests

    url = f"https://jsonplaceholder.typicode.com"
    user_record = requests.get(url + "/users").json()
    task_record = requests.get(url + "/todos").json()

    json_obj = {
        f"{user['id']}": [{
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
                } for task in task_record if user['id'] == task['userId']]
        for user in user_record
    }

    with open(f"todo_all_employees.json", "w") as jsonfile:
        json.dump(json_obj, jsonfile)
