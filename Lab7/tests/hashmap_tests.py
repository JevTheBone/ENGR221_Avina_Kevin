import pytest

from myHashMap import MyHashMap

# Write your tests here

@pytest.fixture

#define empty hashmap for testing
def emptyList():
    return MyHashMap()

@pytest.mark.isEmpty
#put functionality for MyHashMap
def test_put_on_empty(emptyList):
    # Checks that list is empty
    assert emptyList.isEmpty() == True

@pytest.mark.replace
#replace functionality for MyHashMap
def test_replace_on_empty(emptyList):
    #replace 1 with 2 in the hashmap
    emptyList.replace(1,3)
    #check if the value is None
    assert emptyList.get(1) == None

@pytest.mark.remove
#remove functionality for MyHashMap
def test_remove_on_empty(emptyList):
    #remove 1 from the hashmap
    emptyList.remove(1)
    #check if the value is None
    assert emptyList.get(1) == None