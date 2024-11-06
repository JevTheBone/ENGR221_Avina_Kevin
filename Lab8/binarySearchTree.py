"""
File Name: binarySearchTree.py

Description: This assignment will consist of the implementation of an unbalanced binary search tree.
This tree should encompass different range of methods that allow us to insert, search, traverse, delete.

Author: Kevin Avina-Gutierrez
"""

class BinarySearchTree:
    """ Implements multiple methods as well as recursive methods that 
        assist in the following tasks: insert, search, traverse, delete. 
        Our objective is to add more methods to further develop the
        tools of BST class.
    """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ isEmpty method checks whether the BST is empty - hence the name.
            Arguments: None
            Returns Boolean output T/F.
        """
        # Checks that tree is empty
        return self.__root is None
        
    
    def getRoot(self):
        """ getRoot method gets the root node of the BST
            Arguments: None
            Returns: The root Node
        """
        # Return the value assigned to our root Node
        return self.__root

    def search(self, goalKey):
        """ Search method returns a given key in the BST """
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        """ __searchHelp is a recursive method to help with search()
            Arguments: 
                node - root node of subtree to search
                goalKey - key to search for
            Returns: The node with the key(goalKey)
        """
        # This is incase our key is not found within the node
        if node is None:
            return None
        
        # Compare goalKey with the current node's key
        if goalKey == node.key:
            return node  # Found the node with the matching key
        elif goalKey < node.key:
            # Search in the left subtree
            return self.__searchHelp(node.left, goalKey)
        else:
            # Search in the right subtree
            return self.__searchHelp(node.right, goalKey)

    def lookup(self, goal):
        """ Get the value of the given key
            Arguments: goal - The key whose value to return
            Returns: the value of the goal key  
        """
        # Call search to find the node with the specified key
        node = self.search(goal)

        # Check if the node was found, key does not exist in the tree return None
        if node is None:
            return None 
        # Return the value associated with the found node
        else:
            return node.value 

    def findSuccessor(self, subtreeRoot):
        """ Finds the smallest node in the tree """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ A recursive mehtod to help with the findSuccessor() method,
            which find the samllest node in the tree
            Arguments: node - the root node of the subtree to find the successor
            Returns: The successor     
        """
        # Node to the left will be the smallest if node.left is none
        if node.left is None:
            return node
        # Since it isn't the smallest we must continue moving down
        # the left subtree
        else: 
            return self.__findSuccessorHelp(node.left)
    
    def delete(self, deleteKey):
        """ Deletes the node with the given key from the BST """
        if self.search(deleteKey):
            return self.__deleteHelp(self.__root, deleteKey)
        raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ A recurvise method to help with the delete() method, which
            deletes the node with the given key from the BST
            Arguments:
                node - root node of the subtree to delete from
                deleteKey - key we will be deleting
            Returns: the udpated node with the specified node deleted 
        """
        # If node is None, return None indicating key was not found in BST
        if node is None:
            return None
        
        # Compare DeleteKey with node.key
        if deleteKey < node.key:
            # Assign results to node.left and call __deleteHelp() method
            # Recursively search in the left subtree
            node.left = self.__deleteHelp(node.left, deleteKey)
            return node
        # Compare DeleteKey with node.key
        elif deleteKey > node.key:
            # Assign results to node.right and call __deleteHelp() method
            # Recursively search in the right subtree
            node.right = self.__deleteHelp(node.right, deleteKey)
            return node
        # If key to delete and node.key are the same
        else:
            # Compare different cases that need to be address before deleting
            # Node has no children
            if node.right is None and node.left is None:
                # This removes the node by returning None
                return None
            # Node has one child
            elif node.left is None:
                # Replace node with its right child
                return node.right
            elif node.right is None:
                # Replace node with its left child
                return node.left
            # Node has two children
            else:
                # Find the in-order successfor, this case it requires the smallest node in the right
                successor = self.findSuccessor(node.right)
                # Replace the current node's key-value entry with the smallest node (successor)
                node.key = successor.key
                node.value = successor.value
                # Delete successor node in the right subtree
                node.right = self.__deleteHelp(node.right, successor.key)
                # Return the updated Node 
                return node


    def traverse(self) -> None:
        """ Visits each node in the tree in ascending order """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ A recursive method to help with the traverse() method,
            which visits each node in the tree in ascending order
            Arguments: node - the root node of the subtree to traverse
            Returns: None, but should print each node in the order visited. 
        """
        # When node isn't None we continue with the recursive call
        if node is not None:
            # Traverse the left subtree
            self.__traverseHelp(node.left)
            # Print the current node's key and value
            print(f"({node.key}, {node.value})")
            # Traverse the right subtree
            self.__traverseHelp(node.right)

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    pass