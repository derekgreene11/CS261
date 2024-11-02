# Name: Derek Greene
# OSU Email: greenede@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and ADT Implementation
# Due Date: 10/28/2024
# Description: Completed various methods of the DynamicArray class including methods to resize, append, map, filter, and reduce, among others. Also completed find_mode and chunk functions.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Method to resize dynamicArray to given new_capacity size.
        Parameters: new_capacity: int
        Returns: None
        """
        if new_capacity < self._size or new_capacity <= 0:
            return

        newStaticArray = StaticArray(new_capacity)

        for i in range(self._size):
            newStaticArray[i] = self._data[i]

        self._capacity = new_capacity
        self._data = newStaticArray

    def append(self, value: object) -> None:
        """
        Method to add given value to dynamicArray.
        Parameters: value: object
        Returns: None
        """
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Method to insert given value at given index. Raises an exception if index is out of range.
        Parameters: index: int, value: object
        Returns: None
        """
        if index < 0 or index > self._size:
            raise DynamicArrayException("Invalid Index")

        # If dynamicArray is full, double capacity
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Method to remove value at given index. Raises an exception is index is out of range.
        Parameters: index: int
        Returns: None
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Invalid Index")

        # If current elements < 1/4 capacity, reduce capacity to 2 * current elements    
        if self._size < (0.25 * self._capacity) and self._capacity > 10:
            self.resize(max(10, 2 * self._size))

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size -1] = None
        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Method to splice dynamicArray with given start and end points, and return a new dynamicArray 
        with the requested range of values. Raises an exception if start_index or size create a splice out of range.
        Parameters: start_index: int, size: int
        Returns: newDynamicArray: object
        """
        if start_index < 0 or start_index >= self._size or size < 0 or start_index + size > self._size:
            raise DynamicArrayException("Invalid Index, Size, or Splice")

        newDynamicArray = DynamicArray(None)

        for i in range(start_index, start_index + size):
            newDynamicArray.append(self._data[i])

        return newDynamicArray

    def map(self, map_func) -> "DynamicArray":
        """
        Method to imlement a given mapping function on each element of dynamicArray and 
        return new dynamicArray with resultant elements.
        Parameters: map_func: function
        Returns: newDynamicArray: object
        """
        newDynamicArray = DynamicArray(None)

        for i in range(self._size):
            value = map_func(self._data[i])
            newDynamicArray.append(value)

        return newDynamicArray

    def filter(self, filter_func) -> "DynamicArray":
        """
        Method to filter elements of dynamicArray based on given filter function and return new 
        dynamicArray with the resulant matches.
        Parameters: filter_func: function
        Returns: newDynamicArray: object
        """
        newDynamicArray = DynamicArray(None)

        for i in range(self._size):
            if filter_func(self._data[i]):
                newDynamicArray.append(self._data[i])

        return newDynamicArray

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Method to apply reduce function to elements of dynamicArray and return resultant value.
        If no initializer parameter provided, first elem of array is used. If dynamicArray is empty,
        returns value of initializer or None if no initializer provided.
        Parameters: recude_func: function, initializer: object
        Returns: result: object
        """
        if initializer is None:
            initializer = self._data[0]
            start = 1
        else:
            start = 0
        
        # If dynamicArray is empty, return initializer if provided, else return None
        if self._size == 0:
            if initializer is not None:
                return initializer
            else:
                return None

        result = initializer
        for i in range(start, self._size):
            result = reduce_func(result, self._data[i])

        return result

def chunk(arr: DynamicArray) -> "DynamicArray":
    """
    Function to take dynamicArray values and chunk them into an array of arrays, each with non-descending subsequences of values.
    Returned dynamicArray consists of an array in which each index consists of a dynamicArray containing one of the subsequences.
    Parameters: arr: DynamicArray
    Returns: chunks: object
    """
    chunks = DynamicArray(None)
    current = DynamicArray(None)

    if arr.is_empty():
        return DynamicArray(None)
    
    # Start at first element
    current.append(arr.get_at_index(0))

    for i in range(1, arr.length()):
        value = arr.get_at_index(i)
        lastV = current.get_at_index(current.length() - 1)
        
        # If non-descending
        if value >= lastV:
            current.append(value)
        else:
            chunks.append(current)
            current = DynamicArray(None)
            current.append(value)

    chunks.append(current)

    return chunks

def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Function to find the mode of given dynamicArray and return tuple with mode and frequency.
    Parameters: arr: DynamicArray
    Returns: tuple[DynamicArray, int]
    """
    count = 1
    maxC = 1
    current = arr.get_at_index(0)
    mode = DynamicArray(None)

    for i in range(1, arr.length()):
        value = arr.get_at_index(i)

        if value == current:
            count += 1
        else:
            if count > maxC:
                maxC = count
                mode = DynamicArray(None)
                mode.append(current)
            elif count == maxC:
                mode.append(current)

            current = value
            count = 1
    # Final check to account for last item
    if count > maxC:
        mode = DynamicArray(None)
        mode.append(current)
        maxC = count
    elif count == maxC:
        mode.append(current)

    return mode, maxC

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')

    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
