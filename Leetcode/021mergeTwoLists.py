__author__ = 'cwang'

import Leetcode.ListNode as LN
from Leetcode.ListNode import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, l = None, None
        if l1 is None: return l2
        if l2 is None: return l1
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                newNode = ListNode(l1.val)
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                l2 = l2.next
            if head is None:
                head, l = newNode, newNode
            else:
                l.next = newNode
                l = l.next
        if l1 is None:
            l.next = l2
        else:
            l.next = l1
        return head

if __name__ == '__main__':
    ls1 = [2]
    ls2 = [1]
    l1 = LN.get_list(ls1)
    print(l1)
    l2 = LN.get_list(ls2)
    print(l2)
    sol = Solution()
    result = sol.mergeTwoLists(l1, l2)
    print(result)