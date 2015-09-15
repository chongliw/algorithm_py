__author__ = 'cwang'
def STEPS(x):
    if (x == 1):
        step = 0
    else:
        if not x % 2:
            step = STEPS(x / 2) + 1
        else:
            step = STEPS(3 * x + 1) + 1
    return step

def Collartz():
    b = 10
    k = 10
    for i in range(1, b):
        print(STEPS(i))

Collartz()