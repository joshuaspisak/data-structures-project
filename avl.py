import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations.
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds an object to the AVL and automatically balances the tree

        parameters:
        an object

        returns:
        nothing
        """
        
        new_node = AVLNode(value)

        p = None

        #case where no objects are in tree
        if self._root is None:
            self._root = new_node

        else:
            n = self.get_root()

            #find the correct spots
            while n is not None:
                p = n
                if value < n.value:
                    n = n.left
                elif value > n.value:
                    n = n.right
                else:
                    return
            #left or right depending on value
            if value < p.value:
                p.left = new_node
            else:
                p.right = new_node

        new_node.parent = p

        new_insert = new_node

        new_parent = new_insert.parent

        #now rebalance after insert
        while new_parent is not None:
            self._rebalance(new_parent)
            new_parent = new_parent.parent
            
    def remove(self, value: object) -> bool:
        """
        Removes an object from the AVL and automatically balances the tree

        parameters:
        an value

        returns:
        a boolean whether it removed something or not
        """
        p = None
        n = self.get_root()

        #find correct value to remove
        while n is not None:
            if n.value == value:
                break
            p = n
            if value < n.value:
                n = n.left
            else:
                n = n.right

        #if nothing is found
        if n is None:
            return False
        
        #no subtrees
        if n.left is None and n.right is None:
            if p is None:
                new_center = n
            else:
                new_center = p
            self._remove_no_subtrees(p, n)
            self._update_height(new_center)
        #one subtree
        elif (n.left is not None and n.right is None) or n.left is None and n.right is not None:
            if p is None:
                new_center = n
            else:
                new_center = p
            self._remove_one_subtree(p, n)
            self._update_height(new_center)
        #two subtrees
        else:
            new_center = self._remove_two_subtrees(p, n)

        #now rebalance after removal
        while new_center is not None:
            self._rebalance(new_center)
            new_center = new_center.parent

        return True

    def _remove_two_subtrees(self, remove_parent: AVLNode, remove_node: AVLNode) -> AVLNode:
        """
        Helper function for removing node with two subtrees

        parameters:
        the node to remove and its parent

        returns:
        the node to start rebalancing at
        """

        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        successor_parent = remove_node
        successor_node = remove_node.right

        #find the inorder successor
        while successor_node.left is not None:
            successor_parent = successor_node
            successor_node = successor_node.left

        successor_node.left = remove_node.left

        #reassign relationships
        if successor_node is not remove_node.right:
            successor_parent.left = successor_node.right
            if successor_parent.left is not None:
                successor_parent.left.parent = successor_parent
            successor_node.right = remove_node.right
            remove_node.right.parent = successor_node

        successor_node.parent = remove_parent

        if successor_node.parent is None:
            self._root = successor_node

        elif remove_node.value < remove_parent.value:
            successor_node.parent.left = successor_node
        else:
            successor_node.parent.right = successor_node

        remove_node.left.parent = successor_node

        #temporary variable to update heights
        if successor_parent == remove_node:
            temp = successor_node
        else:
            temp = successor_parent

        while temp is not None:
            self._update_height(temp)
            temp = temp.parent

        #return the node to start at for rebalancing
        if successor_parent == remove_node:
            return successor_node
        else:
            return successor_parent

    def _balance_factor(self, node: AVLNode) -> int:
        """
        Calculates the balance factor for a node

        parameters:
        a node

        returns:
        an int value
        """
        return self._get_height(node.right) - self._get_height(node.left)

    def _get_height(self, node: AVLNode) -> int:
        """
        Returns the height of a node

        parameters:
        a node

        returns:
        an int value
        """
        #empty nodes have height of -1
        if node is None:
            return -1
        
        return node.height

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        rotates a node and its subtrees left (right-heavy)

        parameters:
        a node

        returns:
        a node for the new subtree root
        """

        #variable for new root
        c = node.right
        node.right = c.left
        #reassign relationships
        if node.right is not None:
            node.right.parent = node
        c.left = node
        c.parent = node.parent
        #condition where new subtree root is tree root
        if c.parent is None:
            self._root = c
        node.parent = c
        #update heights
        self._update_height(node)
        self._update_height(c)
        return c

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        rotates a node and its subtrees right (left-heavy)

        parameters:
        a node

        returns:
        a node for the new subtree root
        """

        #variable for new root
        c = node.left
        node.left = c.right
        #reassign relationships
        if node.left is not None:
            node.left.parent = node
        c.right = node
        c.parent = node.parent
        #condition where new subtree root is tree root
        if c.parent is None:
            self._root = c
        node.parent = c
        #update heights
        self._update_height(node)
        self._update_height(c)
        return c

    def _update_height(self, node: AVLNode) -> None:
        """
        updates the height of a node

        parameters:
        a node

        returns:
        nothing
        """

        #returns the max height of its children plus one
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _rebalance(self, node: AVLNode) -> None:
        """
        rebalances a subtree

        parameters:
        a node

        returns:
        nothing
        """

        #if left heavy
        if self._balance_factor(node) < -1:
            #if LR
            if self._balance_factor(node.left) > 0:
                node.left = self._rotate_left(node.left)
                node.left.parent = node
            newSubtreeRoot = self._rotate_right(node)
            node = newSubtreeRoot
            if node.parent is not None:
                if node.parent.value <= node.value:
                    node.parent.right = node
                else:
                    node.parent.left = node
        #if right heavy
        elif self._balance_factor(node) > 1:
            #if RL
            if self._balance_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
                node.right.parent = node
            newSubtreeRoot = self._rotate_left(node)
            node = newSubtreeRoot
            if node.parent is not None:
                if node.parent.value <= node.value:
                    node.parent.right = node
                else:
                    node.parent.left = node
        #if already balanced just update height
        else:
            self._update_height(node)
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
