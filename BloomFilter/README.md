# Bloom Filter Implementation

This repository contains a simple implementation of a **Bloom Filter**, a probabilistic data structure used to test whether an element is a member of a set. It is space-efficient and allows for fast membership queries, but with a small probability of false positives.

## Features
- **Space Efficiency**: Uses a bit array to store membership information.
- **Fast Lookups**: Provides constant-time complexity for both insertion and membership queries.
- **Configurable**: Allows customization of the number of hash functions (`num_seeds`) and the size of the bit array (`size`).

## Dependencies
- `bitarray`: A library for handling bit arrays in Python.
- `murmurhash`: A non-cryptographic hash function suitable for generating hash values.

Install the dependencies using:
```bash
pip install bitarray murmurhash
```

## Usage

### Initialization
To create a Bloom Filter, specify the number of hash functions (`num_seeds`) and the size of the bit array (`size`):
```python
from bloom_filter import BloomFilter

bloom_filter = BloomFilter(num_seeds=5, size=100)
```

### Inserting Elements
Use the `put` method to add elements to the Bloom Filter:
```python
bloom_filter.put('Banana')
bloom_filter.put('Apple')
```

### Checking Membership
Use the `in` keyword to check if an element is likely in the set:
```python
print("Banana" in bloom_filter)  # Output: True
print("Apple" in bloom_filter)   # Output: True
print("Peach" in bloom_filter)   # Output: False (or True, if a false positive occurs)
```

### Example
```python
if __name__ == "__main__":
    bloom_filter = BloomFilter(5, 100)

    bloom_filter.put('Banana')
    bloom_filter.put('Apple')

    print("Banana" in bloom_filter)  # True
    print("Apple" in bloom_filter)   # True
    print("Peach" in bloom_filter)   # False (or True, if a false positive occurs)
```

## How It Works
1. **Hash Functions**: The Bloom Filter uses multiple hash functions (determined by `num_seeds`) to map each element to several positions in the bit array.
2. **Insertion**: When an element is added, the corresponding bits in the bit array are set to `1`.
3. **Membership Query**: To check if an element is in the set, the Bloom Filter checks if all the corresponding bits are `1`. If any bit is `0`, the element is definitely not in the set. If all bits are `1`, the element is probably in the set (with a small chance of a false positive).

## Limitations
- **False Positives**: The Bloom Filter may incorrectly report that an element is in the set when it is not. The probability of false positives can be reduced by increasing the size of the bit array or the number of hash functions.
- **No Deletion**: This implementation does not support deleting elements from the Bloom Filter.

## Applications
- **Spell Checkers**: Quickly check if a word is in a dictionary.
- **Duplicate Detection**: Identify duplicate entries in a dataset.
- **Network Routers**: Track seen packets to avoid reprocessing.

## License
This project is open-source and available under the [MIT License](LICENSE).

---