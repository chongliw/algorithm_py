__author__ = 'cwang'

def findRank(n1, s1, e1, n2, rk):
    rk1 = (e1 - s1) // 2
    if rk1:
        rk2 = rk - rk1
        if rk2 < 1: return findRank(n1, s1, s1 + rk1, n2, rk)
        elif rk2 > len(n2): return findRank(n1, s1 + rk1, e1, n2, rk2)
        else:
            return findRank(n1, s1 + rk1, e1, n2, rk2) if n1[s1 + rk1 - 1] < n2[rk2 - 1] \
            else   findRank(n1, s1, s1 + rk1, n2, rk)
    else:
        if e1 == s1: return n2[rk - 1]
        if rk == 1: return min(n1[s1], n2[0])
        if rk == 1 + len(n2): return max(n1[e1 - 1], n2[-1])
        return max(n1[s1], n2[rk - 2]) if n1[s1] < n2[rk - 1] else n2[rk - 1]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sz1, sz2 = len(nums1), len(nums2)
        if sz1 > sz2:
            nums1, nums2 = nums2, nums1
            sz1, sz2 = sz2, sz1
        sz = sz1 + sz2
        rk = sz // 2
        return float(findRank(nums1, 0, sz1, nums2, rk + 1)) if sz % 2 \
        else   float(findRank(nums1, 0, sz1, nums2, rk) +
                     findRank(nums1, 0, sz1, nums2, rk + 1)) / 2

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1]
    nums2 = [2, 3]
    print(sol.findMedianSortedArrays(nums1, nums2))