The goal is to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 

**We want the `get()` operation to be O(1).** 
Data structure choices:
1. If we use an array for the cache, `get()` operation will take O(n) as in the worst case, we need to go through the whole array to find it or say that it does not exist. 
2. If we use a dictionary (hash table), `get()` operation will take O(1).

**We also want the `set()` operation to be O(1).** 
Data structure choices:
Normally, the `set()` operation will take O(1) whether we use an array or a dictionary. 
However, when the cache memory reaches its limit, we need to remove the least recently used entry. To do that, we need to keep track of the usage recency for each entry. A dictionary is a good data structure for that purpose: we create a dictionary so that anytime when there is a `set()` or `get()` operation we update the time for that entry. Still it will take O(n) to go through the dictionary and find the least recently used entry and delete it from the cache.
1. If we use an array for the cache, the deletion will take O(n) and add the new entry will take O(1) as we know the position.
2. If we use a dictionary, the deletion and addition will take O(1).
So the worst case for `set()` operation runtime is O(n) but the average case is O(1)

Therefore, dictionary is a good data structure for the cache and the recency tracking. 

**Space complexity** is 0(n) for n is the cache capcity.