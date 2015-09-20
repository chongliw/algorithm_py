__author__ = 'Zhijie Huang'
import random
# this function returns the max successive sum in a list

def max_successive_sum(a):
    max_sum = 0
    toend = 0
    for i in range(len(a)):
        if toend + a[i] > max_sum:
            max_sum = toend + a[i]
            toend = max_sum
        else:
            toend = max(toend + a[i], 0)
    return max_sum

a = []
for i in range(10):
    a.append(random.randint(-10, 5))
print(a)
print(max_successive_sum(a))