class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        mostFrequent = []
        frequencies = list(hashMap.values())
        frequencies.sort(reverse=True)
        frequencies = frequencies[:k]
        for e in hashMap:
            if hashMap[e] in frequencies:
                mostFrequent.append(e)
        return mostFrequent