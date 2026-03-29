class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #value is node
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    # left: LRC
    # right: MRC
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        rightmost = self.right.prev
        rightmost.next = node
        node.prev = rightmost

        self.right.prev = node
        node.next = self.right



        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # what should i do to remove the LRU? I cannot do it 
            # through self.remove() because I don't know which 
            # one is the node
            # should i directly manipulate the cache?
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
