import requests

# Microservice URLs
CRUD_SERVICE = "http://localhost:5000"
TAGS_SERVICE = "http://localhost:5001"
GROUP_SERVICE = "http://localhost:5002"
SORT_SERVICE = "http://localhost:6000"


def print_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\n=== Your Tasks ===")
    for idx, task in enumerate(tasks, 1):
        task_name = task.get("task_name", "Unnamed Task")
        due_date = task.get("due_date", "No due date")
        tags = (
            ", ".join(task.get("tags", []))
            if task.get("tags")
            else "No tags"
        )
        group = task.get("group", "No group")
        print(f"{idx}. {task_name}")
        print(f"   Due: {due_date}")
        print(f"   Tags: {tags}")
        print(f"   Group: {group}")
        print("-" * 25)
    print()


def create_task():
    name = input("Enter task name: ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    payload = {"task_name": name, "due_date": due_date}
    requests.post(f"{CRUD_SERVICE}/tasks", json=payload)
    print("New task created.")


def list_tasks():
    r = requests.get(f"{CRUD_SERVICE}/tasks")
    if r.status_code == 200:
        print_tasks(r.json())
    else:
        print("Error retrieving tasks.")


def update_task():
    task_id = input("Enter task ID to update: ")
    name = input("Enter new task name: ")
    due_date = input("Enter new due date (YYYY-MM-DD): ")
    payload = {"task_name": name, "due_date": due_date}
    requests.put(f"{CRUD_SERVICE}/tasks/{task_id}", json=payload)
    print("Task updated.")


def delete_task():
    check_list_choice = input(
        "Would you like to see your task list before deleting a task? "
        "('y' to confirm): "
    )
    if check_list_choice == 'y':
        list_tasks()
    task_id = input("Enter task ID to delete: ")
    requests.delete(f"{CRUD_SERVICE}/tasks/{task_id}")
    print("Task deleted.")


def create_tag():
    name = input("Enter tag name: ")
    payload = {"name": name}
    requests.post(f"{TAGS_SERVICE}/tags", json=payload)
    print("New tag created.")


def list_tags():
    r = requests.get(f"{TAGS_SERVICE}/tags")
    tags = r.json()

    if not tags:
        print("\nNo tags found.\n")
        return False

    if r.status_code == 200:
        print("\n=== Your Tags ===")
        for tag in tags:
            print(f"ID: {tag.get('id')} | Name: {tag.get('name')}")
        print("-" * 25 + "\n")
    else:
        print("Error retrieving tags.")


def add_tag():
    if list_tags() is False:
        return
    task_id = input("Enter task ID to tag: ")
    tag_id = input("Enter tag ID: ")
    requests.post(f"{CRUD_SERVICE}/tasks/{task_id}/tags/{tag_id}")
    print("Tag added to task.")


def create_group():
    name = input("Enter group name: ")
    payload = {"group_name": name}
    requests.post(f"{GROUP_SERVICE}/groups", json=payload)
    print("New group created.")


def list_groups():
    r = requests.get(f"{GROUP_SERVICE}/groups")
    groups = r.json()

    if not groups:
        print("\nNo groups found.\n")
        return False

    if r.status_code == 200:
        print("\n=== Your Groups ===")
        for group in groups:
            print(f"ID: {group.get('id')} | Name: {group.get('name')}")
        print("-" * 25 + "\n")
    else:
        print("Error retrieving groups.")


def assign_to_group():
    if list_groups() is False:
        return
    group_id = input("Enter group ID: ")
    task_id = input("Enter task ID to assign: ")
    payload = {"task_id": task_id}
    requests.post(f"{GROUP_SERVICE}/groups/{group_id}/tasks", json=payload)
    print("Task assigned to group.")


def sort_tasks():
    r = requests.get(f"{CRUD_SERVICE}/tasks")
    tasks = r.json()
    r_sort = requests.post(f"{SORT_SERVICE}/organize", json={"tasks": tasks})
    sorted_tasks = r_sort.json().get("tasks", [])
    print("\nTasks sorted by due date:")
    print_tasks(sorted_tasks)


def menu():
    # Print available commands to user
    print("""
=== To-Do App Menu ===
1. Create Task
2. List Tasks
3. Update Task
4. Delete Task
5. Create New Tag
6. Add Tag to Task
7. Create New Group
8. Assign Task to Group
9. View tasks by Due Date
0. Exit
""")

    # Prompt user for action
    return input("Choose an option: ")


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
            # Update task
            case '3':
                update_task()
            # Delete task
            case '4':
                delete_task()
            # Create new tag
            case '5':
                create_tag()
            # Add tag to task
            case '6':
                add_tag()
            # Create new group
            case '7':
                create_group()
            # Assign task to group
            case '8':
                assign_to_group()
            # Sort tasks by due date
            case '9':
                sort_tasks()
            # Exit program
            case '0':
                quit_choice = input(
                    "Are you sure you want to exit the program? "
                    "Type 'yes' to confirm, type anything else to stay: "
                )
                if quit_choice == 'yes':
                    print("Thank you for using the task tracker program!\n")
                    break
                else:
                    print("")
            case _:
                print(
                    "You have entered an invalid command, "
                    "please double check that your input is an "
                    "accepted command.\n"
                )
    return


if __name__ == '__main__':
    main()
