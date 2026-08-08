from heap import MaxHeap

class PriorityQueue:
    def __init__(self) -> None:
        self.heap = MaxHeap() 

    def top(self):
        return self.heap.top()

    def push(self, val):
        self.heap.push(val)

    def pop(self):
        self.heap.pop()


