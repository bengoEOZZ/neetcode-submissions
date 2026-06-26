from typing import List

class MinHeap:
    def __init__(self):
        self.heap = [0] # Initialize heap with a dummy value at index 0, For Ex: [0, _, _, _].

    def push(self, val: int) -> None:
        """
        Pushes a value onto the heap.
        """
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1) # Bubble-up pushed value in the tree until valid

    def pop(self) -> int:
        """
        Pops the smallest value off the heap.
        """
        # Empty heap — nothing to pop
        if len(self.heap) <= 1: # Just dummy value
            return -1

        # Only one real element — just pop it directly
        if len(self.heap) == 2: # Just dummy value + root
            return self.heap.pop()

        # Save the minimum (root) to return it
        root = self.heap[1]

        # Move the last element to replace the root, then pop the last element.
        self.heap[1] = self.heap.pop()

        # Bubble-down the last element (currently at root) in the tree until valid
        self._bubble_down(1)

        return root

    def top(self) -> int:
        """
        Returns the smallest value without removing it.
        """
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        """
        Transforms a list into a valid heap in-place.
        """
        # Prepend the dummy 0 so the 1-based indexing math still works
        self.heap = [0] + nums

        # Starts from the last non-leaf node (up to the root) and bubble-downs each one.
        # Leaf nodes (indices > len//2) are skipped entirely.
        for i in range(len(self.heap) // 2, 0, -1):
            self._bubble_down(i)

    def _bubble_up(self, index: int) -> None:
        """
        Restores the order property after a push by moving a node UP the tree.

        Starting at the given index, repeatedly compare the node with its
        parent (at index // 2). If the node is smaller than its parent, swap
        them and continue upward. Stop when we reach the root (index 1) or
        the node is >= its parent (order property satisfied).
        """
        parent = index // 2
        while index > 1 and self.heap[index] < self.heap[parent]:
            # Node is smaller than its parent — swap to move it up
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]

            # Move up the tree and recalculate new position
            index = parent
            parent = index // 2

    def _bubble_down(self, index: int) -> None:
        """
        Restores the order property after a pop or during heapify by moving a node DOWN the tree.

        Starting at the given index, compare the node with its children.
        Swap with the SMALLER child (so the smaller child becomes the new
        parent, keeping the min-heap property). Repeat until the node is
        smaller than both children, or there are no children left.
        """
        child = 2 * index  # Start with the left child, right child may not exist

        # While the index of the left child is valid (inside the tree)
        while child < len(self.heap):
            # If a right child exists AND is smaller than the left child, choose right child for swapping
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1

            # If current node is already <= the smallest child, heap order is satisfied — stop here
            if self.heap[index] <= self.heap[child]:
                break

            # Swap current node down with the smaller child
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]

            # Move down the tree and recalculate new position
            index = child
            child = 2 * index 