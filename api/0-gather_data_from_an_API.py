#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress for a given employee ID
using a REST API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID from the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Prints:
        The employee name, number of completed tasks, total number of tasks,
        and the titles of the completed tasks.
    """
    url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    employee_response = requests.get(f"{url}/users/{employee_id}")
    if employee_response.status_code != 200:
        print("Employee not found.")
        return

    employee = employee_response.json()
    employee_name = employee.get('name')

    # Fetch TODO list data for the employee
    todo_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todo_response.json()

    # Filter tasks
    done_tasks = [todo for todo in todos if todo.get('completed')]
    total_tasks = len(todos)
    done_tasks_count = len(done_tasks)

    # Print the required output
    print(f"Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):")

    # Print completed task titles
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
