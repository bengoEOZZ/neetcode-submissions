class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        mostFrequent = []
        sortedHashMap = []
        for num, count in hashMap.items():
            sortedHashMap.append((count, num))
        sortedHashMap.sort(reverse=True)
        for i in range(k):
            mostFrequent.append(sortedHashMap[i][1])
        return mostFrequent