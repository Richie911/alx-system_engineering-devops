#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url= "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    todos = requests.get(api_url + "todos", params={"userId": user_id}).json()

    tasks_json = {user_id: [{"task": task.get("title"),
                             "completed": task.get("completed"),
                             "username": username} for task in todos]}

    # Write the JSON data to a file named after the user ID
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(tasks_json, json_file)

    print("Tasks exported to {}.json successfully.".format(user_id))