# 🐦‍🔥 Productivity Pet

**Productivity Pet** is an interactive Python program designed to motivate you to complete your daily tasks by “hatching” a virtual pet based on your productivity. Gamify your day and track your progress with fun visual feedback!

---

## Features
- Track your daily tasks and completion status  
- Visualize your progress with fun emoji pets  
- Color-coded terminal feedback using **Colorama**  
- Simple, interactive, and beginner-friendly Python project  

---

## Installation
1. Ensure Python 3.7+ is installed  
2. Install dependencies:

    pip install colorama

3. Download or clone this repository  

---

## Usage
Run the program:

    python productivity_pet.py

Follow the prompts:  
1. Confirm if you completed your tasks today  
2. Enter your task list and the number of tasks completed  
3. Watch your pet hatch based on your productivity  

**Pet Stages:**
- 🥚 Egg → less than 50% tasks completed  
- 🐣 Hatchling → 50–79% tasks completed  
- 🐦 Fully hatched pet → 80%+ tasks completed (randomly selected from 🐦, 🐧, 🦇, 🦤, 🦆, 🦅)

---

## How It Works
- Calculates progress percentage:

    Progress (%) = (Completed Tasks / Total Tasks) * 100

- Displays a pet emoji corresponding to your completion percentage  
- Encourages continued productivity if tasks are incomplete  

---

## Example
    PRODUCTIVITY PET 🐦‍🔥
    Current Progress of Pet:🥚
    Complete your tasks to hatch your  pet.
    Did you complete your tasks today? 
    yes
    How many tasks in your list? 3
    Enter task: Finish assignment
    Enter task: Read book
    Enter task: Workout
    How many tasks did you complete? 2
    Progress: 66.67%
    CURRENT PROGRESS : 🐣

---

## Why This Project is good?
- Demonstrates Python skills including loops, input handling, and lists  
- Shows knowledge of third-party packages (**Colorama**) and terminal output formatting  
- Highlights creativity and initiative in building a productivity tool  
- Easy to extend into a larger portfolio project (e.g., saving progress, GUI version)  

---

## ALSO:
detailed explanation:https://steps-to-tech-world.hashnode.dev/weekend-2-project-3-productivity-pet-with-python
