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
        hsz = max(sz1 // 2 - 2, 0)   # half size of list 1 - 2
        arr = ls1[s1 + hsz: e1 - hsz] + ls2[s2: e2]
        arr.sort()
        return med(arr, 0, len(arr))
    med1 = med(ls1, s1, e1)
    med2 = med(ls2, s2, e2)
    skipsz = (e2 - s2 - 1) // 2
    if med1 < med2:
        return find_median(ls1, ls2, s1 + skipsz, e1, s2, e2 - skipsz)
    else:
        return find_median(ls1, ls2, s1, e1 - skipsz, s2 + skipsz, e2)

def find_order(ls1, ls2, s1, e1, s2, e2, rk):
    rank2 = (e2 - s2) // 2
    if rank2 == 0:
        if e2 == s2:
            return ls1[rk - 1]
        num2 = ls2[s2]
        if rk == 1: return min(ls1[s1], num2)
        if rk == 1 + e1 - s1: return max(ls1[e1 - 1], num2)
        if ls1[s1 + rk - 1] < ls2[s2]:
            return ls1[s1 + rk - 1]
        else:
            return max(ls1[s1 + rk - 2], ls2[s2])
    if rk <= rank2:
        return find_order(ls1, ls2, s1, e1, s2, s2 + rank2, rk)
    elif rk > rank2 + (e1 - s1):
        return find_order(ls1, ls2, s1, e1, s2 + rank2, e2, rk - rank2)
    else:
        rank1 = rk - rank2
        if ls1[s1 + rank1 - 1] < ls2[s2 + rank2 - 1]:
            return find_order(ls1, ls2, s1 + rank1, e1, s2, s2 + rank2, rank2)
        else:
            return find_order(ls1, ls2, s1, s1 + rank1, s2 + rank2, e2, rank1)

if __name__ == '__main__':
    ls1 = []
    ls2 = [2, 3]
    start = time()
    if len(ls1) < len(ls2):
        swap = ls1
        ls1 = ls2
        ls2 = swap
    result = find_median(ls1, ls2, 0, len(ls1), 0, len(ls2))
    print(result)
    k = 1
    krank = find_order(ls1, ls2, 0, len(ls1), 0, len(ls2), k)
    print(krank)
    print('running time=', time() - start)