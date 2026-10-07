class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        for a, b in zip(s1, s2):
            first, second = find(ord(a) - 97), find(ord(b) - 97)
            if first != second:
                small, large = min(first, second), max(first, second)
                parent[large] = small
        return "".join(chr(find(ord(char) - 97) + 97) for char in baseStr)
