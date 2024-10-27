"""
Kevin Avina-Gutierrez
myHashMap.py
Implement a hash map class for a Box system, upon completition of the hash class
Test the functionality of the class by writing at least 3 tests.

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Create a new set of buckets that's twice as big as the old one
        new_buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in self.buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())
        # Update the self.buckets attribute with the new entries
        self.buckets = new_buckets

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        # Adds the specified key using hash function
        keyHash = hash(key)
        # TODO: write your replace implementation here
        # Checks that key isn't None
        if key is None:
            raise Exception("Error: key can't be None.")    

        # Calculate bucket index before adding entry into self.buckets
        bucket_index = keyHash % self.capacity
        # Using MapEntry constructor we assign key value pair to hashEntry
        hashEntry = self.MyHashMapEntry(key, value)

        # If adding a new key would surpass load_factor 
        # Call resize method to increase capacity 
        if ((self.size + 1) / self.capacity > self.load_factor):
            self.resize()
            
        # Checks bucket index for duplicates, 
        # Returns false if key exists
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                return False
                
            # Since key isn't a duplicate and we have enough capacity
            # Add key-value pair and increment size
            self.buckets[bucket_index].append(hashEntry)
            self.size += 1
            return True 

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        # TODO: write your replace implementation here
        # Checks that key isn't None
        if key is None:
            raise Exception("Error: key can't be None.")

        # Calculate bucket index
        bucket_index = hash(key) % self.capacity

        # Check if the key exists in the corresponding bucket list
        for entry in self.buckets[bucket_index]:
            # If key found, replace value assigned to key 
            # with newValue and return True
            if entry.key == key:
                entry.value = newValue
                return True
                
        # Return false if key is not found
        return False

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        # TODO: write your remove implementation here
        # Checks that key isn't None
        if key is None:
            raise Exception("Error: key can't be None.")

        # Calculate bucket index
        bucket_index = hash(key) % self.capacity

        # Check if the key exists in the corresponding bucket list
        for entry in self.buckets[bucket_index]:
            # If key is found, remove the entry 
            # corresponding to the given key
            if entry.key == key:
                self.buckets[bucket_index].remove(entry)
                return True
            
        # Return false if key is not found
        return False

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        # TODO: Write your set implementation here
        # Checks that key isn't None
        if key is None:
            raise Exception("Error: key can't be None.")

        # Call replace method for key, value pair
        if not self.replace(key, value):
            # If replace() method returns false, key was not found
            # Add the new entry in the appropriate bucket
            self.put(key, value)
        return

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        # TODO: Write your get implementation here 
        # Checks that key isn't None
        if key is None:
            raise Exception("Error: key can't be None.")

        # Calculate bucket index
        bucket_index = hash(key) % self.capacity

        # Check if the key is in bucket lists
        for entry in self.buckets[bucket_index]:
            # Returns value of the specified key
            if entry.key == key:
                return entry.value
        # Key does not exist in MyHashMap
        return None

    """
    Return the number of key, value pairs in this MyHashMap. """
    def size(self):
        # TODO: Write your size implementation here 
        # Returns number of key, value pairs
        return self.size 

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self) -> bool:
        # TODO: Write your isEmpty implementation here
        # Returns True if hashmap is empty, False if there
        # are elements present
        return self.size == 0
         
    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        # TODO: Write your containsKey implementation here 
        # Check that key isn't None
        if key is None:
            raise Exception("Error: key can't be None.") 
        
        # Calculate index value
        bucket_index = hash(key) % self.capacity
        
        # Loops through bucket list and returns true if key is found
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                return True
        return False

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        # TODO: Write your keys implementation here
        # Initialize list of keys
        keyList = []

        # Iterate through each bucket in bucket list
        for bucket in self.buckets:
            # Look at each entry in bucket
            for entry in bucket:
                # Add each key entry to the list of keys
                keyList.append(entry.key)
        return keyList 

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 

if __name__ == "__main__":
    pass