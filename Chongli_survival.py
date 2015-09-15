__author__ = 'cwang'
from random import randint

def isSurvivial(n):
    if n == 1:
        return True
    elif n == 0:
        return False
    else:
        ls = []
        num = 0
        for i in range(n):
            l = randint(0, n - 2)
            if l >= i: l += 1
            if not l in ls:
                ls.append(l)
                num += 1
        return isSurvivial(n - num)


if __name__ == '__main__':
    n = 100
    iter = 10000
    count = 0
    for i in range(iter):
        if isSurvivial(n):
            count += 1
    print(float(count) / iter)