# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, arr, l, r):
        if l >= r:
            return arr

        m = (l+r) // 2

        self.mergeSortHelper(arr, l, m)
        self.mergeSortHelper(arr, m+1, r)

        self.merge(arr, l, m, r)

        return arr

    def merge(self, arr, left, m, right):
        L = arr[left:m+1]
        R = arr[m+1:right+1]

        l, r = 0, 0
        curr = left

        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                arr[curr] = L[l]
                l += 1
            else:
                arr[curr] = R[r]
                r += 1
            curr += 1

        while l < len(L):
            arr[curr] = L[l]
            l += 1
            curr += 1

        while r < len(R):
            arr[curr] = R[r]
            r += 1
            curr += 1