"""
Author: Kevin Avina-Gutierrez
Filename: myarray.py
Description: Implementation of an unsorted array with duplicates
"""

class MyArray():
    # Constructor
    def __init__(self, initialSizeOrValues):
        if type(initialSizeOrValues) == int:
            self.__a = [None] * initialSizeOrValues # The array isn't stored with this type
            self.__length = initialSizeOrValues     # sets length to int input
        elif type(initialSizeOrValues) == list:
            self.__a = initialSizeOrValues           # The array is stored as a list
            self.__length = len(initialSizeOrValues) # The length based on number of list items

    ########
    # Methods
    ########
        
    # Return the current length of the array
    def length(self):
        return self.__length 
    
    # Return a list of the current array values
    def values(self):
        return self.__a

    # Return the value at index idx
    # Otherwise, do not return anything
    def get(self, idx):
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         return self.__a[idx]              # only return item if in bounds
 
    # Set the value at index idx
    def set(self, idx, value):         
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         self.__a[idx] = value               # only set item if in bounds
    
    # Insert value to the end of the array
    def insert(self, value):
        self.__length += 1  #increment length

        self.__a.append(value) #Ask someone to explain this part - why couldn't it add a new item after increasing length without
                               #using the append method?
        
    # Return the index of value in the array, 
    # or -1 if value is not in the array
    def search(self, value):

        # Only search the indices we've inserted
        for idx in range(self.__length): 

            # Check the value at the current index 
            if self.__a[idx] == value:  

                # Return the index  
                return idx  
            
        # Return -1 if value was not found             
        return -1                        

    # Delete the first occurrence of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        # Find the index of the value to delete
        idx = self.search(value)
        
        # If the value was found
        if idx != -1: 

            # Decrement the array length
            self.__length -= 1

            # Shift all the remaining values 
            for j in range(idx, self.__length):
                self.__a[j] = self.__a[j+1]
            
            self.__a = self.__a[:self.__length] # Sets array list size to the newly decreased size value

            if self.search(value) != -1:    # Checks array again for duplicate instances
                self.delete(value)

            # Return that value was deleted
            return True
        
        # Return False if the value was not found
        return False
    
    # Print all items in the list
    def traverse(self):
        for i in range(self.__length):
            print(self.__a[i])

if __name__ == '__main__':
    pass
