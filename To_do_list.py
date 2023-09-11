# To-Do List Application in Python

# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to display the list of tasks
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to remove a task by its index
def remove_task(index):
    if index >= 1 and index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
