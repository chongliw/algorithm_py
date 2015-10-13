__author__ = 'cwang'

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sz = len(height)
        if sz < 2: return 0
        low, high = 0, sz - 1
        area = 0
        while low < high:
            area = max(area, (high - low) * min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return area

if __name__ == '__main__':
    sol = Solution()
    height = [1, 2, 4, 3]
    maxA = sol.maxArea(height)
    print(maxA)