# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, arr, left, right):
        if (right-left+1) <= 1:
            return

        pivot = arr[right]
        l = left

        for r in range(left, right):
            if arr[r].key < pivot.key:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
        
        arr[right], arr[l] = arr[l], pivot

        self.quickSortHelper(arr, left, l-1)
        self.quickSortHelper(arr, l+1, right)