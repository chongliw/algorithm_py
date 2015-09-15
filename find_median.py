# Given two sorted array, find their combined medium.
# run time O(log(min(n, m))

__author__ = 'cwang'
from time import time
def med(arr, i, j):
    m, r = divmod(j - i, 2)
    if r:
        return arr[i + m]
    else:
        return sum(arr[i + m - 1: i + m + 1]) / 2

def find_median(ls1, ls2, s1, e1, s2, e2):
    sz1 = e1 - s1
    sz2 = e2 - s2
    if sz2 <= 2:
        hsz = max(sz1 // 2 - 1, 0) # half size of list 1
        arr = ls1[s1 + hsz: e1 - hsz] + ls2[s2: e2]
        arr.sort()
        return med(arr, 0, len(arr))
    med1 = med(ls1, s1, e1)
    med2 = med(ls2, s2, e2)
    skipsz = (e2 - s2) // 2
    if med1 < med2:
        return find_median(ls1, ls2, s1 + skipsz, e1, s2, e2 - skipsz)
    else:
        return find_median(ls1, ls2, s1, e1 - skipsz, s2 + skipsz, e2)

if __name__ == '__main__':
    ls1 = list(range(1, 100000000, 2))
    ls2 = list(range(2, 100000000, 2))
    start = time()
    if len(ls1) < len(ls2):
        swap = ls1
        ls1 = ls2
        ls2 = swap
    result = find_median(ls1, ls2, 0, len(ls1), 0, len(ls2))
    print(result)
    print('running time=', time() - start)