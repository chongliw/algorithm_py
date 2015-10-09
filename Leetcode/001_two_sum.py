__author__ = 'cwang'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sz = len(nums)
        indices = []
        sorted_index = sorted(range(sz), key=lambda i:nums[i])
        sorted_nums = [nums[i] for i in sorted_index]
        targetminus = [target - num for num in reversed(sorted_nums) ]
        p1 = 0
        p2 = 0
        while p1 < sz and p2 < sz:
            if sorted_nums[p1] == targetminus[p2]:
                if p1 != sz - 1 - p2:
                    i1 = sorted_index[p1]
                    i2 = sorted_index[sz - 1 - p2]
                    if i1 < i2:
                        indices += [i1 + 1, i2 + 1]
                    else:
                        indices += [i2 + 1, i1 + 1]
                    return indices
            elif sorted_nums[p1] < targetminus[p2]:
                p1 += 1
            else:
                p2 += 1

        return indices

if __name__ == '__main__':
    nums = [2, 7, 15, 11]
    target = 23
    test = Solution()
    ls = test.twoSum(nums, target)
    print(ls)
