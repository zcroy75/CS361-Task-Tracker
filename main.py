def guide():
    # Print available commands to user
    print("COMMANDS:")
    print("Type 'add' to add a task to the list.")
    print("Type 'view' to see the full task list.")
    print("Type 'delete' to remove a task from the list.")
    print("Type 'quit' to exit the program.\n")

    # Prompt user for action
    print("What would you like to do?")
    return input("Input: ")


def add(task_list):
    return task_list


def view(task_list):
    if task_list == []:
        return print("The list of tasks is empty! Add tasks by using the 'add' command.\n")
    return


def delete(task_list):
    return task_list


def main():
    # Introduce program to user
    print("Welcome, user!")
    print("This program will keep track of your tasks, including their due dates.\n")

    task_list = []
    while True:
        choice = guide()
        print("")
        match choice:
            case 'add':
                task_list = add(task_list)
            case 'view':
                view(task_list)
            case 'delete':
                task_list = delete(task_list)
            case 'quit':
                print("Thank you for using the task tracker program!\n")
                break
            case _:
                print("You have entered an invalid command, please double check that your input is an accepted command.\n")
    return


if __name__ == '__main__':
    main()
