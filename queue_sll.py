from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
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
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    """
    Adds an object to the back of the queue

    Parameters:
    an object

    Returns:
    none
    """
    
    def enqueue(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        new_node = SLNode(value) #creates the node to be added

        if self.size() == 0: #case if queue is empty
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node


    """
    Removes the object at the front of the queue and returns its value

    Parameters:
    none

    Returns:
    object value
    """

    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.size() == 0:
            raise QueueException
        
        front_val = self._head.value #saves value

        self._head = self._head.next #skips over value to remove it

        return front_val
    
    """
    Returns the value of the object of the front of the queue

    Parameters:
    none

    Returns:
    object
    """

    def front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.size() == 0:
            raise QueueException

        return self._head.value #no need to remove


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
