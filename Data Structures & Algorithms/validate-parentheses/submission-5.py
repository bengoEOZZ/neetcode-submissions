class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")": "(", "}": "{", "]": "["}
        stack = []
        for b in s:
            if b in parentheses:
                if stack and parentheses[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False