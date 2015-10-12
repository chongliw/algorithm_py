__author__ = 'cwang'

def longestLength(s, start):
    leng = min(start, len(s) - start)
    for i in range(leng):
        if s[start - i] != s[start + i]:
            return i - 1
    return leng

def get_string(s, length, st):
    news = ''
    for i in range(st - length + 1, st + length):
        if s[i] != '#': news += s[i]
    return news

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        newS = "#"
        for ch in s:
            newS += ch + '#'
        sz = len(s)
        maxlength, maxS = 0, ''
        for i in range(sz):
            if sz - i < maxlength: return maxS
            dirs = [-1, +1]
            for dir in dirs:
                length = longestLength(newS, sz + dir * i)
                if length > maxlength:
                    maxlength = length
                    maxS = get_string(newS, length, sz + dir * i)
        return maxS

if __name__ == '__main__':
    sol = Solution()
    s = "abb"
    palind = sol.longestPalindrome(s)
    print(len(palind), palind)