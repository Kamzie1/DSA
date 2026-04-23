from typing import Tuple
def max_min(array:list)->Tuple[int, int] | None:
    """
        An optimal algorithm for finding maximum and minimum at the same time.
        Time complexity: T(ceil(n/2*3))
        Memory complexity: O(1)
    """
    operations = 0
    N = len(array)
    if N == 0:
        return None
    min = array[0]
    maks = array[0]
    l_maks = 0
    l_min = 0
    for i in range(0,N-N%2,2):
        operations+=3
        if array[i] > array[i+1]:
            l_maks = array[i]
            l_min = array[i+1]
        else:
            l_maks = array[i+1]
            l_min = array[i]
        if l_maks > maks:
            maks = l_maks
        if l_min < min:
            min = l_min
    l_maks = array[N-1]
    l_min = array[N-1]
    operations+=2
    if l_maks > maks:
        maks = l_maks
    if l_min < min:
        min = l_min
    print(operations)
    return (maks, min)

def max_min_noob(array:list)->Tuple[int, int] | None:
    operations = 0
    N = len(array)
    if N == 0:
        return None
    min = array[0]
    maks = array[0]
    for i in range(N):
        operations+=2
        if array[i] > maks:
            maks = array[i]
        if array[i] < min:
            min = array[i]
    print(operations)
    return (maks, min)

if __name__ == "__main__":
    array = [1,1,3,2,5,5,3,4,7,77,1,2,33]
    print(max_min(array))
    print(max_min_noob(array))
