class Solution:
    def minimumHammingDistance(
        self, source: list[int], target: list[int], allowedSwaps: list[list[int]]
    ) -> int:
        parent = list(range(len(source)))

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        for first, second in allowedSwaps:
            root_first, root_second = find(first), find(second)
            if root_first != root_second:
                parent[root_first] = root_second
        available: dict[int, Counter[int]] = {}
        for index, value in enumerate(source):
            available.setdefault(find(index), Counter())[value] += 1
        distance = 0
        for index, value in enumerate(target):
            counts = available[find(index)]
            if counts[value]:
                counts[value] -= 1
            else:
                distance += 1
        return distance
