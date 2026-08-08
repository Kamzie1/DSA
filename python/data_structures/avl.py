from bst import BST
from node import Node

class AvlNode(Node):
    def __init__(self, val, height = 0) -> None:
        super().__init__(val)
        self.height = height

class AVL(BST):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def height(node:AvlNode):
        return node.height if node else -1

    @staticmethod
    def update_height(node):
        node.height = 1 + max(AVL.height(node.left), AVL.height(node.right))

    @staticmethod
    def balance_factor(node):
        return AVL.height(node.left) - AVL.height(node.right) if node else 0

    def add(self, val):
        """
        time: O(log n)
        space: O(log n) ze względu na stos rekurencji
        """
        self.node = self._add_recursive(self.node, val)

    def _add_recursive(self, node, val):
        if node is None:
            return AvlNode(val)
            
        if val < node.val:
            node.left = self._add_recursive(node.left, val)
        elif val > node.val:
            node.right = self._add_recursive(node.right, val)
        else:
            return node

        AVL.update_height(node)

        return AVL.balance(node)

    @staticmethod
    def left_rotate(node):
        b = node.right
        node.right = b.left
        b.left = node
        AVL.update_height(node)
        AVL.update_height(b)
        return b

    @staticmethod
    def right_rotate(node):
        b = node.left
        node.left = b.right
        b.right = node
        AVL.update_height(node)
        AVL.update_height(b)
        return b

    @staticmethod
    def balance(node):
        if AVL.balance_factor(node) < -1:
            if AVL.balance_factor(node.right) > 0:
                node.right = AVL.right_rotate(node.right)
            node = AVL.left_rotate(node)
        elif AVL.balance_factor(node) > 1:
            if AVL.balance_factor(node.left) < 0:
                node.left = AVL.left_rotate(node.left)
            node = AVL.right_rotate(node)
        return node



if __name__ == "__main__":
    avl = AVL()
    avl.add(5)
    avl.add(2)
    avl.add(6)
    avl.add(1)
    print(avl.contains(-1))
    print(avl.contains(2))
    print(avl.max())
    print(avl.min())
    print("Preorder:")
    for i in avl.preorder():
        print(i)
    print("Inorder:")
    for i in avl.inorder():
        print(i)
    print("Postorder:")
    for i in avl.postorder():
        print(i)



