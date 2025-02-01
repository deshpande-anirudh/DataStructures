### **Simple Requirements for the LRU Cache**

1. **Capacity**  
   - The cache has a fixed capacity.  
   - If a new item is added when the cache is full, the least recently used (LRU) item should be removed.

2. **Operations**
   - **`put(key, value)`**:  
     - Inserts or updates the value of a key in the cache.  
     - If the key already exists, update its value and move it to the most recently used position.  
     - If the cache is full, evict the LRU key before adding the new one.

   - **`get(key)`**:  
     - Retrieves the value of a key.  
     - If the key is found, move it to the most recently used position and return the value.  
     - If the key is not found, return `-1`.

3. **Eviction Policy**  
   - The least recently used item is always removed first when the cache is full.

4. **Performance Expectations**  
   - Both `get()` and `put()` operations should be efficient, ideally with a time complexity of O(1).  
