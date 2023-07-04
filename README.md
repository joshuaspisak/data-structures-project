# data-structures
Comprehensive Data Structures Implementation and Optimization Project

**Dynamic Array Implementation**
The DynamicArray class is built on top of the StaticArray class (provided in Assignment 1) and provides several methods similar to Python lists. These methods include resizing the array, appending elements, inserting elements at a specific index, removing elements at a specific index, slicing the array, merging arrays, mapping, filtering, reducing, and finding the mode.

**Bag ADT Implementation**
The Bag class represents a bag data structure, also known as a multiset, which allows duplicate elements. It provides methods for adding elements, removing elements, counting the occurrences of an element, clearing the bag, checking equality with another bag, and iteration.

**Singly Linked List Implementation**

insert_front(): Adds a new node at the beginning of the list.

insert_back(): Adds a new node at the end of the list.

insert_at_index(): Inserts a new value at the specified index position in the linked list.

remove_at_index(): Removes the node at the specified index position from the linked list.

remove(): Removes the first node that matches the provided value from the linked list.

count(): Counts the number of elements in the list that match the provided value.

find(): Checks if the provided value exists in the list.

slice(): Returns a new LinkedList object containing a specified number of nodes starting from a given index.


**Stack ADT - Dynamic Array Implementation**

push(): Adds an element to the top of the stack.

pop(): Removes and returns the top element from the stack.

top(): Returns the top element of the stack without removing it.


**Queue ADT - Static Array Implementation**

enqueue(): Adds an element to the rear of the queue.

dequeue(): Removes and returns the front element from the queue.

front(): Returns the front element of the queue without removing it.


**Stack ADT - Linked Nodes Implementation**

push(): Adds an element to the top of the stack.
  
pop(): Removes and returns the top element from the stack.
  
top(): Returns the top element of the stack without removing it.

**BST Tree Implementation**

add(self, value: object) -> None: Adds a new value to the BST. Duplicate values are allowed, and they will be added to the right subtree of the node with the same value.

remove(self, value: object) -> bool: Removes a value from the BST. The method returns True if the value is successfully removed; otherwise, it returns False.

contains(self, value: object) -> bool: Checks if the given value exists in the BST. Returns True if found; otherwise, False.

inorder_traversal(self) -> List[object]: Performs an inorder traversal of the BST and returns a list of elements in ascending order.

find_min(self) -> object: Returns the minimum value in the BST.

find_max(self) -> object: Returns the maximum value in the BST.

is_empty(self) -> bool: Checks if the BST is empty. Returns True if it is empty; otherwise, False.

make_empty(self) -> None: Empties the BST by removing all elements.

**AVL Tree Implementation**

add(self, value: object) -> None: Adds a new value to the AVL tree, maintaining the tree's balance.

remove(self, value: object) -> bool: Removes a value from the AVL tree while ensuring that the tree remains balanced. Returns True if the value is successfully removed; otherwise, False.

**MinHeap Implementation**

add(node: object) -> None: Adds a new object to the MinHeap while maintaining the heap property.

is_empty() -> bool: Returns True if the heap is empty, otherwise False.

get_min() -> object: Returns the object with the minimum key without removing it from the heap.

remove_min() -> object: Returns the object with the minimum key and removes it from the heap.

build_heap(da: DynamicArray) -> None: Builds a proper MinHeap from a given DynamicArray.

size() -> int: Returns the number of items currently stored in the heap.

clear() -> None: Clears the contents of the heap.

heapsort(arr: DynamicArray) -> None: Sorts the content of a DynamicArray in non-ascending order using the Heapsort algorithm.

**HashMap Implementation**

put(key, value): Updates the key/value pair in the hash map.

get(key): Returns the value associated with the given key.

remove(key): Removes the key/value pair from the hash map.

contains_key(key): Returns True if the given key is in the hash map, otherwise False.

clear(): Clears the contents of the hash map.

empty_buckets(): Returns the number of empty buckets in the hash table.

table_load(): Returns the current hash table load factor.

resize_table(new_capacity): Changes the capacity of the internal hash table.

get_keys_and_values(): Returns a list of tuples containing all key/value pairs in the hash map.

find_mode(): Returns the key that appears most frequently in the hash map.
