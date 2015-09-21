__author__ = 'cwang'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currPos = head
        inDistinct = True
        init = False
        dhead, distLN = None, None
        while currPos is not None:
            currVal = currPos.val
            if currPos.next is None or currVal != currPos.next.val:
                if inDistinct:
                    if not init:
                        distLN = ListNode(currVal)
                        dhead = distLN
                        init = True
                    else:
                        newLN = ListNode(currVal)
                        distLN.next = newLN
                        distLN = newLN
                inDistinct = True
            elif inDistinct:
                inDistinct = False
            currPos = currPos.next
        return dhead