__author__ = 'cwang'

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        strs = [''] * numRows
        index, dir = 0, 1
        if numRows == 1: return s
        for ch in s:
            strs[index] += ch
            index += dir
            if index == 0 or index == numRows - 1:
                dir = -dir
        result = ''
        for st in strs: result += st
        return result

if __name__ == '__main__':
    sol = Solution()
    result = sol.convert('PAY', 1)
    print(result)
