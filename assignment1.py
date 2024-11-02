# Name: Derek Greene
# OSU Email: greenede@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1 Python Fundamentals Review
# Due Date: 10/21/2024
# Description: Review of python fundamentals


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
"""
    Function to find min and max of StaticArray
    Parameters: arr: StaticArray
    Returns: tuple[int, int]
"""
def min_max(arr: StaticArray) -> tuple[int, int]:
    minimum = arr.get(0)
    maximum = arr.get(0)
    
    if arr.length() > 1:
        for i in range(1, arr.length()):
            input = arr.get(i)
            
            if input < minimum:
                minimum = input
            if input > maximum:
                maximum = input
                
    return (minimum, maximum)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
"""
    Function to read existing static array and return new "converted" StaticArray object
    Parameters: arr: StaticArray
    Returns: StaticArray
"""
def fizz_buzz(arr: StaticArray) -> StaticArray:
    newStaticArray = StaticArray(arr.length())
    
    for i in range(0, arr.length()):
        input = arr.get(i)
        
        if input % 5 == 0 and input % 3 == 0:
            newStaticArray.set(i, "fizzbuzz")
        elif input % 3 == 0:
            newStaticArray.set(i, "fizz")
        elif input % 5 == 0:
            newStaticArray.set(i, "buzz")
        else:
            newStaticArray.set(i, input)

    return newStaticArray

# ------------------- PROBLEM 3 - REVERSE -----------------------------------
"""
    Function to reverse StaticArray in-place.
    Parameters: arr: StaticArray
    Returns: None
"""
def reverse(arr: StaticArray) -> None:
    arrayStart = 0
    arrayEnd = arr.length() - 1
    
    # reverse array by tracking beginning and end of array and swapping elements
    while arrayStart < arrayEnd:
        arr[arrayStart], arr[arrayEnd] = arr[arrayEnd], arr[arrayStart]
        arrayStart += 1
        arrayEnd -= 1
    
    return None
# ------------------- PROBLEM 4 - ROTATE ------------------------------------
"""
    Function to rotate elements of Static Array left or right 'steps' number of places. 
    If steps is positive, elements are moved to the right, when steps is negative, elements are moved to the left.
    Parameters: arr: StaticArray, steps: int
    Returns: StaticArray
"""
def rotate(arr: StaticArray, steps: int) -> StaticArray:
    newStaticArray = StaticArray(arr.length())
    # handle cases when steps > arr.length()
    steps = steps % arr.length()
    
    for i in range(arr.length()):        
        if steps > 0:
            index = (i + steps) % arr.length()
        else:
            index = (i + (arr.length() + steps)) % arr.length()
        newStaticArray.set(index, arr.get(i))
            
    return newStaticArray

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
"""
    Function that receives to ints and generates an array compliled of the values between those two ints.
    Parameters: start: int, end: int
    Returns: StaticArray
"""
def sa_range(start: int, end: int) -> StaticArray:
    index = 0
    
    if start < end:
        newStaticArray = StaticArray(end - start + 1)
        
        for i in range(start, end + 1):
            newStaticArray.set(index, i)
            index += 1
    else:
        newStaticArray = StaticArray(start - end + 1)
        
        for i in range(start, end -1, -1):
            newStaticArray.set(index, i)
            index += 1
        
    return newStaticArray

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
"""
    Function that reads the values from an array and determines if they are sorted in ascending order, 
    descening order, or neither. Function than returns an int corresponding to sort status.
    Parameters: arr: StaticArray
    Returns: int:
"""
def is_sorted(arr: StaticArray) -> int:
    if arr.length() <= 1:
        return 1
    
    sortedAsc = True
    sortedDes = True
    
    for i in range(arr.length() - 1):
        current = arr.get(i)
        next = arr.get(i + 1)
        if current < next:
            sortedDes = False
        elif current > next:
            sortedAsc = False
        else: 
            return 0
           
    if sortedAsc:
        return 1
    elif sortedDes and not sortedAsc:
        return -1
    else:
        return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------
"""
    Function that reads the values from an array and determines the mode and frequency of the mode. 
    Parameters: arr: StaticArray
    Returns: tuple[object, int]:
"""
def find_mode(arr: StaticArray) -> tuple[object, int]:
    max = 1
    duplicates = 1
    mode = arr.get(0)
    
    for i in range(1, arr.length()):
        if arr.get(i) == arr.get(i - 1):
            duplicates += 1
        else:
            if duplicates > max:
                max = duplicates
                mode = arr.get(i - 1)
            duplicates = 1
    
    if duplicates > max:
        mode = arr.get(arr.length() - 1)
        max = duplicates

    return (mode, max)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------
"""
    Function that reads the values from an array and writes the non-duplicates to a new array. 
    Parameters: arr: StaticArray
    Returns: StaticArray:
"""
def remove_duplicates(arr: StaticArray) -> StaticArray:
    duplicates = 1
    index = 0
    tempStaticArray = StaticArray(arr.length())
    tempStaticArray.set(index, arr.get(0))
    index += 1
    
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            tempStaticArray.set(index, arr.get(i))
            index += 1
    
    # return correct size array with just duplicates
    newStaticArray = StaticArray(index)
    for i in range(index):
        newStaticArray.set(i, tempStaticArray.get(i))

    return newStaticArray            

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
"""
    Function that reads the values from an array and sorts them into a new array in non-ascending order using count sort algorithm.
    Parameters: arr: StaticArray
    Returns: StaticArray:
"""
def count_sort(arr: StaticArray) -> StaticArray:
    minVar, maxVar = min_max(arr)
    rangeVar = (maxVar - minVar) + 1
    occCount = StaticArray(rangeVar)
    
    # initialize StaticArray
    for i in range(rangeVar):
        occCount.set(i, 0)
    
    # count each element
    for i in range(arr.length()):
        index = arr.get(i) - minVar   
        occCount.set(index, occCount.get(index) + 1)
        
    count = 0
    for i in range(rangeVar):
        count += occCount.get(i)
            
    sorted = 0
    newStaticArray = StaticArray(count)
    for i in range(rangeVar - 1, -1, -1):
        while occCount.get(i) > 0:
            newStaticArray.set(sorted, i + minVar)
            sorted += 1
            occCount.set(i, occCount.get(i) - 1)
    
    return newStaticArray

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------
"""
    Function that reads the values from an array and calculates the squares of each element. Results are returned in a new StaticArray.
    Parameters: arr: StaticArray
    Returns: StaticArray:
"""
def sorted_squares(arr: StaticArray) -> StaticArray:
    start = 0
    end = arr.length() - 1
    index = arr.length() - 1
    
    newStaticArray = StaticArray(arr.length())
    
    while start <= end:
        square1 = arr.get(start) ** 2
        square2 = arr.get(end) ** 2
        if square1 > square2:
            newStaticArray.set(index, square1)
            start += 1
        else:
            newStaticArray.set(index, square2)
            end -= 1
        index -= 1
    
    return newStaticArray

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
