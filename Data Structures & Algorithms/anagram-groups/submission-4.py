class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for s in strs:
            count = [0]*26
            for c in s:
                count[alpha.index(c)] += 1
            count = tuple(count)
            if count not in hashMap:
                hashMap[count] = [s]
            else:
                hashMap[count].append(s)
        return hashMap.values()