class Solution:
    def isValid(self, s: str) -> bool:
        paran = {')':'(', ']':'[', '}':'{'}
        stack = []
        for b in s:
            if b in paran:
                if stack and stack[-1] == paran[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
