__author__ = 'cwang'

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sz = len(s)
        last_index = {}
        maxlength, lastlength = 0, 0
        for i in range(sz):
            ch = s[i]
            if ch in last_index:
                length = min(lastlength + 1, i - last_index[ch])
            else:
                length = lastlength + 1
            if length > maxlength: maxlength = length
            lastlength = length
            last_index[ch] = i
        return maxlength

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abba'))