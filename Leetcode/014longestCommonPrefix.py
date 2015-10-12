__author__ = 'cwang'

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sz = len(strs)
        if not sz: return ''
        digit = 0
        while True:
            intialized = False
            ch = ''
            for i in range(sz):
                if digit >= len(strs[i]) or (intialized and strs[i][digit] != ch):
                    return strs[i][:digit]
                if not intialized:
                    ch = strs[i][digit]
                    intialized = True
            digit += 1

if __name__ == '__main__':
    sol = Solution()
    strs = ['a', 'ab']
    print(sol.longestCommonPrefix(strs))