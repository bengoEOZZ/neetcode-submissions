class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carsSorted = [(position[i], speed[i]) for i in range(len(position))]
        carsSorted.sort(reverse=True)
        fleetTime = []
        for pos, speed in carsSorted:
            time = (target-pos)/speed
            if not fleetTime or time > fleetTime[-1]:
                fleetTime.append(time)
        return len(fleetTime)