#!/usr/bin/python3
"""
    this module contains a simple API gether
    and json exporter
"""


if __name__ == "__main__":
    """main function"""
    import json
    import requests
    from sys import argv

    id = int(argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_name = requests.get(url).json()["username"]
    task_record = requests.get(url + "/todos").json()

    with open(f"{id}.json", "w") as jsonfile:
        json_obj = {
            f"{id}": [{
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name
                } for task in task_record]
        }
        json.dump(json_obj, jsonfile)
