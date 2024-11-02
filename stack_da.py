# Name: Derek Greene
# OSU Email: greenede@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3 Linked List and ADT Implementation 
# Due Date: 11/4/2024
# Description: Completed methods for Stack class to push elements to stack, pop elements from stack, and return value at top of stack.


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Method to push given value to top of stack.
        Parameters: value: object
        Returns: None
        """
        self._da.append(value)

    def pop(self) -> object:
        """
        Method to pop value off top of stack and return its value. Raises exception if stack is empty.
        Parameters: None
        Returns: value: object
        """
        if self.is_empty():
            raise StackException("ERROR: Empty Stack!")
        else:
            value = self._da.get_at_index(self.size() - 1)
            self._da.remove_at_index(self.size() - 1)
            return value

    def top(self) -> object:
        """
        Method to return value at top of stack.
        Parameters: None
        Returns: top: object
        """
        if self.is_empty():
            raise StackException("ERROR: Empty Stack!")
        
        top = self._da.get_at_index(self.size() - 1)

        return top
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
