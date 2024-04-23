#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

Takes an employee ID as a command-line argument and fetches
the corresponding user info and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(api_url + "users/{}".format(employee_id)).json()

    parameter = {"userId": employee_id}
    todos = requests.get(api_url + "todos", parameter).json()

    completed_tasks = [tasks.get("title") for tasks in todos
                       if tasks.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        response.get("name"), len(completed_tasks), len(todos)))

    [print("\t {}".format(complete)) for complete in completed_tasks]
