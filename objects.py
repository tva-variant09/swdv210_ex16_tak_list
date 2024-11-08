#!/usr/bin/env python3
# author: Marco Ramos
# date: 10-24-2024
# description: objects for task list program

from dataclasses import dataclass

@dataclass
class Task:
    # task object attributes
    description:str = ""
    completed:bool = False

    # object methods
    def __str__(self):
        completed_str = ""
        if self.completed == True:
            completed_str = " (DONE!)"            
        return self.description + completed_str

@dataclass
class Category:
    # category object attributes
    name:str = ""

    # object methods
    def __post_init__(self): 
        self.__tasks = []
        
    def addTask(self, task):
        self.__tasks.append(task)
        
    def getTask(self, number):
        index = number - 1
        return self.__tasks[index]
    
    def removeTask(self, task):
        self.__tasks.remove(task)
        
    @property
    def count(self):
        return len(self.__tasks)
    
    def __iter__(self):
        for task in self.__tasks:
            yield task
            
    def __str__(self):
        tasks_str = ""
        for task in self.__tasks:
            tasks_str += str(task) + " | "
        tasks_str = tasks_str[:-3]
        return tasks_str
        