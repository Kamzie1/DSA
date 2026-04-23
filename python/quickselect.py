from quick_sort import partition_horne, partition_lomuto

def quickselect_rek(array:list, l:int, r:int, f: int) -> int:
    """
        A quick selection algorithm based on partitions used in quick sort
        Time complexity: on average O(n), however worst case(or actual O) is O(n^2)
    """
    if l > r:
        return -1
    m = partition_lomuto(array, l, r)
    if array[m] == f:
        return m
    elif array[m] < f:
        return quickselect_rek(array, m+1, r, f)
    else:
        return quickselect_rek(array, l, m-1, f)


def quickselect(array:list, f:int)->int:
    return quickselect_rek(array, 0, len(array)-1, f)

if __name__ == "__main__":
    array = [1,1,3,2,5,5,3,4,7,77,1,2,33]
    print(quickselect(array, 7))
    print(quickselect(array, 100))

