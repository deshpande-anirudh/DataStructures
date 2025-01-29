### **Simple Requirements for the LFU Cache**

1. **Capacity**  
   - The cache has a fixed capacity.  
   - If a new item is added when the cache is full, the least frequently used (LFU) item should be removed.  
   - If multiple items have the same frequency, the least recently used (LRU) among them is removed.

2. **Operations**
   - **`put(key, value)`**:  
     - Inserts or updates the value of a key in the cache.  
     - If the key already exists, update its value and increase its frequency.  
     - If the cache is full, evict the LFU key before adding the new one.

   - **`get(key)`**:  
     - Retrieves the value of a key.  
     - If the key is found, increase its frequency and return the value.  
     - If the key is not found, return `-1`.

3. **Frequency Tracking**
   - Maintain the number of times each key is accessed.  
   - Keep track of the minimum frequency for efficient eviction.

4. **Performance Expectations**  
   - Both `get()` and `put()` operations should be efficient.  
   - The goal is to keep operations as close to O(1) time complexity as possible.
