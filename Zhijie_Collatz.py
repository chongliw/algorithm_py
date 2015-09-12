__author__ = 'cwang'


def f(a):
    if a % 2 == 0:
        return a // 2
    else:
        return 3 * a + 1

def count(b, k):
    steps = [-1] * (b + 1)
    steps[1] = 0

    for i in range(2, b):
        if steps[i] == -1:
            iterate_f_i = []
            l = i
            for j in range(2 * k):
                iterate_f_i.append(l)
                l = f(l)
                if l < b and steps[l] != -1:
                    break
            len_iter = len(iterate_f_i)
            if l < b and steps[l] != -1:
                for j in range(len_iter):
                    if iterate_f_i[len_iter - 1 - j] < b:
                        steps[iterate_f_i[len_iter - 1 - j]] = steps[l] + j + 1
    return steps


print(count(100, 10))
