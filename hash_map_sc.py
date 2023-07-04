from include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        puts a new key, value pair in the hash table, or replaces the value if the key already exists

        Parameters:
        key, value pair

        Returns:
        nothing
        """

        #resizes if load factor is 1.0 or greater
        if self.table_load() >= 1.0:
            new_capacity = self._capacity * 2
            self.resize_table(new_capacity)

        #gets the right bucket based off of the key
        index = self._hash_function(key) % self._capacity
        bucket = self._buckets[index]

        #checks if that bucket has a node with that key, if not inserts new node and increases size
        if bucket.contains(key) is None:
            bucket.insert(key, value)
            self._size += 1
        #if key exists in that bucket, change value on the node with that key
        else:
            bucket.contains(key).value = value


    def empty_buckets(self) -> int:
        """
        counts number of empty buckets

        Parameters:
        just self

        Returns:
        an int
        """
        count = 0

        #goes through each bucket and adds to count if linked list is empty
        for i in range(self._capacity):
            if self._buckets[i].length() == 0:
                count += 1

        return count

    def table_load(self) -> float:
        """
        calulates the load factor

        Parameters:
        just self

        Returns:
        float
        """
        return self._size / self._capacity

    def clear(self) -> None:
        """
        empties the hash table

        Parameters:
        just self

        Returns:
        nothing
        """

        #sets each buckets to a new linked list to clear all data
        for i in range(self._capacity):
            self._buckets[i] = LinkedList()

        self._size = 0

    def resize_table(self, new_capacity: int) -> None:
        """
        changes the capacity to new amount

        Parameters:
        int for new capacity

        Returns:
        nothing
        """
        #takes care of edge case with 0 capacity
        if new_capacity < 1:
            return

        #makes sure new capacity is prime
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        #creates new da with the new capacity number of buckets
        new_buckets = DynamicArray()
        for i in range(new_capacity):
            new_buckets.append(LinkedList())

        old_buckets = self._buckets
        old_capacity = self._capacity
        self._size = 0

        self._buckets = new_buckets
        self._capacity = new_capacity

        #goes through each old bucket, iterating through each buckets linked list, and adding each key, value pair to the new buckets
        for i in range(old_capacity):
            bucket = old_buckets[i]
            for current in bucket:
                self.put(current.key, current.value)        

    def get(self, key: str) -> object:
        """
        returns the value for a given key, or nothing if it doesn't exist in the hash table

        Parameters:
        key to search

        Returns:
        the value or nothing
        """
        #gets the right bucket based off of the key
        index = self._hash_function(key) % self._capacity
        bucket = self._buckets[index]

        #checks the bucket for the key, and if it exists, returns value. otherwise return none
        for current in bucket:
            if current.key == key:
                return current.value
            
        return None

    def contains_key(self, key: str) -> bool:
        """
        checks if a given key is in the hash table

        Parameters:
        key to search for

        Returns:
        bool if it exists or not in hash table
        """
        #finds the correct bucket
        index = self._hash_function(key) % self._capacity
        bucket = self._buckets[index]

        #employs existing contains function from the linkedlist implementation
        if bucket.contains(key):
            return True
            
        return False

    def remove(self, key: str) -> None:
        """
        removes a given key, value pair if the key exists

        Parameters:
        key to search

        Returns:
        nothing
        """
        #gets the right bucket based off of the key
        index = self._hash_function(key) % self._capacity
        bucket = self._buckets[index]

        #removes the key and its value if it exists in the bucket
        if bucket.remove(key):
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        returns an array of all the key, value pairs in the hash table

        Parameters:
        just self

        Returns:
        array
        """
        #creates new blank array
        arr = DynamicArray()

        #goes through all buckets and adds the key, value pairs
        for i in range(self._capacity):
            for current in self._buckets[i]:
                arr.append((current.key, current.value))

        return arr

        



def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    finds the numbers with most occurrences in the array and how many times they occur

    Parameters:
    array

    Returns:
    tuple with array and int
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap()

    #counts the frequency of each element in the array
    for i in range(da.length()):
        if map.contains_key(da[i]) == 0:
            map.put(da[i], 1)
        else:
            map.put(da[i], map.get(da[i]) + 1)

    #finds the maximum frequency
    max_frequency = 0
    for i in range(da.length()):
        frequency = map.get(da[i])
        if frequency > max_frequency:
            max_frequency = frequency

    #collects all elements with the maximum frequency
    mode_values = DynamicArray()
    for i in range(da.length()):
        flag = 0
        frequency = map.get(da[i])
        if frequency == max_frequency:
            for j in range(mode_values.length()):
                if mode_values[j] == da[i]:
                    flag = 1
            if flag == 0:
                mode_values.append(da[i])

    return mode_values, max_frequency


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(23, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
