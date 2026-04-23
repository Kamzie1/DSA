def partition_horne(array:list, l:int, r:int) ->int:
    """
    Partiton algorithm for quick sort. (see lomuto)
    Time complexity: O(n)
    Memory complexity: O(1)

    array: array
    l: left
    r: right
    """
    m = array[(l+r)//2]
    i = l -1
    j = r+1
    while True:
        i+=1
        j-=1
        while(array[i]<m):
            i+=1
        while(array[j]>m):
            j-=1
        if i>=j:
            return j
        array[i], array[j] = array[j], array[i]

def partition_lomuto(array:list, l:int, r:int)->int:
    """
    Partiton algorithm for quick sort. (see horne)
    Lomuto partition guaranties that m is in the correct order after partition(meaning it is sorted)
    Time complexity: O(n)
    Memory complexity: O(1)

    array: array
    l: left
    r: right
    """
    i = l-1
    j = l-1
    m = array[r]
    while j+1<=r:
        j+=1
        if array[j] <= m:
            i+=1
            array[i], array[j] = array[j], array[i]
    return i

def quick_sort_rek(array:list, l:int, r:int):
    """
        This is a helper to quick sort algorithm.
        It is used so that when we sort we don't need to type l and r.

        l: left side
        r: right side
    """
    if(l>=r):
        return
#    m = partition_horne(array:list, l:int, r:int) 
#    quick_sort_rek(array, l, m)
    m = partition_lomuto(array, l, r)
    quick_sort_rek(array, l, m-1) # This is because in lomuto m is already ordered correctly
    quick_sort_rek(array, m+1, r)

def quick_sort(array:list):
    """
        quick sort algorithm.
        The algorithm splits the array into two smaller arrays, one with bigger and one with smaller numbers all the way down.
        Time complexity: omega(nlogn), however O(n^2) when we don't divide equally (m is the highest/lowest number)
        Memory complexity: O(1)
        Type:
          * in place
          * stable 
    """
    quick_sort_rek(array, 0, len(array)-1)


array1 = [1,5,4,6,7,3,2]
array2 = [1,5,4,6,7,3,2]
array3 = [1,1,3,2,5,5,3,4,7,77,1,2,33]

#partition_horne(array1, 0, len(array1) -1)
#partition_lomuto(array2, 0, len(array2) -1)
#print(array1)
#print(array2)

quick_sort(array1)
print(array1)
quick_sort(array3)
print(array3)

