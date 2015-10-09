__author__ = 'cwang'

from Leetcode.ListNode import ListNode
from Leetcode.ListNode import get_list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val, addition = 0, 0
        l, head = None, None
        while l1 is not None or l2 is not None or addition:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            val = v1 + v2 + addition
            addition = val // 10
            if l is None:
                l = ListNode(val % 10)
                head = l
            else:
                l.next = ListNode(val % 10)
                l = l.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return head

if __name__ == '__main__':
    l1 = get_list([4, 3, 2])
    l2 = get_list([9, 1])
    sol = Solution()
    head = sol.addTwoNumbers(l1, l2)
    while head is not None:
        print(head.val)
        head = head.next