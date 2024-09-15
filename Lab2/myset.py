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

        for i in self.__s:  # Go through the list values with i as the assigned index
            while i in self.__s and self.__s.count(i) > 1:
                self.__s.remove(i)
                self.__size -= 1

    
    # Return the size of setList
    def size(self):
        return self.__size
    
    # Return the values of setList
    def vals(self):
        return self.__s