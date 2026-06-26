class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.table = [Node(-1) for _ in range(10**4)]

    def _hash(self, key):
        return key % len(self.table)

    def add(self, key: int) -> None:
        hashKey = self._hash(key)
        node = self.table[hashKey]

        while node.next:
            if node.next.key == key:
                return
            node = node.next
        
        node.next = Node(key)

    def remove(self, key: int) -> None:
        hashKey = self._hash(key)
        node = self.table[hashKey]

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def contains(self, key: int) -> bool:
        hashKey = self._hash(key)
        node = self.table[hashKey]

        while node:
            if node.key == key:
                return True
            node = node.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)