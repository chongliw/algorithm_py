__author__ = 'cwang'


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = 0
        initialized = False
        nums.sort()
        sz = len(nums)

        for idx1 in range(sz):
            idx2 = idx1 + 1
            idx3 = sz - 1
            while idx2 < idx3:
                new_diff = nums[idx1] + nums[idx2] + nums[idx3] - target
                if abs(new_diff) < abs(diff) or not initialized:
                    initialized = True
                    diff = new_diff
                if new_diff < 0:
                    idx2 += 1
                else:
                    idx3 -= 1

        return target + diff


if __name__ == '__main__':
    S = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    result = sol.threeSumClosest(S, target)
    print(result)
