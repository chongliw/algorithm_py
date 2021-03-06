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
        dhead, distLN = None, None
        while currPos is not None:
            currVal = currPos.val
            if currPos.next is None or currVal != currPos.next.val:
                if inDistinct:
                    if dhead:
                        newLN = ListNode(currVal)
                        distLN.next = newLN
                        distLN = newLN
                    else:
                        distLN = ListNode(currVal)
                        dhead = distLN
                inDistinct = True
            elif inDistinct:
                inDistinct = False
            currPos = currPos.next
        return dhead