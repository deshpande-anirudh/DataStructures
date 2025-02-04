from bitarray import bitarray
import murmurhash


class BloomFilter:
    def __init__(self, num_seeds, size):
        self.num_seeds = num_seeds
        self.size = size
        self.bit_array = bitarray(size)

    def __contains__(self, content):
        for i in range(1, self.num_seeds+1):
            _hash = murmurhash.hash(content) % self.size
            if self.bit_array[_hash] != 1:
                return False
        return True

    def put(self, content):
        for i in range(1, self.num_seeds+1):
            _hash = murmurhash.hash(content) % self.size
            self.bit_array[_hash] = 1


if __name__ == "__main__":
    bloom_filter = BloomFilter(5, 100)

    bloom_filter.put('Banana')
    bloom_filter.put('Apple')

    print("Banana" in bloom_filter)
    print("Apple" in bloom_filter)
    print("Peach" in bloom_filter)
