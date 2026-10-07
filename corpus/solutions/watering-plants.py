class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0
        for index, need in enumerate(plants):
            if water < need:
                steps += 2 * index + 1
                water = capacity
            else:
                steps += 1
            water -= need
        return steps
