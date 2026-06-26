class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMapS, hashMapT = {}, {}
        for i in range(len(s)):
            hashMapS[s[i]] = hashMapS.get(s[i], 0) + 1
            hashMapT[t[i]] = hashMapT.get(t[i], 0) + 1
        
        for c in s:
            if c not in hashMapT:
                return False
            if hashMapS[c] != hashMapT[c]:
                return False
        return True