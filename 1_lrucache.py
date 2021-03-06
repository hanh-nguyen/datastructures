import datetime
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity <= 0:
            print("Capacity should be greater than 0. Setting to 1")
        self.capacity = capacity if capacity > 0 else 1
        self.storage = dict() # store items
        self.recency = dict() # track usage time

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.storage:
            self.recency[key] = datetime.datetime.now()
            return self.storage[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.storage:
            if len(self.storage) >= self.capacity:
                least_used = min(self.recency, key=self.recency.get)
                del self.storage[least_used]
                del self.recency[least_used]
            self.storage[key] = value
            self.recency[key] = datetime.datetime.now()

# Test 1
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test 2
our_cache = LRU_Cache(1)
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # return 2

# Test 3
our_cache = LRU_Cache(0)      # Capacity should be greater than 0. Setting to 1
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # return 2