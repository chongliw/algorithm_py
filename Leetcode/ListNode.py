__author__ = 'cwang'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        node = self
        result = ''
        while node is not None:
            result += str(node.val)
            if node.next is not None: result += '->'
            node = node.next
        return result

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
    data = [2, 6]
    head = get_list(data)