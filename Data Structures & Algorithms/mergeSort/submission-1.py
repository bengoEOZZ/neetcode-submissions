# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def mergeSortHelper(self, arr, l, r):
        if (r-l+1) <= 1:
            return

        m = (l+r) // 2
        
        self.mergeSortHelper(arr, l, m)
        self.mergeSortHelper(arr, m+1, r)

        self.merge(arr, l, m, r)

    def merge(self, arr, left, mid, right):
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]

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