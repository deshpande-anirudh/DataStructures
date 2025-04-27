import random

import random

class Node:
    def __init__(self, val=None, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'), Node(float('inf')))
        self.levels = [self.head]

    def __repr__(self):
        levels = []
        for i, level in enumerate(reversed(self.levels)):  # Start from the highest level
            nodes = []
            node = level
            while node:
                nodes.append(str(node.val))
                node = node.next
            levels.append(f"L{i}: {' → '.join(nodes)}")
        return '\n'.join(levels)

    def search(self, target: int) -> bool:
        node = self.levels[-1]
        while node:
            while node.next.val < target:
                node = node.next
            if node.next.val == target:
                return True
            node = node.down
        return False

    def add(self, num: int) -> None:
        node = self.levels[-1]
        stack = []
        while node:
            while node.next.val < num:
                node = node.next
            stack.append(node)
            node = node.down

        down = None

        while stack:
            top = stack.pop()
            new_node = Node(num, top.next, down)
            top.next = new_node
            down = new_node

            if not random.choice([True, False]):
                break

        if not stack:
            head = Node(float('-inf'), Node(float('inf')), self.levels[-1])
            self.levels.append(head)

    def erase(self, num: int) -> bool:
        node = self.levels[-1]
        is_deleted = False

        while node:
            while node.next.val < num:
                node = node.next
            if node.next.val == num:
                is_deleted = True
                node.next = node.next.next
            node = node.down

        while len(self.levels) > 0 and self.levels[-1].next.val == float('inf'):
            self.levels.pop()

        return is_deleted


obj = Skiplist()
for i in range(1, 31):
    obj.add(i)
print(obj)
print(obj.search(29))
print(obj.erase(29))
print(obj)
print(obj.search(29))
obj.add(29)
print(obj.search(29))
print(obj)


