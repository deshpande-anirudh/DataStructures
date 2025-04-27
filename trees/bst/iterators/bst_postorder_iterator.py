class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTPostOrderIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
        self.prev = None

    def _push_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        while self.stack:
            node = self.stack[-1]
            if node.right and node.right != self.prev:
                self._push_left(node.right)
            else:
                self.prev = self.stack.pop()
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

it = BSTPostOrderIterator(root)

while it.hasNext():
    print(it.next())
