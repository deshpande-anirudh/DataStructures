class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.visited = []
        self.idx = -1
        self._push_left(root)

    def _push_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.idx < len(self.visited)

    def next(self) -> int:
        self.idx += 1
        if self.idx < len(self.visited):
            return self.visited[self.idx].val
        elif self.stack:
            node = self.stack.pop()
            self._push_left(node.right)
            self.visited.append(node)
            return node.val

    def hasPrev(self) -> bool:
        return self.idx > 0

    def prev(self) -> int:
        self.idx -= 1
        return self.visited[self.idx].val


root = TreeNode(7)
left = TreeNode(3)

root.left = left

right = TreeNode(15)
right.left = TreeNode(9)
right.right = TreeNode(20)

root.right = right

it = BSTIterator(root)

#"next","next","prev","next","hasNext","next","next","next","hasNext","hasPrev","prev","prev"
print(it.next())
print(it.next())
print(it.prev())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.prev())
print(it.prev())
