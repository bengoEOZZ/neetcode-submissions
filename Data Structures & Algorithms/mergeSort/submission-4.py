# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortH(pairs, 0, len(pairs)-1)
        return pairs
    
    def mergeSortH(self, arr, start, end):
        if (end-start+1) <= 1:
            return

        mid = (start+end) // 2

        self.mergeSortH(arr, start, mid)
        self.mergeSortH(arr, mid+1, end)

        self.merge(arr, start, mid, end)

    def merge(self, arr, start, mid, end):
        L = arr[start:mid+1]
        R = arr[mid+1:end+1]

        l, r = 0, 0
        curr = start

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
            curr += 1
            l += 1

        while r < len(R):
            arr[curr] = R[r]
            curr += 1
            r += 1