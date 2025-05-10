class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    Node.head = Node(-1,-1)
    Node.tail = Node(-1,-1)

    map = {}

    def __init__(self, capacity: int):
        

    def get(self, key):
        

    def put(self, key, value):
        