class Node:
    def __init__(self, key, val = None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.table = [Node(-1) for _ in range (10**4)]

    def _hash(self, key):
        return key % len(self.table)

    def put(self, key: int, value: int) -> None:
        hashKey = self._hash(key)
        node = self.table[hashKey]

        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next

        node.next = Node(key, value)

    def get(self, key: int) -> int:
        hashKey = self._hash(key)
        node = self.table[hashKey]

        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        hashKey = self._hash(key)
        node = self.table[hashKey]

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)