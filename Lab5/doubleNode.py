"""
Kevin Avina-Gutierrez
doubleNode.py
Implement bi-directional nodes "Double Nodes"
These nodes should have a pointer to the previous node in the list.
"""

class DoubleNode():

    def __init__(self, value, next=None, previous=None):
        self.__value = value
        self.__nextNode = next
        self.__previousNode = previous 

    #####
    # Methods
    #####
        # Checks whether or not the given node is first in the list
    def isFirst(self) -> bool:
        return self.__previousNode == None
        
        # Check whether or not the given node is last in the list
    def isLast(self) -> bool:
        return self.__nextNode == None
        
    #####
    # Getters
    #####
        # Return the value of the current double node
    def getValue(self):
        return self.__value
    
        # Return the value of the next Node in the list
    def getNextNode(self):
        return self.__nextNode
    
        # Return the previous node in the list
    def getPreviousNode(self):
        return self.__previousNode

    #####
    # Setters
    #####
        # Set the value of the node to a new value
    def setValue(self, new_value) -> None:
        self.__value = new_value

        # Set the value of the new next node
    def setNextNode(self, new_next) -> None:
        self.__nextNode = new_next

        # Set the value of the new previous node
    def setPreviousNode(self, new_previous) -> None:
        self.__previousNode = new_previous

    #####
    # Helpers
    #####

    def __checkValidNode(self, node) -> bool:
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
    
    def __str__(self):
        # Overloads the built in __str__() method so this will be run when printing a node.
        return str(self.getValue())

if __name__ == "__main__":
    pass