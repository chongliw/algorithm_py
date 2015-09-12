__author__ = 'cwang'

def trade(prices):
    sz = len(prices)
    transaction = [0] * sz
    curr = prices[-1]
    currindex = sz - 1
    profit = 0
    for i in reversed(range(sz)):
        if prices[i] < curr:
            transaction[i] = 1
            transaction[currindex] -= 1
            profit += curr - prices[i]
        else:
            curr = prices[i]
            currindex = i
    print("transaction", transaction)
    print("profit %d" % profit)

if __name__ == '__main__':
    prices = [13, 2, 1, 12]
    trade(prices)