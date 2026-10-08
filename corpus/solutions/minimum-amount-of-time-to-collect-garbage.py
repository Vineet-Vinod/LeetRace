class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        prefix = [0]
        for duration in travel:
            prefix.append(prefix[-1] + duration)
        total = sum(map(len, garbage))
        for kind in "MPG":
            houses = [index for index, house in enumerate(garbage) if kind in house]
            if houses:
                total += prefix[houses[-1]]
        return total
