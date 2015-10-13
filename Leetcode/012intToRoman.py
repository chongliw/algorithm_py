__author__ = 'cwang'


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # thousand-part
        dic = {1: 'I', 5: 'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 5000: '', 10000: ''}
        digit = 1000
        result = ''
        while num:
            dig = num // digit
            dig_map = {0: '', 5: dic[digit * 5], 10: dic[digit * 10]}
            dig_map[4] = dic[digit] + dig_map[5]
            dig_map[9] = dic[digit] + dig_map[10]
            for i in range(1, 4):
                dig_map[i] = dic[digit] * i
                dig_map[5 + i] = dic[digit * 5] + dic[digit] * i
            result += dig_map[dig]
            num %= digit
            digit //= 10
        return result

if __name__ == '__main__':
    sol = Solution()
    result = sol.intToRoman(761)
    print(result)
