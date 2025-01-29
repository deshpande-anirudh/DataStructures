from collections import defaultdict, deque

class LFUCache:
    def __init__(self, capacity):
        # Initialize the cache with a given capacity
        self.capacity = capacity
        self.size = 0
        # Track the minimum frequency for efficient eviction
        self.min_freq = float('inf')
        # Maps keys to values
        self.key_value = {}
        # Maps keys to their frequencies
        self.key_freq = {}
        # Maps frequencies to a deque of keys for efficient access and eviction
        self.freq_keys = defaultdict(deque)

    def _evict(self):
        # Evict the least frequently used key
        min_key = self.freq_keys[self.min_freq].popleft()
        # Remove the key from key-value and key-frequency mappings
        del self.key_value[min_key]
        del self.key_freq[min_key]

        # No need to update self.min_freq here; it will be updated when needed.

    def _change_frequency(self, key):
        if key in self.key_freq:
            # Get the current frequency of the key
            old_freq = self.key_freq[key]
            # Remove the key from its current frequency bucket
            self.freq_keys[old_freq].remove(key)
            # Increase the frequency and move the key to the new bucket
            self.freq_keys[old_freq + 1].append(key)
            # Update the frequency of the key
            self.key_freq[key] = old_freq + 1

            # Update the minimum frequency if the old frequency bucket is empty
            if self.min_freq == old_freq and not self.freq_keys[old_freq]:
                # The old_freq + 1 bucket already exists as it was updated above
                self.min_freq = old_freq + 1
        else:
            # If key is new, set its frequency to 1
            self.key_freq[key] = 1
            self.freq_keys[1].append(key)
            # Reset min_freq to 1 for new keys
            self.min_freq = 1

    def put(self, key, value):
        # If key already exists, update its value and frequency
        if key in self.key_value:
            self.key_value[key] = value
            self._change_frequency(key)
        else:
            # If capacity is reached, evict the least frequently used key
            if self.capacity <= self.size:
                self._evict()

            # Add the new key-value pair
            self.key_value[key] = value
            self._change_frequency(key)
            self.size += 1

    def get(self, key):
        # Return -1 if the key is not found
        if key not in self.key_value:
            return -1
        # Update the frequency of the accessed key
        value = self.key_value[key]
        self._change_frequency(key)
        return value
