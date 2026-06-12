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

    def min(self):
        node = self.node
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.val

    def max(self):
        node = self.node
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.val

    def contains(self, val)->bool:
        """
        time: O(n), omega(logn)
        space: O(n)
        """
        node = self.node
        if node is None:
            return False
        while node is not None and node.val != val:
            if node.val > val:
                node = node.left
            else:
                node = node.right
        return node is not None

    def erase(self, val):
        """
        time: O(h) h:height, omega(1)
        space: O(h), recursion
        """
        pass


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

