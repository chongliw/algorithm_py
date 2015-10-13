__author__ = 'cwang'

from Leetcode.ListNode import get_list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def remove(head, st, n):
    if st is None:
        remove.counter = -1
    else:
        remove(head, st.next, n)
    remove.counter += 1
    if remove.counter == n - 1:
        remove.nextNode = st
    if remove.counter == n + 1:
        st.next = remove.nextNode
    if st == head and remove.counter == n:
        return False
    return True

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        st = head
        if not remove(head, st, n):
            return head.next
        else:
            return head

if __name__ == '__main__':
    data = [2, 3, 4, 5]
    head = get_list(data)
    sol = Solution()
    result = sol.removeNthFromEnd(head, 4)
    print(result)