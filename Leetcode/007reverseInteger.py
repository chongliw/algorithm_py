__author__ = 'cwang'

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isPos = True
        if x < 0:
            isPos = False
            strCandidate = str(-x)
        else:
            strCandidate = str(x)

        abs = ''
        for ch in reversed(strCandidate):
            abs += ch
        result = int(abs)
        if result > 2147483647: return 0
        return result if isPos else -result


if __name__ == '__main__':
    sol = Solution()
    result = sol.reverse(-1200)
    print(result)

