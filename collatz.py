__author__ = 'cwang'

def f(a):
    if a % 2 == 0:
        return a/2
    else:
        return 3*a + 1

def count(b,k):
    steps = [ -1 for i in range( b + 1) ]
    steps[1] = 0
    
    for i in range(2,b):
        if steps[i] == -1:
            iterate_f_i = []
            l = i
            for j in range( 2 * k):
                iterate_f_i.append(l)
                l = f(l)
                if  l < b and steps[l] != -1:
                    break
            len_iter = len(iterate_f_i)
            if l < b and steps[l] != -1:
                for j in range(len_iter):
                    if iterate_f_i[len_iter - 1 - j] < b:
                        steps[iterate_f_i[len_iter - 1 - j]] = steps[l] + j + 1
            print steps
            return steps
                             
print count(100,10)


"""
def collatz(B, k):
    steps = [None] * (B + 1)
    steps[1] = 0
    for i in range(B):
        num = i + 1
        path = [num]
        if steps[num] is not None: continue
        for step in range(2 * k):
            if num % 2 == 0:
                num //= 2
            else:
                num = num * 3 + 1
            path.append(num)
            if num <= B and steps[num] is not None:
                break

        sz = len(path)
        if num > B or steps[num] is None:
            for i in range(k):
                if path[i] <= B:
                    steps[path[i]] = -1
        else:
            number_of_steps = steps[path[-1]]
            for i in reversed(range(sz)):
                if path[i] <= B:
                    steps[path[i]] = number_of_steps
                if number_of_steps < k and number_of_steps >= 0:
                    number_of_steps += 1
                elif number_of_steps == k:
                    number_of_steps = -1
    # pairs = 0
    # for i, num in enumerate(steps):
    #     if i < B and steps[i] == steps[i + 1]:
    #         pairs += 1
    #     print(i, num)

    count = B - steps.count(-1)
    print(steps.index(max(steps[1:])), max(steps[1:]))
    # return count

if __name__ == '__main__':
    B = 100000000
    k = 1000
    # print(collatz(B, k))
    collatz(B, k)
"""
