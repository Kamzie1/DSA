def radix_sort(array:list):
    """
        Radix sort algorithm.
        Needs the same length elements and the least important is at the end.
        Time complexity: O(n) + O of whatever sorting algorithm we are using(needs to be stable)
        Memory complexity: O(1)
        type:
          * in place
          * stable
    """
    if len(array) == 0:
        return
    length = len(array[0])
    for i in range(length):
        array.sort(key = lambda x: x[length - i - 1])


array = ["ala", "mak", "sia", "dla", "kot", "plo", "wso", "aso"]
radix_sort(array)
print(array)
