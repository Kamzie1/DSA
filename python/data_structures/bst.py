from node import Node
from dfs import postorder, preorder, inorder

class BST:
    def __init__(self):
        self.node = None

    def add(self, val):
        """
        time: O(n), omega(logn)
        space: O(1)
        """
        if self.node is None:
            self.node = Node(val)
            return
        node = self.node
        while True:
            if val < node.val:
                if node.left is None:
                    node.left= Node(val)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(val)
                    return
                node = node.right

    def min_val(self):
        node =  self.min()
        if node is not None:
            return node.val
        return None

    @staticmethod
    def _min(node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def min(self):
        return BST._min(self.node)

    def max_val(self):
        node =  self.max()
        if node is not None:
            return node.val
        return None

    def max(self):
        node = self.node
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    def find(self, val)->Node|None:
        """
        time: O(n), omega(logn)
        space: O(n)
        """
        node = self.node
        if node is None:
            return None
        while node is not None and node.val != val:
            if node.val > val:
                node = node.left
            else:
                node = node.right
        return node 

    def contains(self, val)->bool:
        """
        time: O(n), omega(logn)
        space: O(n)
        """
        if self.find(val) is not None:
            return True
        return False
    
    def erase(self, val):
        """
        time: O(H) gdzie H to wysokość drzewa
        space: O(H) na stos wywołań rekurencyjnych
        """
        self.node = self._erase_recursive(self.node, val)

    def _erase_recursive(self, node, val):
        if node is None:
            return None
        
        if val < node.val:
            node.left = self._erase_recursive(node.left, val)
        elif val > node.val:
            node.right = self._erase_recursive(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            next_min = self._min(node.right)

            assert(next_min is not None)
            
            node.val = next_min.val
            
            node.right = self._erase_recursive(node.right, next_min.val)
            
        return node

    def is_balanced(self)->bool:
        """
        time: O(n) - liczba węzłów
        space: O(h) - wysokość
        """
        def _check_height(node:Node|None)->int:
            if node is None:
                return 0
            left_node = _check_height(node.left)
            if left_node == -1:
                return -1
            right_node = _check_height(node.right)
            if right_node == -1:
                return -1

            if abs(left_node - right_node) > 1:
                return -1
            return max(left_node, right_node)
        return _check_height(self.node)!=-1
            
    """
    DFS: 
        time: O(n)
        space: O(n), omega(logn)
    """

    def preorder(self):
        node = self.node
        yield from preorder(node)


    def inorder(self):
        node = self.node
        yield from inorder(node)


    def postorder(self):
        node = self.node
        yield from postorder(node)


if __name__ == "__main__":
    bst = BST()
    bst.add(5)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    print(bst.contains(-1))
    print(bst.contains(2))
    print(bst.max())
    print(bst.min())
    print("Preorder:")
    for i in bst.preorder():
        print(i)
    print("Inorder:")
    for i in bst.inorder():
        print(i)
    print("Postorder:")
    for i in bst.postorder():
        print(i)

