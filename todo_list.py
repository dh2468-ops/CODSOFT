# CODSOFT Task 2: To-Do List Application

def main():
    tasks = []
    
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("List is empty.")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                
        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added successfully!")
            
        elif choice == '3':
            if tasks:
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Nothing to remove.")
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()