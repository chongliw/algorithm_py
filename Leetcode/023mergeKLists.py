__author__ = 'cwang'

from Leetcode.ListNode import ListNode
from Leetcode.ListNode import get_list
from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        currHeap = []
        head, l = None, None
        for li in lists:
            if li is not None:
                heappush(currHeap, (li.val, li))
        while currHeap:
            val, node = heappop(currHeap)
            newNode = ListNode(val)
            if node.next is not None:
                heappush(currHeap, (node.next.val, node.next))
            if not head:
                head, l = newNode, newNode
            else:
                l.next = newNode
                l = l.next
        return head

if __name__ == '__main__':
    sol = Solution()
    l1 = get_list([1, 2, 3])
    l2 = get_list([4, 5])
    l3 = get_list([])
    lists = [l1, l2, l3]
    result = sol.mergeKLists(lists)
    print(result)