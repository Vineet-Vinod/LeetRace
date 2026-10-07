class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for value in arr1:
            text = str(value)
            for end in range(1, len(text) + 1):
                prefixes.add(text[:end])
        best = 0
        for value in arr2:
            text = str(value)
            for end in range(1, len(text) + 1):
                if text[:end] in prefixes:
                    best = max(best, end)
        return best
