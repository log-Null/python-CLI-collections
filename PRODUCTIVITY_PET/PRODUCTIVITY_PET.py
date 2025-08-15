from colorama import Fore, Style
import random

tasks = []
print(Fore.BLUE + " PRODUCTIVITY PET 🐦‍🔥 " + Style.RESET_ALL)

while True:
    user = input("Did you complete your tasks today? ").lower().strip()
    
    if user in ["yes", "yeah", "yep"]:
        print("🥚")
        print(Fore.GREEN + " Share your tasks to hatch your customized pet" + Style.RESET_ALL)
        
        tasks = [input("Enter task: ") for _ in range(int(input("How many tasks in your list? ")))]
        completed = int(input("How many tasks did you complete? "))
        
        percentage = (completed / len(tasks)) * 100
        print(f"Progress: {percentage:.2f}%")
        
        petc = ["🐦", "🐧", "🦇", "🦤", "🦆", "🦅"]
        pets = random.choice(petc)
        
        if percentage < 50:
            print(Fore.YELLOW + "Oops! The pet didn’t hatch. Current stage: 🥚" + Style.RESET_ALL)
        elif 50 <= percentage < 80:
            print(Fore.YELLOW + "CURRENT PROGRESS : 🐣" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"Congratulations!\nCURRENT PROGRESS : {pets}" + Style.RESET_ALL)
    
    elif user in ["no", "nope", "nah"]:
        print("You need to complete your tasks to hatch your pet")
        cont = input("Do you want to continue? ").lower().strip()
        if cont in ["yes", "yeah", "yep"]:
            continue
        else:
            print("Thank you for using PRODUCTIVITY PET! Goodbye!")
            break

