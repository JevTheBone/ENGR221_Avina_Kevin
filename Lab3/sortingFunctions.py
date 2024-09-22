"""
Name: Kevin Avina-Gutierrez
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

# Implementation of insertionSort algorithm
def insertionSort(list_to_sort:list) -> list:
    ### Add your insertionSort implementation here
    # Check through the number of indexes in list to sort
    for i in range(len(list_to_sort)):
        # Assign index 'i' to value 'j'
        j = i
        # Check if 'j-1' is grater than the value at 'j' for the list
        while j > 0 and list_to_sort[j-1] > list_to_sort[j]:
            ## Swap values between [j] and [j-1]
            # Store list[j] value
            temp = list_to_sort[j]
            # Assign list to sort[j] the value at [j-1]
            list_to_sort[j] = list_to_sort[j-1]
            # Assign list to sort[j-1] the original value of list to sort[j] using temp.
            list_to_sort[j-1] = temp
            # Update 'j' value index with 'j-1'
            j = j-1
    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort:list) -> list:
    ### Add your bubbleSort implementation here
    #print(list_to_sort)
    # Check for index is within the size of list to sort - 1
    for i in range(len(list_to_sort) - 1):
        # Index j within the size of list - 1 and - index 'i'
        for j in range(len(list_to_sort) - 1 - i):
            # If list[j] is grater than list[j+1]
            if list_to_sort[j] > list_to_sort[j+1]:
                # Swap values between [j] and [j+1]
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j+1]
                list_to_sort[j+1] = temp

    return list_to_sort

# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time


if __name__ == '__main__':
    pass