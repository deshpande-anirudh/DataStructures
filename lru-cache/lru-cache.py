
class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"(key: {self.key}: val: {self.val})\n"


class DoublyLinkedList:
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity

    def add_start(self, node):
        _next = self.start.next
        self.start.next = node
        node.prev = self.start
        node.next = _next
        _next.prev = node
        self._size += 1

    def remove(self, node):
        _prev, _next = node.prev, node.next
        _prev.next = _next
        _next.prev = _prev
        self._size -= 1


"""
Idea: LRU at the end of the queue
"""
class LruCache:
    def __init__(self, capacity):
        self.linked_list = DoublyLinkedList(capacity)
        self.key_to_node = {}

    def put(self, key, value):
        if self.linked_list.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.linked_list.remove(node)
            self.linked_list.add_start(node)
        else:
            node = Node(key, value)
            if self.linked_list.size >= self.linked_list.capacity:
                to_be_removed = self.linked_list.end.prev
                self.linked_list.remove(to_be_removed)
                del self.key_to_node[to_be_removed.key]

            self.linked_list.add_start(node)
            self.key_to_node[key] = node

    def get(self, key):
        if self.linked_list.size == 0 or key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.linked_list.remove(node)
        self.linked_list.add_start(node)

        return node.val

    def __repr__(self):
        return ''.join(str(node) for _, node in self.key_to_node.items())


cache = LruCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.get(1)
print(cache)

cache.put(4, 4)
cache.put(5, 5)
print()
print(cache)




