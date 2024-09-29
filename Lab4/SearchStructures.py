"""
Name: Kevin Avina-Gutierrez
SearchStructures.py
Description: Implement a stack with the necessary functions to check if stack is empty,
update the top item in the stack and show an item from the stack.
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.__items = []

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        # Check if stack is empty
        if self.__items == []:
            # If stack is empty, return True
            return True
        pass

    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        # Add item to the top of the list
        self.__items.append(item)
        pass

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        # Assign value at index '-1'
        temp = self.__items[-1]
        # Decrease stack size by removing the previous value place
        self.__items = self.__items[:-1]
        return temp
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.__items = []

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        # Check if stack is empty, return true
        if self.__items == []:
            return True
        pass

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        # Add item to the back of the queue
        self.__items.append(item)
        pass

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        # Place holder for index value at '0'
        temp = self.__items[0]
        # Assign queue value at index '1'
        self.__items = self.__items[1:]
        return temp