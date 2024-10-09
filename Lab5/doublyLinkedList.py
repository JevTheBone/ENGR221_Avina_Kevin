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
       return self.getFirstNode() == None

    # Set the first node of the list to a new node 
    def first(self):
        if self.isEmpty():
            raise Exception("Error: List is empty, no value to return.")
        return self.getFirstNode().getValue()
    
    # Return the first node in the list
    def getFirstNode(self) -> DoubleNode:
        return self.__firstNode

    # Return the last node in the list
    def getLastNode(self) -> DoubleNode:
        return self.__lastNode
    
    # Set the first node of the list to a new node
    def setFirstNode(self, node):
        # Raise an exception if the input is not a valid node
        if node != None and type(node) != DoubleNode:
            raise Exception("Error: Input must be valid DoubleNode or None")
        else: 
            self.__firstNode = node

    # Set the first node of the list to a new node   
    def setLastNode(self, node):
        # Raise an exception if the input is not a valid node
        if node != None and type(node) != DoubleNode:
            raise Exception("Error: Input must be valid DoubleNode or None")
        else: 
            self.__lastNode = node

    def find(self, value):
        # Traverse down the list, starting with the first node
        node = self.getFirstNode()
        while node != None:
            # If this node has the given value, return it
            if node.getValue() == value:
                return node 
            # Otherwise, grab the next node to check
            node = node.getNextNode()
        # If the value was not found, return None
        return None

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