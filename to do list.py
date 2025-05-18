print('Welcome to your task manager')
tasks = []

while True:
    print('\n1. Add task')
    print('2. View all tasks')
    print('3. Delete task')
    print('4. Exit task manager')

    choice = input('Enter an option: ')

    if choice == '1':
        while True:
            new_task = input("Name a task you would like to add: ")
            tasks.append(new_task)
            print(f'Task "{new_task}" has been added to your list.')
            another = input('Would you like to add another task? (yes/no): ').strip().lower()
            if another != 'yes':
                break

    elif choice == '2':
        if not tasks:
            print('Your task list is empty.')
        else:
            print('Here is the list of your added tasks:')
            for i, task in enumerate(tasks, start=1):
                print(f'{i}. {task}')
            input("\nPress Enter to return to the main menu...")

    elif choice == '3':
        if not tasks:
            print('Your task list is empty.')
        else:
            print('Choose a task to delete: ')
            for i, task in enumerate(tasks, start=1):
                print(f'{i}. {task}')
            try:
                number=int(input('Enter a task number to delete: '))
                if 1 <= number <= len(tasks):
                    deleted = tasks.pop(number - 1)
                    print(f"Task '{deleted}' has been removed from your list")
                else:
                    print('That number doest exist')
            except ValueError:
                print('Please enter a valid number from the list')
                break
            input("\nPress Enter to return to the main menu...")

    elif choice == '4':
       print('You are exiting the task manager. Thank you for testing :) Goodbye!')
       restart = input("Press Enter to relaunch the Task Manager, or type anything else to quit: ").strip().lower()
       if restart != '':
           break


