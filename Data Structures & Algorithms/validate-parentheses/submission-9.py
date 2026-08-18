class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}':'{', ')':'(', ']':'['}
        for br in s:
            if br in closeToOpen:
                if not stack or stack.pop() != closeToOpen[br]:
                    return False
            else:
                stack.append(br)
        return True if not stack else False