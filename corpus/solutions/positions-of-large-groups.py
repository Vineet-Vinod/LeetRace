class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        groups: list[list[int]] = []
        start = 0
        while start < len(s):
            end = start
            while end + 1 < len(s) and s[end + 1] == s[start]:
                end += 1
            if end - start + 1 >= 3:
                groups.append([start, end])
            start = end + 1
        return groups
