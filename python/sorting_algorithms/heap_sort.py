from data_structures.heap import Heap

def heap_sort(arr:list, relation = lambda x,y: x<y ):
    n = len(arr)
    arr = Heap._build_heap(arr, relation)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        Heap._heapify(arr, 0, relation, i - 2)

