import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        adds an object to the BST

        parameters:
        an object

        returns:
        nothing
        """

        #creates a new node
        new_node = BSTNode(value)

        #if no objects in tree
        if self._root is None:
            self._root = new_node

        else:
            p = None
            n = self.get_root()

            #find right spot
            while n is not None:
                p = n
                if value < n.value:
                    n = n.left
                else:
                    n = n.right
            if value < p.value:
                p.left = new_node
            else:
                p.right = new_node

    def remove(self, value: object) -> bool:
        """
        removes an object from the BST

        parameters:
        a value

        returns:
        a bool if something was removed
        """
        p = None
        n = self.get_root()

        #find reight node to be removed
        while n is not None:
            if n.value == value:
                break
            p = n
            if value < n.value:
                n = n.left
            else:
                n = n.right

        #if node not found
        if n is None:
            return False
        
        #three cases (no, 1, or 2 subtrees)
        if n.left is None and n.right is None:
            self._remove_no_subtrees(p, n)
        elif (n.left is not None and n.right is None) or n.left is None and n.right is not None:
            self._remove_one_subtree(p, n)
        else:
            self._remove_two_subtrees(p, n)

        return True
        

    # Consider implementing methods that handle different removal scenarios; #
    # you may find that you're able to use some of them in the AVL.          #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change these methods in any way you'd like.                            #

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        helper function for removing node with no subtrees

        parameters:
        the node to remove and its parent

        returns:
        nothing
        """
        # remove node that has no subtrees (no left or right nodes)
        if remove_parent is None:
            self._root = None
        elif remove_node.value < remove_parent.value:
            remove_parent.left = None
        else:
            remove_parent.right = None
        

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        helper function for removing node with one subtree

        parameters:
        the node to remove and its parent

        returns:
        nothing
        """
        # remove node that has a left or right subtree (only)
        if remove_parent is None:
            if remove_node.left is None:
                self._root = remove_node.right
            else:
                self._root = remove_node.left

        #if right child exists
        elif remove_node.left is None:
            if remove_node.value < remove_parent.value:
                remove_parent.left = remove_node.right
            else:
                remove_parent.right = remove_node.right

        #if left child exists
        elif remove_node.right is None:
            if remove_node.value < remove_parent.value:
                remove_parent.left = remove_node.left
            else:
                remove_parent.right = remove_node.left

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        helper function for removing node with two subtrees

        parameters:
        the node to remove and its parent

        returns:
        nothing
        """
        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        successor_parent = remove_node
        successor_node = remove_node.right

        #find inorder successors
        while successor_node.left is not None:
            successor_parent = successor_node
            successor_node = successor_node.left

        successor_node.left = remove_node.left

        #reassign relationships if the inorder successor is not the direct child of the node to remove
        if successor_node is not remove_node.right:
            successor_parent.left = successor_node.right
            successor_node.right = remove_node.right

        if remove_parent is None:
            self._root = successor_node

        elif remove_node.value < remove_parent.value:
            remove_parent.left = successor_node
        else:
            remove_parent.right = successor_node


    def contains(self, value: object) -> bool:
        """
        checks if a value is in the tree

        parameters:
        a value

        returns:
        a bool if it was found
        """
        if self._root is None:
            return False
        
        n = self.get_root()

        #looks through tree and checks nodes
        while n is not None:
            if n.value == value:
                break
            if value < n.value:
                n = n.left
            else:
                n = n.right

        #if not found
        if n is None:
            return False
        
        #if found
        return True

    def inorder_traversal(self) -> Queue:
        """
        gives the inorder traversal results for the BST

        parameters:
        just self

        returns:
        a Queue filled with the inorder traversal
        """
        #creates new queue
        result = Queue()

        #uses helper
        self.inorder_helper(result, self._root)

        return result

        
    def inorder_helper(self, queue: Queue, node: BSTNode) -> None:

        """
        helper function for inorder traveral

        parameters:
        a queue and a node

        returns:
        nothing
        """

        #recursive calls to get inorder traversal (left, itself, right)
        if node is not None:
            self.inorder_helper(queue, node.left)
            queue.enqueue(node.value)
            self.inorder_helper(queue, node.right)

    def find_min(self) -> object:
        """
        finds the minimum value in the tree

        parameters:
        just self

        returns:
        min value
        """
        if self._root is None:
            return None

        n = self._root

        #just goes all the way left since already sorted
        while n.left is not None:
            n = n.left

        return n.value

    def find_max(self) -> object:
        """
        finds the maximum value in the tree

        parameters:
        just self

        returns:
        max value
        """
        if self._root is None:
            return None

        n = self._root

        #just goes all the way to the right since already sorted
        while n.right is not None:
            n = n.right

        return n.value

    def is_empty(self) -> bool:
        """
        checks if the BST is empty

        parameters:
        just self

        returns:
        bool if empty or not
        """
        #just has to check if root exists
        if self._root is None:
            return True
        
        return False

    def make_empty(self) -> None:
        """
        makes the BST empty

        parameters:
        just self

        returns:
        nothing
        """
        #just has to make the root None
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
