__author__ = 'cwang'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def get_list(data):
    head, tail = None, None
    for num in data:
        newNode = ListNode(num)
        if head is not None:
            tail.next = newNode
            tail = newNode
        else:
            head = newNode
            tail = head
    return head

if __name__ == '__main__':
    data = [2, 3, 4, 3]
    head = get_list(data)
    while head is not None:
        print(head.val)
        head = head.next
