from node import Node

"""
DFS: 
    time: O(n)
    space: O(n), omega(logn)
"""
def postorder(node:Node | None):
    if node is not None:
        if node.left is not None:
            yield from postorder(node.left)
        if node.right is not None:
            yield from postorder(node.right)
        yield node.val

def inorder(node: Node | None):
    if node is not None:
        if node.left is not None:
            yield from inorder(node.left)
        yield node.val
        if node.right is not None:
            yield from inorder(node.right)

def preorder(node:Node|None):
    if node is not None:
        yield node.val
        if node.left is not None:
            yield from preorder(node.left)
        if node.right is not None:
            yield from preorder(node.right)
