__author__ = 'cwang'

from collections import defaultdict

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sz = len(nums)
        pairSums = [[nums[i] + nums[j], j, i] for i in range(sz) for j in range(i)]
        dic = defaultdict(list)
        fourTuples = set()
        for pairSum in pairSums:
            dic[pairSum[0]].append(pairSum)
            if target - pairSum[0] in dic:
                for pairS in dic[target - pairSum[0]]:
                    indices = pairS[1:] + pairSum[1:]
                    if len(set(indices)) == 4:
                        fourTuples.add(tuple(sorted(nums[x] for x in indices)))
        return [list(x) for x in fourTuples]

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    results = sol.fourSum(nums, target)
    print(results)
