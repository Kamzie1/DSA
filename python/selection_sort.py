def selection_sort(tab: list)->None:
    """
    time complexity: O(n^2)
    memory complexity: O(1)
    type:
      * in place
      * unstable `(4, 2_1, 2_2, 6, 1, 7) -> (1, 2_2, 2_1, 4, 6, 7)`
    """
    N = len(tab)
    for i in range(N):
        for j in range(i, N):
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j], tab[i]


array = [1,1,3,2,5,5,3,4,7,77,1,2,33]
selection_sort(array)
print(array)
