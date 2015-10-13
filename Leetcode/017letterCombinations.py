__author__ = 'cwang'

def allComb(digits, mapping, index, ls, current):
    if index == len(digits):
        ls.append(current)
        return
    for ch in mapping[digits[index]]:
        allComb(digits, mapping, index + 1, ls, current + ch)


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi',
                   '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}
        ls = []
        allComb(digits, mapping, 0, ls, '')
        return ls

if __name__ == '__main__':
    sol = Solution()
    result = sol.letterCombinations('')
    print(result)
