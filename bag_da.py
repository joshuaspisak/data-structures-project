from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
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
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    """
    adds a new object to the bag

    Parameters:
    An object

    Returns:
    nothing
    """

    def add(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        self._da.append(value) #uses append function from dynamic array

    """
    removes a specific object from the bag

    Parameters:
    An object

    Returns:
    boolean
    """

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        for i in range(self.size()):
            if self._da[i] == value: #checks for match
                self._da.remove_at_index(i)
                return True
        return False
    
    """
    counts the occurrences of a specific object in the bag

    Parameters:
    An object

    Returns:
    int
    """

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """

        count = 0

        for i in range(self.size()):
            if self._da[i] == value: #checks for match
                count += 1

        return count
    
    """
    clears the bag

    Parameters:
    itself (nothing)

    Returns:
    nothing
    """

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        self._da = DynamicArray() #makes new array that is empty

    """
    returns a boolean if the bags are equal

    Parameters:
    A second bag

    Returns:
    boolean
    """

    def equal(self, second_bag: "Bag") -> bool:
        """
        TODO: Write this implementation
        """
        if self.size() != second_bag.size():
            return False
    
        # Check if each element in the first bag appears the same number of times in the second bag
        for i in range(self.size()):
            value = self._da[i]
            if self.count(value) != second_bag.count(value): #flag case
                return False
            
        # If we get here, the bags are equal
        return True
    
    """
    creates an iterator

    Parameters:
    self

    Returns:
    self
    """

    def __iter__(self):
        """
        TODO: Write this implementation
        """
        self.index = 0 #sets iterator

        return self
    
    """
    goes to next value

    Parameters:
    self

    Returns:
    current value
    """

    def __next__(self):
        """
        TODO: Write this implementation
        """
        try:
            value = self._da[self.index]
        except DynamicArrayException:
            raise StopIteration
        
        self.index = self.index + 1 #increases iterator
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
