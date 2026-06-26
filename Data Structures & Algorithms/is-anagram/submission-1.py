class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS, hashMapT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashMapS:
                hashMapS[s[i]] = 1
            else:
                hashMapS[s[i]] += 1
            if t[i] not in hashMapT:
                hashMapT[t[i]] = 1
            else:
                hashMapT[t[i]] += 1
        return hashMapS == hashMapT