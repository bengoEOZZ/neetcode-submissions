# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortH(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortH(self, arr, start, end):
        if (end-start+1) <= 1:
            return

        pivot = arr[end]
        l = start

        for r in range(start, end):
            if arr[r].key < pivot.key:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
        
        arr[end], arr[l] = arr[l], arr[end]

        self.quickSortH(arr, start, l-1)
        self.quickSortH(arr, l+1, end)