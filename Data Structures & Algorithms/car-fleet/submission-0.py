class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        fleet = 0
        curr_fleet_time = 0

        for pos, spe in cars:
            time = ((target-pos)/spe)
            if time > curr_fleet_time:
                fleet += 1
                curr_fleet_time = time
        return fleet

