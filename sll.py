from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    """
    Inserts a new node at the beginning of the list

    Parameters:
    An object

    Returns:
    none
    """

    def insert_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self._head.next is None: #checks if its empty
            self._head.next = SLNode(value)
        else:
            temp = self._head.next
            self._head.next = SLNode(value, temp)

    """
    Inserts a new node at the back of the list

    Parameters:
    An object

    Returns:
    none
    """


    def insert_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """

        current = self._head

        for i in range(self.length()):
            current = current.next #traverses to back

        current.next = SLNode(value)

    """
    Inserts a new node at a sepcified index

    Parameters:
    An object and index

    Returns:
    none
    """

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self.length(): #exceptions
            raise SLLException
        
        current = self._head

        for i in range(index): #traverses to index
            current = current.next
        
        temp = current.next

        current.next = SLNode(value, temp)

    """
    Removes a new node at a sepcified index

    Parameters:
    An object and index

    Returns:
    none
    """

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self.length() - 1: #exceptions
            raise SLLException
        
        current = self._head

        for i in range(index): #traverses to index
            current = current.next

        current.next = current.next.next

    """
    Removes the first occurrence of a specified value from the list and returns a boolean for if something was removed

    Parameters:
    An object

    Returns:
    A boolean for if something was removed
    """

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        current = self._head

        flag = 0

        for i in range(self.length()):
            if current.next.value == value:
                flag = 1 #raises flag if found
                break
            current = current.next

        if flag == 1:
            current.next = current.next.next
            return 1
        
        return 0

    """
    Returns the amount of times a given object appears in the list

    Parameters:
    An object

    Returns:
    A int for the count
    """
        

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        count = 0

        current = self._head

        for i in range(self.length()):
            if current.next.value == value:
                count += 1 #adds to count if match
            current = current.next

        return count
    
    """
    Returns a boolean if a specified object is found in the list

    Parameters:
    An object

    Returns:
    A boolean for if the object was found
    """
    
    def find(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        current = self._head

        flag = 0

        for i in range(self.length()):
            if current.next.value == value:
                flag = 1 #raises flag if found
                break
            current = current.next

        if flag == 1:
            return 1
        
        return 0
    
    """
    Returns a new list object with a specified start index and length from the old list

    Parameters:
    Two ints for the start index and size of new list object

    Returns:
    A new linked list
    """

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        if start_index < 0 or start_index > self.length() - 1 or start_index + size > self.length() or size < 0:
            raise SLLException
        
        current = self._head
        
        for i in range(start_index):
            current = current.next

        new_linked_list = LinkedList()

        for i in range(size):
            new_linked_list.insert_back(current.next.value) #adds values according to size
            current = current.next

        return new_linked_list


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
