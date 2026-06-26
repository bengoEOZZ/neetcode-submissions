class Solution:
    def isValid(self, s: str) -> bool:
        paren = {")": "(", "]": "[", "}": "{"}
        stack = []
        for b in s:
            if b in paren: # If Open bracket
                if stack and stack[-1] == paren[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False