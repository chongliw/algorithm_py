__author__ = 'cwang'

def generate(result, left_remain, right_remain, curr):
    if left_remain:
        generate(result, left_remain - 1, right_remain + 1, curr + '(')
    if right_remain:
        generate(result, left_remain, right_remain - 1, curr + ')')
    if not left_remain and not right_remain:
        result.append(curr)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        generate(result, n, 0, '')
        return result

if __name__ == '__main__':
    sol = Solution()
    result = sol.generateParenthesis(3)
    print(result)