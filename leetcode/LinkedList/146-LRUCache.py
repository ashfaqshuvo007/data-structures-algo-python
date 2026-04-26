class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map key-> Node

        #left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    #Remove from the list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert at the right (MRU)
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val

        return -1 
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Delete from the list and delete the LRU from hashmap
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))  # returns 1
    lru_cache.put(3, 3)      # evicts key 2
    print(lru_cache.get(2))  # returns -1 (not found)
    lru_cache.put(4, 4)      # evicts key 3
    print(lru_cache.get(3))  # returns -1 (not found)
    print(lru_cache.get(4))  # returns 4