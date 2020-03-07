class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.storage:
            n = self.storage[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.storage:
            self._remove(self.storage[key])   # Remove the Node indexed by key from the double linked list
        n = Node(key, value)
        self._add(n)                          # Add the new Node indexed by key into the tail of the double linked list
        self.storage[key] = n
        if len(self.storage) > self.capacity:
            n = self.head.next
            self._remove(n)                   # Remove the first item in the double linked list
            del self.storage[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# Test code below
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

print(our_cache.set(5, 5))
print(our_cache.set(6, 6))

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
