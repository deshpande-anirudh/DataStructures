import random
from collections import Counter


class WeightedRoundRobin:
    def __init__(self, server_to_weights):
        self.servers = [server_to_weight[0] for server_to_weight in server_to_weights]
        self.weights = [server_to_weight[1] for server_to_weight in server_to_weights]

    def get_server(self):
        return random.choices(self.servers, self.weights, k=1)[0]


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
# - Counter({'server_1': 600109, 'server_2': 299951, 'server_3': 99940})




