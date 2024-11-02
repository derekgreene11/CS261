# Name: Derek Greene
# OSU Email: greenede@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and ADT Implementation
# Due Date: 10/28/2024
# Description: Implimented a custom Bag ADT class and methods such as add, remove, count, and clear, among others.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Method to add given value to bag.
        Parameters: value: object
        Returns: None
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Method to remove one occurance of given value from bag and return True if removed, False otherwise.
        Parameters: value: object
        Returns: bool
        """
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        else:
            return False

    def count(self, value: object) -> int:
        """
        Method to count number of times given value occurs in bag.
        Parameters: value: object
        Return: int
        """
        count = 0

        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        Method to clear items from bag
        Parameters: None
        Returns: None
        """
        self._da = DynamicArray(None)

    def equal(self, second_bag: "Bag") -> bool:
        """
        Method to compare content of bag with contents of given 2nd bag. If bags = same num elements & elements match,
        returns True. Otherwise False. 
        Parameters: second_bag: "Bag"
        Returns: bool
        """
        if self._da.length() != second_bag._da.length():
            return False

        for i in range(self._da.length()):
            item = self._da.get_at_index(i)
            count1 = 0
            count2 = 0

            # Count occurance of items in first bag
            for x in range(self._da.length()):
                if self._da.get_at_index(x) == item:
                    count2 += 1
            # Count occurance of items in second bag
            for x in range(second_bag._da.length()):
                if second_bag._da.get_at_index(x) == item:
                    count1 += 1

            if count1 != count2:
                return False

        return True

    def __iter__(self):
        """
        Method to create iterator for loop
        Parameters: None
        Returns: object: self (iter object)
        """
        self._index = 0

        return self

    def __next__(self):
        """
        Method to get next item in bag for loops.
        Parameters: None
        Returns: object: value (next item object)
        """
        try:
            value = self._da.get_at_index(self._index)
        except DynamicArrayException:
            raise StopIteration
        self._index += 1 
        
        return value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
