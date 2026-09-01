class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        carFleetSorted = [(position[i], speed[i]) for i in range(len(position))]
        carFleetSorted.sort(reverse=True)
        for pos, spd in carFleetSorted:
            # spd = distance / time
            # time = distance / spd
            time = (target-pos) / spd
            if not stack or (stack and time > stack[-1]):
                stack.append(time)
        return len(stack)