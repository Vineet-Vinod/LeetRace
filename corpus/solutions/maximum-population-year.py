class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = [0] * 101
        for birth, death in logs:
            events[birth - 1950] += 1
            events[death - 1950] -= 1
        population = 0
        best_population = -1
        best_year = 1950
        for offset, change in enumerate(events[:-1]):
            population += change
            if population > best_population:
                best_population = population
                best_year = 1950 + offset
        return best_year
