class Solution:
    def maximumPoints(self, enemyEnergies: list[int], currentEnergy: int) -> int:
        minimum = min(enemyEnergies)
        if currentEnergy < minimum:
            return 0
        return (currentEnergy + sum(enemyEnergies) - minimum) // minimum
