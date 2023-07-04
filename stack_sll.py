from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    
    """
    Adds a value to the top of the stack

    Parameters:
    An object

    Returns:
    none
    """
    
    def push(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        
        new_node = SLNode(value, self._head) #creates new node

        self._head = new_node #puts it at the beginning

    """
    Removes the object at the top of the stack and returns its value

    Parameters:
    none

    Returns:
    The value of the object at the top of the stack
    """

    def pop(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.size() == 0:
            raise StackException
        
        pop_val = self._head.value #saves value

        self._head = self._head.next #skips over it to remove it

        return pop_val
    
    """
    Returns the value of the object at the top of the stock

    Parameters:
    none

    Returns:
    Object value
    """

    def top(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.size() == 0:
            raise StackException

        return self._head.value #returns front value

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
