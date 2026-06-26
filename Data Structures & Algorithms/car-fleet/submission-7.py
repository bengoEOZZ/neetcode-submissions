class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [(position[i], speed[i]) for i in range(len(position))]
        fleet.sort(reverse=True)
        stack = []
        for pos, spd in fleet:
            time = (target-pos)/spd
            if not stack or (stack and time > stack[-1]):
                stack.append(time)
        return len(stack)