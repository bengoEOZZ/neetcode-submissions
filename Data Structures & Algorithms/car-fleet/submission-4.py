class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i])for i in range(len(position))]
        cars.sort(reverse=True)
        fleetTimes = []
        print(cars)
        for pos, spd in cars:
            time = (target-pos)/spd
            if not fleetTimes or (fleetTimes and time > fleetTimes[-1]):
                fleetTimes.append(time)
        return len(fleetTimes)