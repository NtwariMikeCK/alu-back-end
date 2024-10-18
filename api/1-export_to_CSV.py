#!/usr/bin/python3
"""
This module fetches and exports the TODO list progress of an employee into a CSV file.
"""
import csv
import requests
import sys


def export_employee_todo_to_csv(employee_id):
    """
    Fetches the TODO list for a given employee ID from the REST API
    and exports the data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    The CSV file format:
        "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
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

    # Define the CSV file name based on the user ID
    file_name = f"{employee_id}.csv"

    # Write data to the CSV file
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write the records in the required format
        for task in todos:
            writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])

    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_employee_todo_to_csv(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
