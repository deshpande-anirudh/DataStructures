import random
from collections import Counter, deque


class WeightedRoundRobin:
    def __init__(self, server_to_weights):
        self.deque = deque()
        for server, weight in server_to_weights:
            self.deque.extend([server] * weight)

    def get_server(self):
        server = self.deque.popleft()
        self.deque.append(server)
        return server


if __name__ == "__main__":
    server_to_weights = [
        ("server_1", 60),
        ("server_2", 30),
        ("server_3", 10)
    ]

    server_count = Counter()
    w = WeightedRoundRobin(server_to_weights)
    for _ in range(1000000):
        server_count[w.get_server()] += 1

    print(server_count)

# Output:
# - Counter({'server_1': 600000, 'server_2': 300000, 'server_3': 100000})




