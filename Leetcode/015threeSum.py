__author__ = 'cwang'


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sz = len(nums)
        idx = [i for i in range(sz)]
        idx.sort(key=lambda x: nums[x])
        sortednums = [nums[i] for i in idx]
        target = 0
        sumTriples = set()
        for idx_a in range(sz - 2):
            idx_b = idx_a + 1
            idx_c = sz - 1
            while idx_b < idx_c:
                if sortednums[idx_b] + sortednums[idx_c] == target - sortednums[idx_a]:
                    sumTriples.add(tuple([sortednums[idx_a], sortednums[idx_b], sortednums[idx_c]]))
                    idx_b += 1
                elif sortednums[idx_b] + sortednums[idx_c] < target - sortednums[idx_a]:
                    idx_b += 1
                else:
                    idx_c -= 1

        return([list(x) for x in sumTriples])


if __name__ == '__main__':
    nums = [0,-4,-1,-4,-2,-3,2]
    sol = Solution()
    result = sol.threeSum(nums)
    print(result)
