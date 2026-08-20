class LRUCache:

    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail
        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark as recently used
        self.remove(node)
        self.add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            # Update value
            node.value = value

            # Mark as recently used
            self.remove(node)
            self.add_to_front(node)

        else:
            node = self.Node(key, value)
            self.cache[key] = node
            self.add_to_front(node)

            # Capacity exceeded
            if len(self.cache) > self.capacity:
                lru = self.tail.prev

                self.remove(lru)
                del self.cache[lru.key]