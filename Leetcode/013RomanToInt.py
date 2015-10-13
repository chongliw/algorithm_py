__author__ = 'cwang'


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sz = len(s)
        sum = 0
        for i in range(sz):
            ch = s[i]
            if i < sz - 1 and (dic[ch] * 10 == dic[s[i + 1]] or dic[ch] * 5 == dic[s[i + 1]]):
                sum -= dic[ch]
            else:
                sum += dic[ch]
        return sum


if __name__ == '__main__':
    sol = Solution()
    result = sol.romanToInt("IX")
    print(result)
