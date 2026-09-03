from enum import Enum
from bst import BST

class RedBlackTree(BST):
    class Color(Enum):
        RED = 0
        BLACK = 1

    class Node:
        def __init__(self, val, color) -> None:
            self.left = None  
            self.right = None  
            self.val = val  
            self.color = color

    def __init__(self) -> None:
        self.root = None

    
