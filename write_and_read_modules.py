#!/usr/bin/env python3
# author: Marco Ramos
# date: 10-24-2024
# description: database functions

import sys
import csv
from objects import Task, Category



# terminates the program
def exit_program():
    print("Terminating program.")
    sys.exit()

# retrieves categories from the txt file
def get_categories():
    categories = []
    try:
        with open("task_lists.txt") as file:
            for line in file:
                line = line.strip()  # Remove newline and surrounding whitespace
                if line:  # Ensure the category name is not empty
                    categories.append(line)
    except FileNotFoundError:
        print("Category file not found.")
        exit_program()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit_program()
    return categories

# writes task list to a csv file
def write_task_on_file(category, tasks):
    # convert the TaskList object to a list of lists
    rows = []
    for task in tasks:
        row = []
        row.append(task.description)
        row.append(task.completed)
        rows.append(row)

    # write list of lists to CSV file
    filename = "task_list_" + category.lower() + ".csv"    
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except PermissionError:
        print(f"Permission denied: '{filename}'. Please check the file permissions.")
        exit_program()
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")
        exit_program()
    
# reads task list from a csv file and returns a TaskList object
def read_task_from_file(category):
    filename = "task_list_" + category.lower() + ".csv"
    tasks = Category(category)
    try:
        with open(filename, "r", newline="") as file:  # Open the file in read mode
            reader = csv.reader(file)  # Create a CSV reader object
            for row in reader:  # Iterate over each row in the CSV file
                if len(row) != 2:  # Ensure each row has exactly 2 columns
                    print(f"Invalid row format: {row}")
                    continue
                description, completed_str = row
                if not description:  # Ensure task description is not empty
                    print("Task description cannot be empty.")
                    continue
                completed = completed_str == 'True'
                task = Task(description, completed)
                tasks.addTask(task)
    except FileNotFoundError:
        print(f"No task list found for category: {category}")
        exit_program()
    except PermissionError:
        print(f"Permission denied: '{filename}'. Please check the file permissions.")
        exit_program()
    except Exception as e:
        print(f"An error occurred while reading from file: {e}")
        exit_program()
    return tasks
        