"""
Niezmiennik pętli:
    Trochę jak indukcja. Mamy przypadek startowy, który utrzymuje poprzednik spełniony, a następnie każde przejście utrzymuje niezmiennik.

    Start:
        Tablica jedno-elementowa jest posortowana 
    Krok:
        i-1 elementów jest posortowanych. I-ty element(jedyny nieposortowany) wstawiamy na odpowiednie miejsce. Dzięki czemu otrzymujemy posortowaną tablicę.
    Koniec:
        Pętla kończy się gdy pętla zewnętrzna for dojdzie do końca tablicy, co oznacza, że n elementów z tablicy o rozmiarze n jest posortowanych.

Złożoność:
  Podliczmy liczbę wykonań głównego kosztu. Uznajmy za to przypisanie wartości do tablicy w while. Zewnętrzna pętla for wykona się n-1, pętla wewnętrzna while wykona się w najgorszym przypadku i-1 razy.
  Jest to (n-1)-elementowy ciąg arytmetyczny 1,2,3...n-1, suma wynosi zatem (n-1)*n/2.  
  
  Asymptotyczna złożoność:
    O(g(n)) - jest wtedy gdy istnieją takie stałe n0 i c, że f(n) od n0 jest stale mniejsza od cg(n)
    omega(g(n)) - jest wtedy gdy istnieją takie stałe n0 i c, że f(n) od n0 jest stale większa od cg(n)
    theta(g(n)) - jest wtedy gdy istnieją takie stałe n0 ,c1 i c2, że f(n) od n0 jest stale większa od c1g(n) i mniejsza od c2g(n)
    
    o(g(n)) - dla każdej stałej c istnieje n0 > 0, że f(n) jest mniejsza od g(n)
    małe omega(g(n)) - dla każdej stałej c istnieje n0 > 0, że f(n) jest większa od g(n)
    Notacje te są asymptotycznie nieujemne.
    
  Nasza złożoność:
    o(n^2) i małe omega(n), theta brak bo o != małe omega
  Pamięciowa:
    o(1), omega(1), theta(1) - stała liczba zmiennych i pamięci

Typ algorytmu sortowania:
    In-place : nie tworzy dodatkowej pamięci
    stabilne: ponieważ mamy gwarancję, że kolejność tych samych elementów pozostanie taka sama.
""" 

def insert_sort(array):
    if len(array) <= 1:
       return  
    for i in range(len(array)):
        j = i-1
        tmp = array[i]
        while j >= 0 and  tmp < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = tmp

if __name__ == "__main__":
    array = [1,1,3,2,5,5,3,4,7,77,1,2,33]
    insert_sort(array)
    print(array)
