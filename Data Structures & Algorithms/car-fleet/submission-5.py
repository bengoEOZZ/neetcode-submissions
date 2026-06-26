class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet =  [(position[i], speed[i]) for i in range(len(position))]
        fleet.sort(reverse=True)
        stack = []
        for pos, speed in fleet:
            time = (target-pos)/speed
            if (not stack) or (stack and time > stack[-1]):
                stack.append(time)
        return len(stack)