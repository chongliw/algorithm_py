__author__ = 'cwang'

from queue import Queue

class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None

def get_tree(data):
    root, curr_node = None, None
    nodes = Queue()
    left = False
    for num in data:
        if left:
            curr_node = nodes.get()
        if num is not None:
            newNode = BinaryTreeNode(num)
            nodes.put(newNode)
            if root is None:
                root = newNode
            else:
                if left:
                    curr_node.left = newNode
                else:
                    curr_node.right = newNode
        left = not left

    return root

if __name__ == '__main__':
    data = [1, 2, 3, None, None, 4, 5]
    root = get_tree(data)
    print(root.right.right.val)