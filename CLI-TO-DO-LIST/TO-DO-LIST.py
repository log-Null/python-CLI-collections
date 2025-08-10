from colorama import Fore, Style
print(Fore.GREEN + "hello what do you want to do ?🪸🪸" + Style.RESET_ALL)
tasks = []
while True:
    print(Fore.BLUE+ "\n1. Add a task🖥️\n2. View tasks👀\n3. Remove a task🗑️\n4. Exit🏃‍♂️💨" + Style.RESET_ALL)
    user = int(input("Enter your choice: "))
    if user == 1:
        task = input("Enter the task you want to add: ")
        tasks.append(task)
    elif user == 2:
        for index, task in enumerate(tasks):
            print(f"TASK {index}: {task}")
    elif user == 3:
        task_number = int(input("Enter the task number you want to remove: "))
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
        else:
            print(Fore.RED + "Invalid task number." + Style.RESET_ALL)
    elif user == 4:
        print(Fore.YELLOW + "exiting..." + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)
