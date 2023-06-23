"""
Design a data structure that follows the constraints of a Least 
Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, 
otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

"""


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        node.prev.next = node.next.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            self.move_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.move_to_head(node)
        else:
            if len(self.hash) == self.capacity:
                node = self.pop_tail()
                del self.hash[node.key]

            node = Node(key, value)
            self.hash[key] = node
            self.add_node(node)