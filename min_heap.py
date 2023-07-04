from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        adds a new object to the heap

        Parameters:
        an object

        Returns:
        nothing
        """
        #uses the DynamicArray function to first add to end of array
        self._heap.append(node)

        current = self._heap.length() - 1

        #percolates up to find right spot
        while current != 0:
            if self._heap[(current - 1) // 2] > node:
                self._heap[current] = self._heap[(current - 1) // 2]
                self._heap[(current - 1) // 2] = node
                current = (current - 1) // 2
            else:
                break

    def is_empty(self) -> bool:
        """
        checks if the heap is empty

        Parameters:
        just self

        Returns:
        a boolean
        """
        #checks if length is 0
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        returns the minimum value in heap

        Parameters:
        just self

        Returns:
        an object
        """
        #excpetion if heap is empty
        if self._heap.length() == 0:
            raise MinHeapException
        
        #just return first value
        return self._heap[0]

    def remove_min(self) -> object:
        """
        removes the minimum value in heap and restructures heap to fit rules

        Parameters:
        just self

        Returns:
        the objec that was removed
        """
        #if empty exception
        if self._heap.length() == 0:
            raise MinHeapException
        
        value = self._heap[0]

        #sets the first value equal to the last value

        self._heap[0] = self._heap[self._heap.length() - 1]

        #removes last value

        self._heap.remove_at_index(self._heap.length() - 1)

        if self._heap.length() <= 1:
            return value
        
        #percolate helper function to put in right spot
        
        _percolate_down(self._heap, 0, -1)

        return value

    def build_heap(self, da: DynamicArray) -> None:
        """
        changes a DynamicArray into a valid heap

        Parameters:
        a Dynamic Array

        Returns:
        nothing
        """
        #creates a new DynamicArray to ensure underlying DynamicArray of heap and input are different references
        self._heap = DynamicArray(da)

        #starts at first location where it could break the heap rules

        current = self._heap.length() // 2 - 1

        #percolates down with helper function
        while current >= 0:
            _percolate_down(self._heap, current, -1)
            current -= 1

    def size(self) -> int:
        """
        returns size of heap

        Parameters:
        just self

        Returns:
        int for size
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        clears the heap

        Parameters:
        just self

        Returns:
        nothing
        """

        #sets the heap to a new blank array
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    sorts the data in an array in non-ascending order

    Parameters:
    a DynamicArray

    Returns:
    nothing
    """
    #edge case
    if da.length() == 1:
        return

    current = da.length() // 2 - 1

    #this is building a heap out of the DynamicArray
    while current >= 0:
        _percolate_down(da, current, -1)
        current -= 1

    #the border is the edge of where the heap is and where data is already sorted

    border = da.length() - 1

    #continue until border is 0
    while border >= 1:
        temp = da[border]

        #swaps first value and value by border to get lowest values towards end of heap
        da[border] = da[0]

        da[0] = temp

        #percolate helper function

        _percolate_down(da, 0, border)

        border -= 1

    #one last comparison and potential swap

    if da[0] < da[1]:
        temp = da[1]

        da[1] = da[0]

        da[0] = temp

    

# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int, border: int) -> None:
    """
    goes down the heap checking if a parent is greater than one of its children, swapping with lowest one

    Parameters:
    a DynamicArray, int for index of parent, and int for border

    Returns:
    nothing
    """

    while True:

        two_children = 0

        #checks if the smaller of the two children is beyond the eligible bounds
        if 2 * parent + 1 >= da.length() or (2 * parent + 1 >= border and border != -1):
            return
        
        #checks if the parent has two children
        if 2 * parent + 2 < da.length():
            two_children = 1

        if two_children == 1:
            #checks if at aleast one child is less than parent
            if da[2 * parent + 1] < da[parent] or da[2 * parent + 2] < da[parent]:
                #if right child is least
                if da[2 * parent + 2] < da[2 * parent + 1] and (2 * parent + 2 < border or border == -1):
                    temp = da[parent]
                    da[parent] = da[2 * parent + 2]
                    da[2 * parent + 2] = temp
                    parent = 2 * parent + 2
                #if left child is least
                elif da[2 * parent + 2] >= da[2 * parent + 1]:
                    temp = da[parent]
                    da[parent] = da[2 * parent + 1]
                    da[2 * parent + 1] = temp
                    parent = 2 * parent + 1
                else:
                    return
            else:
                return
        #if only one child
        else:
            if da[2 * parent + 1] < da[parent]:
                    temp = da[parent]
                    da[parent] = da[2 * parent + 1]
                    da[2 * parent + 1] = temp
                    parent = 2 * parent + 1
            else:
                return

    
    


        




# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
