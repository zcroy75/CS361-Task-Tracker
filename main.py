import requests
import json


# Microservice URLs
CRUD_SERVICE = "http://localhost:5000"


def print_nice(data):
    print(json.dumps(data, indent = 2))


def create_task():
    name = input("Enter task name: ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    task = {"task_name": name, "due_date": due_date}
    try:
        r = requests.post(f"{CRUD_SERVICE}/tasks", json = task)
        print("Task created:", r.json())
    except:
        print("Error creating task.")


def list_tasks():
    try:
        r = requests.get(f"{CRUD_SERVICE}/tasks")
        tasks = r.json()
        print("\n--- Tasks ---")
        print_nice(tasks)
    except:
        print("Error listing tasks.")


def delete_task():
    check_list_choice = input("Would you like to see your task list before deleting a task? ('y' to confirm): ")
    if check_list_choice == 'y':
        list_tasks()
    task_id = input("Enter task ID to delete: ")
    try:
        r = requests.delete(f"{CRUD_SERVICE}/tasks/{task_id}")
        print("Response:", r.json())
    except:
        print("Error deleting task.")


def menu():
    # Print available commands to user
    print("\n=== To-Do App Menu ===")
    print("1. Create Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("0. Exit")

    # Prompt user for action
    return input("\nChoose an option: ")


def main():
    # Introduce program to user
    print("Welcome, user!")
    print("This program will keep track of your tasks as a list.")
    print("Functions include creating, viewing, and deleting tasks.")
    print("Please choose a feature from the section below.")

    while True:
        choice = menu()
        print("")
        match choice:
            # Create task
            case '1':
                create_task()
            # View tasks
            case '2':
                list_tasks()
            # Delete task
            case '3':
                delete_task()
            # Exit program
            case '0':
                quit_choice = input("Are you sure you want to exit the program? Type 'yes' to confirm, type anything else to stay: ")
                if quit_choice == 'yes':
                    print("Thank you for using the task tracker program!\n")
                    break
                else:
                    print("")
            case _:
                print("You have entered an invalid command, please double check that your input is an accepted command.\n")
    return


if __name__ == '__main__':
    main()
