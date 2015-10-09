__author__ = "Zhijie Huang"


import time

def f(a):
    if a % 2 == 0:
        return a // 2
    else:
        return 3 * a + 1

def count(b, k):
    steps = [-1 for i in range(b+1)]
    steps[1] = 0

    for i in range(2, b):
        if steps[i] == -1:
            path = []
            l = i
            for j in range(k):
                path.append(l)
                l = f(l)
                if l < b+1 and steps[l] != -1:
                    break
            len_path = len(path)
            if l < b+1 and steps[l] != -1:
                for j in range(len_path):
                    if path[len_path - 1 - j] < b+1:
                        steps[path[len_path - 1 - j]] = steps[l] + j + 1
    return steps

start = time.time()
k = 200
b = 10000000
result = count(b,k)
count = 0
print(time.time() - start)
for i in result:
    if i >= 0 and i <= k:
        count += 1
print(count)
print(time.time() - start)