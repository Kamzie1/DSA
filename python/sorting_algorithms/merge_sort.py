def merge(array:list, l:int, q:int, r:int):
    """
        Merge procedure.
        This procedure is used by merge sort algorithm. The purpose of this function is to merge two ranges in a correct order.

        array: array
        l: left side of the range
        q: the break point
        r: right side

        Time complexity: O(n), since we go from p to r regardless of the input
        Memory comlexity: O(n), since we allocate two arrays list1 and list2
    """
    list1 = [x for x in array[l:q+1]]
    list2 = [x for x in array[q+1:r+1]]
    k = l
    i = 0
    j = 0
    while k <= r:
        if i >= len(list1):
            array[k] = list2[j]
            j+=1
        elif j>= len(list2):
            array[k] = list1[i]
            i+=1 
        else:
            if  list1[i] <= list2[j]:
                array[k] = list1[i]
                i+=1
            elif list2[j] <= list1[i]:
                array[k] = list2[j]
                j+=1
        k+=1

def merge_rec_sort(array:list, l:int, r:int):
    """
        This is a helper to Merge sort algorithm.
        It is used so that when we sort we don't need to type l and r.

        l: left side
        r: right side
    """
    if l>=r:
        return
    q = ( l + r )//2
    merge_rec_sort(array, l, q)
    merge_rec_sort(array, q+1, r)
    merge(array, l, q, r)

def merge_sort(array:list):
    """
        Merge sort algorithm.
        This algorithm splits recursivly given array and then merges it in a correct order(see: merge).
        Time complexity: O(nlogn), since we merge with O(n) and we use recursion.
        Memory complexity: O(n), merge helper uses O(n)
        Type:
          * not in place
          * stable  

        Detailed description of time complexity:
        When we deal with divide and conquer algorithms we use special formula:
        T(n) = {O(1), n<=c, aT(n/b) + C(n) + D(n), n>c} (c is a recursion break, C is conquer complexity, D is divide complexity, a is number of new problems and n/b is a new size of a problems.
        Then:
            D(n) = O(1)
            a = 2
            b = 2
            C(n) = O(n) (merge)
            so we solve a recursive equation and get O(nlogn), which is pretty intuitive since we divide our problem by two every time.
    """
    merge_rec_sort(array, 0, len(array)-1)

array = [1,1,3,2,5,5,3,4,7,77,1,2,33]
merge_sort(array)
print(array)
