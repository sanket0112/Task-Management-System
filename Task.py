# Hy my name is Sanket and this prorgram for begginer level programer 

def task():
    your_task = []

    print("-----This is Task Management App-----")

    total_task = int(input("Enter your total number of tasks: "))
    for i in range(1, total_task + 1):
        task_name = input(f'Enter your Task {i}: ')
        your_task.append(task_name)

    print(f"\nToday's Tasks:\n{your_task}")

    while True:
        operation = int(input("\nChoose an option:\n1. Add\n2. Update\n3. Delete\n4. View\n5. Exit\nEnter your choice: "))

        if operation == 1:
            print("You selected: Add a task")
            add = input("Enter your new task: ")
            your_task.append(add)
            print(f'Task "{add}" has been added.')

        elif operation == 2:
            print("You selected: Update a task")
            old_task = input("Enter the task you want to update: ")
            if old_task in your_task:
                new_task = input("Enter your updated task: ")
                ind = your_task.index(old_task)
                your_task[ind] = new_task
                print(f'Task updated to: {new_task}')
            else:
                print("Task not found!")

        elif operation == 3:
            print("You selected: Delete a task")
            your_del_task = input("Enter the name of the task to delete: ")
            if your_del_task in your_task:
                your_task.remove(your_del_task)
                print(f'Task "{your_del_task}" has been deleted.')
            else:
                print("Task not found!")

        elif operation == 4:
            print("Here are your current tasks:")
            for i, task in enumerate(your_task, 1):
                print(f"{i}. {task}")

        elif operation == 5:
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid input. Please choose a number between 1 and 5.")


task()