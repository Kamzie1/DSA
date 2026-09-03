class Heap:
    def __init__(self, relation, arr:list|None = None) -> None:
        self.relation = relation
        if arr is None:
            self.heap = list()
        else:
            self.build_heap(arr)
        self.size = len(self.heap)


    @staticmethod
    def left(index:int)->int:
        return index * 2 + 1

    @staticmethod
    def right(index:int)->int:
        return index * 2 + 2

    @staticmethod
    def parent(index:int)->int:
        return index // 2

    def heapify(self, i):
        Heap._heapify(self.heap, i, self.relation, self.size)

    @staticmethod
    def _heapify(heap:list, i:int, relation, n=None):
        """
        time: O(logn), omega(1)
        space: O(1)
        """
        l = Heap.left(i)
        r = Heap.right(i)
        if n is None:
            n = len(heap)
        largest = i
        if l < n and relation(heap[l], heap[i]):
            largest = l
        if  r < n and relation(heap[r], heap[largest]):
            largest = r
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            Heap._heapify(heap, largest, relation, n)

    @staticmethod
    def _build_heap(heap:list, relation, size=None)->list:
        """
        time: O(n)
        space: O(1)
        """
        if size is None:
            size = len(heap)
        for i in range(size // 2 - 1, -1, -1):
            Heap._heapify(heap, i, relation, size)
        return heap

    def build_heap(self, arr=None):
        if arr is None:
            arr = self.heap
        self.heap =  Heap._build_heap(arr, self.relation, len(arr))
        
    def empty(self):
        return len(self.heap) == 0

    def top(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def pop(self):
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(0)

    def _bubble_up(self, i):
        p = Heap.parent(i)
        while i > 0 and self.relation(self.heap[i], self.heap[p]):
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            p = Heap.parent(i)

    def push(self, val):
        if self.size == len(self.heap):
            self.heap.append(val)
        else:
            self.heap[self.size] = val
        self.size += 1

        self._bubble_up(self.size-1)

class MaxHeap(Heap):
    def __init__(self, arr:list|None = None) -> None:
        super().__init__(lambda x,y: x > y, arr)

class MinHeap(Heap):
    def __init__(self, arr:list|None = None) -> None:
        super().__init__(lambda x,y: x < y, arr)
