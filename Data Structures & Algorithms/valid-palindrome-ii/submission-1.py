class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            l, r = left, right
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return True if (isPalindrome(l+1, r) or isPalindrome(l, r-1)) else False
            l += 1
            r -= 1
        return True