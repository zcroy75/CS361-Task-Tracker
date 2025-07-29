def guide():
    # Print available commands to user
    print("COMMANDS:")
    print("Type 'add' to add a task to the list.")
    print("Type 'view' to see the full task list.")
    print("Type 'delete' to remove a task from the list.")
    print("Type 'quit' to exit the program.\n")

    # Prompt user for action
    return input("What would you like to do?\n")


def add(task_list):
    task = input("Please write your task below:\n")
    task_list.append(task)
    print("")
    return task_list


def view(task_list):
    if task_list == []:
        return print("The list of tasks is empty! Add tasks by using the 'add' command.\n")
    index = 1
    for task in task_list:
        print(index, ": ", task, sep='')
        index += 1
    print("")
    return


def delete(task_list):
    confirm_choice = input("Be aware that removing a task is final. Type 'confirm' if you would still like to continue, type anything else if you no longer want to delete a task: ")
    if confirm_choice != 'confirm':
        print("No tasks have been removed from the list.\n")
        return task_list
    view_choice = input("Would you like to see the list of your tasks first? Type 'yes' to confirm, type anything else to go straight to deleting a task: ")
    if view_choice == 'yes':
        print("Here are your tasks:")
        view(task_list)
    choice = int(input("Please provide the number of the task you would like to remove, or type 'cancel' if you have decided not to remove a task: "))
    if choice <= len(task_list):
        task_list.pop(choice - 1)
        print("Your task has been successfully removed from the list.\n")
    else:
        print("You entered an invalid number, please double check your task list and try again.\n")
    return task_list


def main():
    # Introduce program to user
    print("Welcome, user!")
    print("This program will keep track of your tasks as a list.")
    print("Newest features of this program include the ability to remove tasks from your list.")
    print("Please view the COMMANDS section below for more info on available features.\n")

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
