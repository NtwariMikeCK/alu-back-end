#!/usr/bin/python3
"""
This module fetches and exports the TODO list progress
of an employee into a JSON file.
"""
import json
import requests
import sys


def export_employee_todo_to_json(employee_id):
    """
    Fetches the TODO list for a given employee ID from the REST API
    and exports the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    The JSON format:
        { "USER_ID": [{"task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...]}
    """
    url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    employee_response = requests.get(f"{url}/users/{employee_id}")
    if employee_response.status_code != 200:
        print("Employee not found.")
        return

    employee = employee_response.json()
    employee_name = employee.get('username')

    # Fetch TODO list data for the employee
    todo_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todo_response.json()
    # Prepare the data in the required format
    tasks = [{"task": task.get('title'),
              "completed": task.get('completed'),
              "username": employee_name} for task in todos]

    data = {str(employee_id): tasks}

    # Define the JSON file name based on the user ID
    file_name = f"{employee_id}.json"

    # Write data to the JSON file
    with open(file_name, mode='w') as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_employee_todo_to_json(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
