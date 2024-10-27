from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='entries.txt'):
        # Open the file as read only
        with open(inputFile, 'r') as f:
            # Add each value in the file as an Entry to the Box
            for line in f:
                # Set the first word in the line as the nickname, and
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species):

        # Check if nickname already exists
        if self.nicknameMap.containsKey(nickname):
            # Return False if key = nickname already exists
            return False
        
        # Create a new entry to add using an instance of Entry 
        # object with key, value pair to add
        newEntry = Entry(nickname, species)

        # Add new entry to nicknameMap and return True indicating
        # object was added successfully
        self.nicknameMap.put(nickname, newEntry)
        return True 

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    def find(self, nickname, species):
        
        # Ensure nickname exists in our Box
        # Returns none if it doesn't
        entry = self.nicknameMap.get(nickname)
        
        # If the entry exists, return it
        if entry:
            return entry
        
        # If it doesn't exist return None
        return None

    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return an empty list if the Box is empty. """
    def findAllNicknames(self):
        # Use key method in MyHashMap to create a list of nicknames
        return self.nicknameMap.keys()

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return an empty list if the nickname is not in the Box. """
    def findEntryByNickname(self, nickname):
        # Assign Entry object value to entry
        entry = self.find(nickname, None)

        # Return an empty list if entry is None
        if entry is None:
            return []
        
        # Otherise return entry found using find method
        return entry

    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        # Use our existing remove method from myHashMap
        return self.nicknameMap.remove(nickname) 

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        # Assign entry with key, value pair obtained from the find method
        entry = self.find(nickname, species)

        # Since empty is not None
        if entry is not None:

            # Check species in entry matches species
            # in the removeEntry method
            if self.nicknameMap.MyHashMapEntry.getValue == species:
                self.nicknameMap.remove(nickname)
                return True
        
        # Return false if entry is None
        return False

if __name__ == '__main__':
    Box()