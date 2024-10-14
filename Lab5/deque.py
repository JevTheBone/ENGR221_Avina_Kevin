"""
Kevin Avina-Gutierrez
deque.py
Implement a Deque using our DoublyLinkedList class, each method can be
written with just a single line.
"""

from .doublyLinkedList import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()

    # Check whether or not the deque is empty
    def isEmpty(self):
        return self.__values.isEmpty()
    
    # Override __len__() method
    def __len__(self):
        return len(self.__values)
    
    # Override __str__() method
    def __str__(self):
        return str(self.__values)
    
    # Return the value of the first(leftmost) item in the deque.
    def peekLeft(self):
        return self.__values.first()

    # Return the value of the last(rightmost) item in the deque
    def peekRight(self):
        return self.__values.getLastNode().getValue()

    # Insert the given value to the front of the deque
    def insertLeft(self, value):
        self.__values.insertFront(value)

    # Insert the given value to the back of the deque    
    def insertRight(self, value):
        self.__values.insertBack(value)

    # Remove the first item from the deque
    def removeLeft(self):
        return self.__values.deleteFirstNode()

    # Remove the last item from the deque
    def removeRight(self):
        return self.__values.deleteLastNode()
    
if __name__ == "__main__":
    pass