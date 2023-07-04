from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
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
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
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
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------
    
    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the dynamic array to the number passed in

        Parameters:
        An int

        Returns:
        nothing
        """
        #checks eligibility
        if new_capacity < 1 or new_capacity < self._size:
            return
        
        self._capacity = new_capacity

        new_arr = StaticArray(self._capacity)

        for i in range(self._size):
            #copies data
            new_arr[i] = self._data[i]

        self._data = new_arr

    def append(self, value: object) -> None:
        """
        Adds an object to the end of the array, increasing capacity as necessary

        Parameters:
        An object

        Returns:
        nothing
        """
        if self._capacity == self._size:
            #resize if necessary
            self.resize(self._capacity * 2)

        self._size += 1
        
        self[self._size - 1] = value

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts new object at specified index. shifting other elements right

        Parameters:
        An int and object

        Returns:
        nothing
        """    

        if self._capacity == self._size:
            self.resize(self._capacity * 2)

        if index < 0 or index >= self._size + 1:
            raise DynamicArrayException

        self._size += 1
        
        #new variable for current number
        current = self[index]
        self[index] = value

        for i in range(index + 1, self._size):
            temp = self[i]
            self[i] = current
            current = temp

    def remove_at_index(self, index: int) -> None:
        """
        Removes object at specified index, moving other elements left

        Parameters:
        An int

        Returns:
        nothing
        """

        #checks conditions
        if(self._size < float(self._capacity) / 4 and self._capacity > 10):
            self.resize(self._size * 2)
            if(self._capacity < 10):
                self.resize(10)

        self[index] = None

        for i in range(index, self._size - 1):
            self[i] = self[i + 1]

        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new array with specified starting index of old array and size

        Parameters:
        Two ints

        Returns:
        new dynamic array
        """

        #checks conditions to throw exception
        if size < 0 or start_index < 0 or start_index > self._size - 1 or start_index + size > self._size:
            raise DynamicArrayException

        new_arr = DynamicArray()

        for i in range(size):
            new_arr.append(self[start_index + i])

        return new_arr

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Adds a new array to the existing one

        Parameters:
        A second array

        Returns:
        nothing
        """
        for i in range(second_da._size):
            #uses append to add new values iteratively
            self.append(second_da[i])

    def map(self, map_func) -> "DynamicArray":
        """
        returns a new array with each value being put into the passed in function

        Parameters:
        A function

        Returns:
        new dynamic array
        """
        
        new_arr = DynamicArray()

        for i in range(self._size):
            #adds new values after pass through function
            new_arr.append(map_func(self[i]))

        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        returns a new array with each value that satisfies the function staying in

        Parameters:
        A function

        Returns:
        new dynamic array
        """
        new_arr = DynamicArray()

        for i in range(self._size):
            if filter_func(self[i]):
                #appends values that pass test
                new_arr.append(self[i])

        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        returns an object with the passed in function being applied sequentially

        Parameters:
        A function and optional initializer

        Returns:
        an object
        """
        #edge case
        if self._size == 0:
            return initializer

        if initializer == None:
            initializer = self[0]
            start = 1
        else:
            start = 0

        accumulator = initializer
        for i in range(start, self._size):
            #repeats process with itself
            accumulator = reduce_func(accumulator, self[i])

        return accumulator

def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    returns a tuple containing an array of the mode and the number of times the mode appears

    Parameters:
    A dynamic array

    Returns:
    tuple (dynamic array, int)
    """
    max_freq = 0
    mode = DynamicArray()

    curr_freq = 1
    for i in range(1, arr.length()):
        if arr[i] == arr[i-1]:
            curr_freq += 1
        else:
            if curr_freq > max_freq:
                max_freq = curr_freq
                #clears array
                mode = DynamicArray()
                #adds mode to array
                mode.append(arr[i-1])
            elif curr_freq == max_freq:
                mode.append(arr[i-1])
            curr_freq = 1

    # Handle case where the mode is at the end of the array
    if curr_freq > max_freq:
        max_freq = curr_freq
        mode = DynamicArray()
        mode.append(arr[arr.length() - 1])
    elif curr_freq == max_freq:
        mode.append(arr[arr.length() - 1])

    return (mode, max_freq)


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

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

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

    print("\n# find_mode - example 1")
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
