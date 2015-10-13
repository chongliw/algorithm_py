__author__ = 'cwang'

import math

def my_isPalindrome(x, deg):
    if deg <= 0: return True
    hi10 = 10 ** deg
    hi = x // hi10
    low = x % 10
    if hi != low: return False
    else: return my_isPalindrome((x % hi10) // 10, deg - 2)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        else:
            if not x: return True
            deg = int(math.log(x, 10))
            return my_isPalindrome(x, deg)

if __name__ == '__main__':
    sol = Solution()
    result = sol.isPalindrome(101)
    print(result)
