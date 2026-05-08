class Stack:
    """
        LIFO Data structure.
        Last in First Out.
        This is simple implementation, i am gonna do a better job in c++.
    """
    def __init__(self) -> None:
        self.stack:list = list()
        self.stack_top:int = 0

    def push(self, element) -> None:
        """
            amortyzowane: O(1)
        """
        self.stack.append(element)
        self.stack_top+=1

    def pop(self):
        """
            O(1)
        """
        self.stack_top-=1
        return  self.stack.pop()
    
    def top(self):
        """
            O(1)
        """
        if self.stack_top == 0:
            return None
        return self.stack[self.stack_top-1]

    def __len__(self):
        """
            O(1)
        """
        return self.stack_top

    def __str__(self):
        """
            O(n)
        """
        return str(self.stack)

    def iter(self):
        """
            Generator
            Iteruje po stosie np. for i in stack.iter():
            O(n)
        """
        pomo = self.stack_top-1
        while pomo >= 0:
            yield self.stack[pomo]
            pomo-=1

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    print(stack.top())
    stack.push(2)
    print(stack)
    print(stack.pop())
    print(stack)
    for i in range(10):
        stack.push(i)

    print(stack)
    print(len(stack))
    for i in stack.iter():
        print(i)

