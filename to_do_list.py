
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def remove_task():
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        view_tasks()
        task_number=int(input("Enter the task number to remove: "))
        if task_number>=1 and task_number<=len(tasks):
            removed_task=tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number!")


while True:
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select an option from the menu.")
 