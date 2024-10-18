#!/usr/bin/python3
import json
import requests

# URL for users and tasks
users_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

# Fetch data from the API
users = requests.get(users_url).json()
todos = requests.get(todos_url).json()

# Dictionary to store all tasks for all users
all_tasks = {}

# Loop through users to map tasks to user IDs
for user in users:
    user_id = user['id']
    username = user['username'] 
    # Filter tasks for the current user
    user_tasks = []
    for task in todos:
        if task['userId'] == user_id:
            task_info = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            user_tasks.append(task_info)
    
    # Assign the list of tasks to the user's ID in the dictionary
    all_tasks[user_id] = user_tasks
# Export the data to a JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(all_tasks, json_file, indent=4)

# The print statement has been removed as per the requirements
