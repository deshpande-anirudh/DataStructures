import random

class Node:
    def __init__(self, val=None, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

    def __repr__(self):
        return f"val={self.val}, \n\tnext={self.next}, \n\tdown={self.down}\n"


"""
-inf -> +inf
"""


class Skiplist:
    def __init__(self):
        self.level = [Node(float('-inf'), Node(float('inf')))]

    def __repr__(self):
        ret = []
        for i, level in enumerate(self.level):
            cur = level
            level_vals = [f'L{i}']
            while cur is not None:
                level_vals.append(str(cur.val))
                cur = cur.next
            ret.append(' > '.join(level_vals))
        return '\n'.join(reversed(ret))

    def search(self, num: int) -> bool:
        # print(self.level[-1])
        # print(num)
        node = self.level[-1]

        while node:
            while node.next.val < num:
                node = node.next

            if node.next.val == num:
                return True

            node = node.down
        return False

    def add(self, num: int) -> None:
        node = self.level[-1]
        stack = []

        while node:
            # print(node.val)
            while node.next.val < num:
                node = node.next

            stack.append(node)
            node = node.down

        down = None

        # print([(node.val, node.next.val, [node.down.val if node.down else None]) for node in stack])

        while stack:
            node = stack.pop()
            new_node = Node(num, node.next, down)
            node.next = new_node
            down = new_node

            if not random.choice([True, False]):
                break

        if not stack:
            head = Node(float('-inf'), Node(float('inf')), self.level[-1])
            self.level.append(head)

    def erase(self, num: int) -> bool:
        node = self.level[-1]
        is_deleted = False

        while node:
            while node.next.val < num:
                node = node.next

            if node.next.val == num:
                cur = node
                while cur.next.val == num:
                    cur = cur.next
                node.next = cur.next

            node = node.down

        while len(self.level) > 1 and self.level[-1].next.val == float('inf'):
            self.level.pop()

        return is_deleted


# Your Skiplist object will be instantiated and called as such:
obj = Skiplist()

obj.add(1)

print(obj)
print(obj.erase(1))
print(obj)
print(obj.search(1))
#print()

