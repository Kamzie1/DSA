def counting_sort(array:list):
    """
    Counting sort algorithm.
    Time complexity: O(n)
    Memory complexity: O(k+n), where k is the biggest number in array
    type:
      * not in place
      * stable (however if we start filling sorted with nums iterating from the start of array then it will not be stable)
    """

    N = len(array)
    maks = max(array)

    count = [0 for _ in range(maks+1)]
    sorted = [ 0 for _ in range(N)]
    
    for i in array:
        count[i] += 1

    sum = 0
    for i in range(maks + 1):
        sum += count[i]
        count[i] = sum 

    for num in array[::-1]:
        sorted[count[num]-1] = num 
        count[num] -=1

    return sorted


if __name__ == "__main__":
    array = [1,1,3,2,5,5,3,4,7,77,1,2,33]
    print(counting_sort(array))
