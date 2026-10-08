class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        for a, b in pairs:
            root_a, root_b = find(a), find(b)
            parent[root_a] = root_b
        groups: Dict[int, List[int]] = defaultdict(list)
        for index, char in enumerate(s):
            groups[find(index)].append(index)
        result = list(s)
        for indices in groups.values():
            letters = sorted(s[index] for index in indices)
            for index, char in zip(sorted(indices), letters):
                result[index] = char
        return "".join(result)
