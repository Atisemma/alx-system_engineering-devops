#!/usr/bin/python3
"""Script returning an employee's TODO list progress"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    # URL for employee information
    url_user = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    # URL for todos
    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetching user data
    response_user = requests.get(url_user)
    user_data = response_user.json()
    employee_name = user_data['name']

    # Fetching todos data
    response_todos = requests.get(url_todos)
    todos_data = response_todos.json()

    # Counting completed tasks
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    # Displaying the progress
    total_tasks = len(todos_data)
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"    {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
