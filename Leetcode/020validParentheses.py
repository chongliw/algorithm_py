__author__ = 'cwang'

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {']': '[', '}': '{', ')': '('}
        stack = []
        leftP = ['(', '[', '{']
        for ch in s:
            if ch in leftP:
                stack.append(ch)
                continue
            else:
                chReverse = mapping[ch]
            if not stack or chReverse != stack.pop():
                return False
        if stack: return False
        else: return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('{(})'))
