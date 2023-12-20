#!/usr/bin/python3
"""
    this module contains a simple API gether
    and csv exporter
"""

from csv import QUOTE_ALL


if __name__ == "__main__":
    """main function"""
    import csv
    import requests
    from sys import argv

    id = int(argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    EMPLOYEE_NAME = requests.get(url).json()["name"]
    task_record = requests.get(url + "/todos").json()

    with open(f"{id}.csv", "w") as csvfile:
        write = csv.writer(csvfile, quoting=QUOTE_ALL)
        for task in task_record:
            write.writerow([
                id, EMPLOYEE_NAME, task["completed"], task["title"]
            ])