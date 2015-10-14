__author__ = 'cwang'

from Leetcode.ListNode import ListNode
from Leetcode.ListNode import get_list


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        st1 = head
        st2 = head.next
        previousNode = None
        while st1 is not None and st2 is not None:
            if previousNode is None:
                st1.next = st2.next
                st2.next = st1
                head = st2
            else:
                st1.next = st2.next
                st2.next = st1
                previousNode.next = st2
            previousNode = st1
            st1 = st1.next
            st2 = st1.next if st1 is not None else None
        return head

if __name__ == '__main__':
    sol = Solution()
    l = get_list([1, 3, 2, 1])
    result = sol.swapPairs(l)
    print(result)
