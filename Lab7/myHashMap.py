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
        if key == None:
            raise Exception("Error: key is None.")
        
        # Mod keyHash value by the current capacity value, store value within "index"
        index = keyHash % self.capacity
        print(self.capacity, index)
        
        # Using the existing HashMapEntry function we designate key and value to a hashEntry
        hashEntry = self.MyHashMapEntry(key, value)

        # Base statement: index greator than/equal to 0 and self.capacity
        if index >= 0 and index < self.capacity:
        # Given that the index meets requirements, next compare size to that of load * cap
            if self.size < self.capacity * self.load_factor:
                # Call rezise function and exit second loop
                self.resize() 
        # increase size of hash map by 1
            self.size += 1
        # Add our hashEntry to self.buckets with the specified index and return True
            self.buckets[index].append(hashEntry)
            return True
        # exit first loop and return false if index doesn't meet specified requirements
        return False

        

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        # TODO: write your replace implementation here
        pass

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        # TODO: write your remove implementation here
        pass 

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        # TODO: Write your set implementation here
        pass 

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        # TODO: Write your get implementation here 
        pass 

    """
    Return the number of key, value pairs in this MyHashMap. """
    def size(self):
        # TODO: Write your size implementation here 
        pass 

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        # TODO: Write your isEmpty implementation here
        pass 

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        # TODO: Write your containsKey implementation here 
        pass 

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        # TODO: Write your keys implementation here
        pass 

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