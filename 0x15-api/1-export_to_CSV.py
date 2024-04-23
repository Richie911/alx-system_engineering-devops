#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    # Define the base URL for the JSON API
    response = requests.get(api_url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = response.get("username")

    todos = requests.get(api_url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, tasks.get("completed"), tasks.get("title")]
         ) for tasks in todos]
