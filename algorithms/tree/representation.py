__author__ = 'cwang'

class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = newNode
        else:
            raise RuntimeError('Cannot insert when left node exists.')

    def insertRight(self, newNode):
        if self.right is None:
            self.right = newNode
        else:
            raise RuntimeError('Cannot insert when right node exists.')

    def getValue(self):
        return self.val

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

class BinaryTreeList(object):
    def __init__(self, tree):
        if len(tree) != 3:
            raise RuntimeError('Tree type must be of form list[root, left, right].')
        self.tree = tree

    def insertLeft(self, newNode):
        if not self.tree[1]:
            self.tree[1] = newNode
        else:
            raise RuntimeError('Cannot insert when left node exists.')

    def insertRight(self, newNode):
        if not self.tree[2]:
            self.tree[2] = newNode
        else:
            raise RuntimeError('Cannot insert when right node exists.')

    def getValue(self):
        return self.tree[0]

    def getRightChild(self):
        return self.tree[2]

    def getLeftChild(self):
        return self.tree[1]



if __name__ == '__main__':
    newTree = BinaryTreeList(['a', ['b', ['c', [], []], []], ['d', ['e', [], []], ['f', [], []]]])
    print(newTree.getLeftChild())

    tree = BinaryTree('a')
    tree.insertLeft(BinaryTree('b'))
    tree.left.insertLeft(BinaryTree('c'))
    tree.insertRight(BinaryTree('d'))
    tree.right.insertLeft(BinaryTree('e'))
    tree.right.insertRight(BinaryTree('f'))