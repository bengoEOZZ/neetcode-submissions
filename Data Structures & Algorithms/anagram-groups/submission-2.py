class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            alpha = "abcdefghijklmnopqrstuvwxyz"
            count = [0]*26
            for c in s:
                count[alpha.index(c)] += 1
            count = tuple(count)
            if count not in hashMap:
                hashMap[count] = [s]
            else:
                hashMap[count].append(s)
        return hashMap.values()