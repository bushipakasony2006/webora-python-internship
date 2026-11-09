tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("Your To-Do List is empty.")
    else:
        print("\n===== YOUR TASKS =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print("Task removed:", removed)
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice! Please select 1 to 4.")
