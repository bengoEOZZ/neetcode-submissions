class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars, fleet = [], []
        for i in range(len(position)):
            sortedCars.append([position[i], speed[i]])
        sortedCars.sort(reverse=True)
        for car in sortedCars:
            time = (target-car[0])/car[1]
            if not fleet:
                fleet.append(time)
            else:
                if time > fleet[-1]:
                    fleet.append(time)
        return len(fleet)