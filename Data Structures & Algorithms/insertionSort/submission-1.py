# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        for r in range(len(pairs)):
            l = r-1
            while l >= 0 and pairs[l+1].key < pairs[l].key:
                pairs[l], pairs[l+1] = pairs[l+1], pairs[l]
                l -= 1
            ans.append(pairs[:])
        return ans