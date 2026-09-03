"""
Czasowa:
    O(n^2), bo ciąg n, n-1, ...
    omega(n), już posortowane (tylko raz przejdzie przez pętla, brak hopki)
    theta brak
Pamięciowa:
    O(1), omega(1), theta(1) - stałe
Typ:
    in-place
    stabline
"""

def bubble_sort(array):
    koniec = len(array)-1
    while True:
        hopka = 0

        for i in range(koniec):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                hopka = i

        koniec = hopka

        if not hopka:
            break


if __name__ == "__main__":
    array = [1,1,3,2,5,5,3,4,7,77,1,2,33]
    bubble_sort(array)
    print(array)

