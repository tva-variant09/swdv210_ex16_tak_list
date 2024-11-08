#!/usr/bin/env python3
# author: marco ramos
# date: 10-22-2024
# description: task list program

import write_and_read_modules as wrm
from objects import Task, Category

# displays the menu
def display_menu():
    print()
    print(f"COMMAND MENU")
    print(f"list".ljust(10) + f" - List all tasks")
    print(f"add".ljust(10) + f" - Add a task")
    print(f"complete".ljust(10) + f" - Complete a task")
    print(f"delete".ljust(10) + f" - Delete a task")
    print(f"switch".ljust(10) + f" - Switch tasks")
    print(f"exit".ljust(10) + f" - Exit program")
    print()
  
# displays the categories
def display_categories():
   # print("Im in cat")
    categories = wrm.get_categories()
    print(f"CATEGORIES LIST")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    print()

# turns prompt in int, validates int, checks for max range in list
def get_int(prompt, maxNum):
        while True:
            try:
                number = int(input(prompt))
            except ValueError:
                print("Invalid whole number. Please try again.\n")
                continue

            if number < 1 or number > maxNum:
                print("That number isn't in the list. Please try again.\n")
            else:
                return number

# selects a category and returns the category and tasks
def select_category():
    categories = wrm.get_categories()
    number = get_int("Enter number to select category: ", len(categories))
    category = categories[number - 1]
    tasks = wrm.read_task_from_file(category)
    return category, tasks

# lists the tasks
def list_tasks(tasks, category):
    tasks = wrm.read_task_from_file(category)
    if tasks.count == 0:
        print("There are no tasks in this category.\n")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# adds a task
def add_task(tasks, category):
    tasks = wrm.read_task_from_file(category)
    while True:
        description = input("Description: ").strip()
        if description:
            break
        else:
            print("Description cannot be empty. Please try again.")
    task = Task(description)    
    tasks.addTask(task)
    wrm.write_task_on_file(category, tasks)  # Save changes
    print(f"task ({task}) added")
    
# deletes a task
def delete_task(category, tasks):
    tasks = wrm.read_task_from_file(category) # reads task list from a csv file and returns a TaskList object
    number = get_int("Number: ", tasks.count)
    task = tasks.getTask(number)
    tasks.removeTask(task) 
    wrm.write_task_on_file(category, tasks)  # Save changes 
    print(f"Task ({number}) deleted.\n")  

# completes a task
def complete_task(category, tasks):
    tasks = wrm.read_task_from_file(category)
    number = get_int("Number: ", tasks.count)
    task = tasks.getTask(number)
    task.completed = True
    wrm.write_task_on_file(category, tasks)  # Save changes with updated task completion
    print("Task marked as completed.\n") 
 

def main():
    
    display_menu()
    display_categories()
    category, tasks = select_category()
    
    while True:
        
        command = input("Command: ")
        if command == "list":
            list_tasks(tasks, category)
        elif command == "add":
            tasks = add_task(tasks, category)
        elif command == "complete":
            complete_task(category, tasks)
        elif command == "delete":
            delete_task(category, tasks)
        elif command == "switch":
            display_categories()
            category, tasks = select_category()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")
    
if __name__ == "__main__":
    main()