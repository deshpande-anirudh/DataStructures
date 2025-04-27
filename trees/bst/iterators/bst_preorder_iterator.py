class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTPreOrderIterator:
    def __init__(self, root):
        self.stack = [root]

    def next(self):
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)
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

it = BSTPreOrderIterator(root)

while it.hasNext():
    print(it.next())
