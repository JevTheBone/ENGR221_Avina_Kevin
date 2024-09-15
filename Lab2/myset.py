"""
Author: Kevin Avina-Gutierrez
Filename: myset.py
Description: Sets are another type of data structure with the following properties
    a) All items in the set are unique (i.e., no duplicates)
    b) Sets are unordered (similar to arrays)
    c) Sets are unindexed (unlike arrays)

"""
class MySet():
    # Contructor
    def __init__(self, setList):    
        
        self.__s = setList      #Assigns set values
        self.__size = len(setList) #Set size is the number of values

        # Checks is "i" is in setList    
        for i in self.__s:
            # "i" found and has a recorded entry in the setList
            while i in self.__s and self.__s.count(i) > 1:
                # Delete "i" in setList for index "i"
                self.__s.remove(i)
                self.__size -= 1  
    
    # Return the size of setList
    def size(self):
        return self.__size
    
    # Return the values of setList
    def vals(self):
        return self.__s
    
    # Return index value in setList
    # False if value is not found
    def search(self, value):
        # Look only in set items we've added
        for index in range(self.__size):
            # Return value if value is found
            if self.__s[index] == value:
                #Return value at index point in setList
                return value
        #Return only if item is not found in setList
        return False
    
    # Add a new value into setList
    def insert(self, value):
        if value not in self.__s: #If value isn't in the setList
            # Increase set size by one
            self.__size += 1
            # Append value into the list
            self.__s.append(value)
    
    # Delete an existing value in setList
    def delete(self, value):
        # Call upon the search method and assign it to index
        index = self.search(value)
        # If index "value" exists in search method, delete item
        if index != False:
            # Decrease setList length
            self.__size -= 1
            self.__s.remove(value)
            # Return that value was deleted
            return True
        #Return False if value was not found
        return False
    
    #Print all itesm in the Set
    def traverse(self):
        for i in range(self.__size):
            print(self.__s[i])
    



