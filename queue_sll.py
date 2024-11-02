# Name: Derek Greene
# OSU Email: greenede@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3 Linked List and ADT Implementation 
# Due Date: 11/4/2024
# Description: Completed methods for Queue class to add items at end of queue, remove items from start of queue, and get value at front of queue.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Method to add given value at end of queue. 
        Parameters: value: object
        Returns: None
        """
        newNode = SLNode(value)

        if self.is_empty():
            self._head = newNode
            self._tail = newNode

        self._tail.next = newNode
        self._tail = newNode 

    def dequeue(self) -> object:
        """
        Method to remove and return value at start of queue. Raises exception if queue is empty.
        Parameters: None
        Returns: value: object
        """
        if self.is_empty():
            raise QueueException("ERROR: Empty Queue!")

        value = self._head.value
        self._head = self._head.next
        
        return value

    def front(self) -> object:
        """
        Method to return value at start of queue. Raises exception if queue is empty. 
        Parameters: None
        Returns: value: object
        """
        if self.is_empty():
            raise QueueException("ERROR: Empty Queue!")

        value = self._head.value

        return value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
