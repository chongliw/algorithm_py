__author__ = 'cwang'

INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        sign = {'+': 1, '-': -1}
        isSigned = False
        outOfEmptySpace = False
        num = 0
        sig = 1
        for st in str:
            if st == ' ' and not outOfEmptySpace: continue
            if st in sign and not isSigned:
                isSigned = True
                sig = sign[st]
                outOfEmptySpace = True
                continue
            outOfEmptySpace = True
            if not st in dic:
                return num * sig
            num = num * 10 + dic[st]
            if num > INT_MAX:
                return INT_MAX if sig == 1 else INT_MIN
        return num * sig

if __name__ == '__main__':
    sol = Solution()
    result = sol.myAtoi('  -88j')
    print(result)
