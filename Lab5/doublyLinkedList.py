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
       return (self.__firstNode == None and self.__lastNode == None)

    # Set the first node of the list to a new node 
    def first(self):
        if self.isEmpty():
            raise Exception("Error: List is empty, no value to return.")
        return self.__firstNode.getValue()
    
    # Return the first node in the list
    def getFirstNode(self):
        return self.__firstNode

    # Return the last node in the list
    def getLastNode(self):
        return self.__lastNode
    
    # Set the first node of the list to a new node
    def setFirstNode(self, node):
        # Raise an exception if the input is not a valid node
        if node != None and type(node) != DoubleNode:
            raise Exception("Error: Input must be valid DoubleNode or None")
        # Assign first node
        self.__firstNode = node

    # Set the last node of the list to a new node   
    def setLastNode(self, node):
        # Raise an exception if the input is not a valid node
        if node != None and type(node) != DoubleNode:
            raise Exception("Error: Input must be valid DoubleNode or None")
        # Assign last node
        self.__lastNode = node

    # Return a node in the list containing the given value
    def find(self, value) -> DoubleNode:
        # Traverse the list starting with the first node
        node = self.getFirstNode()
        while node != None:
            # If the node has the value, return it
            if node.getValue() == value:
                return node
            # Grab the next node to check
            node = node.getNextNode()
        # If the value was not found, return None
        return None
            
    # Insert the given value to the front of the list
    def insertFront(self, value):
        # Create a new node that points to the first node in the list
        node = DoubleNode(value, self.__firstNode, None)
        # If list is empty, insert node in the the end of the list
        if self.isEmpty():
            self.setLastNode(node)
        # If first node is not none, set first node to previous node
        if self.__firstNode != None:
            self.__firstNode.setPreviousNode(node)
        # Otherwise set node to first node
        self.setFirstNode(node)

    # Insert the given value to the back of the list
    def insertBack(self, value):
        # Create a new node that points to the last node in the list
        node = DoubleNode(value, None, self.__lastNode)
        # If list is not empty, insert node in the the start of the list
        if self.isEmpty():
            self.setFirstNode(node)
        # If last node is not none, set last node to previous node
        if self.__lastNode != None:
            self.__lastNode.setNextNode(node)
        # Otherwise set node to last node
        self.setLastNode(node)

    # Insert a value into the list after a specified value
    def insertAfter(self, value_to_add, after_value) -> None:
        if self.isEmpty():
            raise Exception("Error: cannot insertAfter in an empty list")
        # Value to add
        newNode = DoubleNode(value_to_add)
        node = self.getFirstNode()
        # Get the next value to check
        while node.getValue() != after_value:
            node = node.getNextNode()
        # When the node is the last one in the list
        if node.isLast():
            # Shift node and newNode order
            newNode.setPreviousNode(node)
            node.setNextNode(newNode)
            self.setLastNode(newNode)
        #Here we insert the value after a specified value
        newNode.setPreviousNode(node)
        newNode.setNextNode(node.getNextNode())
        node.getNextNode().setPreviousNode(newNode)
        node.setNextNode(newNode)
        
    # Remove the first node from the list
    def deleteFirstNode(self):
        # Raise an exception if list is empty
        if self.isEmpty():
            raise Exception("Error: cannot deleteFirstNode in an empty list")
        
        # Value of the node that was deleted
        removeVal = self.getFirstNode().getValue()

        # Check if its not the only item in the list
        if not(self.getFirstNode().isLast()):
            self.setFirstNode(self.getFirstNode().getNextNode())
            self.getFirstNode().setPreviousNode(None)

        else:
            self.setFirstNode(None)
        # The value of the node that was deleted
        return removeVal
        
    # Remove the last node from the list
    def deleteLastNode(self):
        # If the list is empty raise an exception
        if self.isEmpty():
            raise Exception("Error can't deleteLastNode in an empty list")
        
        # Node value to remove
        removeVal = self.getLastNode()

        if removeVal.isFirst():
            self.setLastNode(None)

        else:
            self.setLastNode(self.getLastNode().getPreviousNode())
            self.getLastNode().setNextNode(None)

        # Return deleted value
        return removeVal.getValue()
    
    # REmove a node with the specified value from the list
    def deleteValue(self, value):
        # Raise an exception if list is empty
        if self.isEmpty():
            raise Exception("Error: Cannot delete from empty list")
        
        removeVal = self.getFirstNode()

        # Traverse the list in search for the value to delete
        while removeVal.getValue() != value:
            removeVal = removeVal.getNextNode()
        
        removeVal.getPreviousNode().setNextNode(removeVal.getNextNode())
        removeVal.getNextNode().setPreviousNode(removeVal.getPreviousNode())

        # Return deleted value
        return removeVal.getValue()

    # Print each item in the list from the beginning to end
    def forwardTraverse(self):
        # Raise an exception if list is empty
        if self.isEmpty():
            raise Exception("Error: cannot print empty list")
        
        ourList = []
        node = self.getFirstNode()

        # Begin adding nodes into our list starting with the first node
        while not (node.isLast()):
            ourList.append(node.getValue())
            node = node.getNextNode()
        # Add the last node into our list
        ourList.append(self.getLastNode().getValue())

        for i in ourList:
            print(i)

    # Print each item in the list in reverse order
    def reverseTraverse(self):
        # Raise an exception if list is empty
        if self.isEmpty():
            raise Exception("Error: cannot print empty list")
        
        ourList = []
        node = self.getLastNode()

        # Begin adding nodes into our list starting from the last node
        while not (node.isFirst()):
            ourList.append(node.getValue())
            node = node.getPreviousNode()
        # Add the last node into our list
        ourList.append(self.getFirstNode().getValue())

        for i in ourList:
            print(i)

    # This will be run instead of the built in __len__() method
    # when checking the length of a DoublyLinkedList
    def __len__(self):
        index = 0
        # Traverse down the list starting with the first node
        node = self.getFirstNode() 
        # Stop when we reach the end of the list
        while node != None:
            # Increment the counter for each node we find
            index += 1
            # Update node to be the next node
            node = node.getNextNode()
        # Return the counter
        return index
    
    # This will run instead of the built in __str__() method
    # when printing a DoublyLinkedList
    def __str__(self):
        # Raise an exception if list is empty
        if self.isEmpty():
            raise Exception("Error: Cannot delete from empty list")
        
        convertedList = []
        node = self.getFirstNode()

        while node.getNextNode() != None:
            convertedList.append(node.getValue())
            node = node.getNextNode()

        return "["+ "".join(str(i) + " <-> " for i in convertedList)+ str(self.getLastNode().getValue()) + "]"
    
if __name__ == "__main__":
    pass