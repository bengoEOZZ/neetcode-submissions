class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        alpha = "abcdefghijklmonpqrstuvwxyz"
        for s in strs:
            count = [0]*26
            for c in s:
                count[alpha.index(c)] += 1
            count = tuple(count)
            if count not in res:
                res[count] = [s]
            else:
                res[count].append(s)
        return list(res.values())