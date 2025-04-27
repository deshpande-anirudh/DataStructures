class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTInOrderIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0


root = TreeNode(10)

left = TreeNode(5)
left.left = TreeNode(2)
left.right = TreeNode(8)

root.left = left

right = TreeNode(18)
right.left = TreeNode(12)
right.right = TreeNode(20)

root.right = right

it = BSTInOrderIterator(root)

while it.hasNext():
    print(it.next())
