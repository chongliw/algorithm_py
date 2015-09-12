__author__ = 'cwang'

# Collatz conjecture: x -> x * 3 + 1 or x -> x / 2 if x is odd or even.
# Given B and k, determine how many numbers between 1 and B can go to 1 within k steps

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
                    # cannot reach in 2k steps, hence first k states are impossible
                    # to reach in k steps
        else:
            number_of_steps = steps[path[-1]]
            for i in reversed(range(sz)):
                if path[i] <= B:
                    steps[path[i]] = number_of_steps
                if number_of_steps < k and number_of_steps >= 0:
                    number_of_steps += 1
                elif number_of_steps == k:
                    number_of_steps = -1 # indicating impossibility within k steps
    # pairs = 0
    # for i, num in enumerate(steps):
    #     if i < B and steps[i] == steps[i + 1]:
    #         pairs += 1
    #     print(i, num)

    count = B - steps.count(-1)
    # print(steps.index(max(steps[1:])), max(steps[1:]))
    return count

if __name__ == '__main__':
    B = 100000000
    k = 1000
    # print(collatz(B, k))
    print(collatz(B, k))

