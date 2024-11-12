[5:56 pm, 12/11/2024] Sarvesh Gujrathi: import json
from datetime import datetime

# Path to the JSON file where tasks are saved
FILE_PATH = "tasks.json"

# Load tasks from the file if it exists
def load_tasks():
    try:
        with open(FILE_PATH, 'r') as file:
            tasks = json.load(file)
            
        return tasks
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    


    # Create a task dictionary
    task = {
        "title": title,
        "description": description,
        
        "status": "incomplete"
    }
    tasks.append(task)
    print("Task added successfully!")

# Update an existing task
def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to update: ")) - 1

    if 0 <= task_number < len(tasks):
        tasks[task_number]["status"] = input("Enter new status (incomplete, in-progress, complete): ")
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to delete: ")) - 1

    if 0 <= task_number < len(tasks):
        del tasks[task_number]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} - {task['description']}")
           
            print("-" * 30)

# Main function to run the To-Do list application
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
[6:32 pm, 12/11/2024] Sarvesh Gujrathi: def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is undefined."
        else:
            return num1 / num2
    else:
        return "Invalid operation selected."

# Main function to run the calculator
def main():
    print("Welcome to the Simple Calculator!")

    # Input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values…
[6:43 pm, 12/11/2024] Sarvesh Gujrathi: import random
import string

def generate_password(length):
    # Define character sets to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

# Run the password generator
if _name_ == "_main_":
    main()