"""
Kevin Avina-Gutierrez
doublyLinkedList.py
Implement a doubly linked list which keeps track of both the first and last nodes
in the list, allowing you to traverse from both ends of the list.
"""

from .doubleNode import DoubleNode 

class DoublyLinkedList():

    # Implements the first and last node in the linked list
    def __init__(self):
        self.__firstNode = None
        self.__lastNode = None 

    # Determine whether or not the list is empty
    def isEmpty(self) -> bool:
        if self.getFirstNode().__nextNode == None and self.getLastNode().__previousNode == None:
            return True

    
    def first(self):
        pass
    
    def getFirstNode(self) -> DoubleNode:
        return self.__firstNode

    def getLastNode(self) -> DoubleNode:
        return self.__lastNode
    
    def setFirstNode(self, node):
        pass

    def setLastNode(self, node):
        pass

    def find(self, value):
        pass

    def insertFront(self, value):
        pass

    def insertBack(self, value):
        pass

    def insertAfter(self, value_to_add, after_value) -> None:
        pass
    
    def deleteFirstNode(self):
        pass
    
    def deleteLastNode(self):
        pass
    
    def deleteValue(self, value):
        pass

    def forwardTraverse(self):
        pass

    def reverseTraverse(self):
        pass

    def __len__(self):
        pass
    
    def __str__(self):
        pass
    
if __name__ == "__main__":
    pass