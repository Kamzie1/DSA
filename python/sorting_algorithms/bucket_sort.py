import math

def normalize(array:list):
    """ 
        normalizes values of array(array must have values greater than or equal 0)
    """
    maks = max(array)
    for i in range(len(array)):
        array[i] = array[i] / maks

def bucket_sort(array:list)->list:
    """
        Bucket sort algorithm.
        Array needs to be normalized to values [0,1]
        Time complexity: omega(n), however O(n^2) if values are not evenly distributed
        Memory complexity: O(n)
        type:
          * not in place
          * stable 
    """
    buckets = [list() for _ in range(len(array)+1)]
    for i in array:
        buckets[math.floor(i*len(array))].append(i)

    for l in buckets:
        l.sort()

    sorted = [0 for _ in range(len(array))]
    i = 0
    for bucket in buckets:
        for num in bucket:
            sorted[i] = num
            i+=1

    return sorted

if __name__ == "__main__":
    array = [0.1, 0.3, 0.2, 0.01, 0.5, 0.25, 0.6, 1, 0]
    print(bucket_sort(array))
