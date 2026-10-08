class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def remains_subsequence(count: int) -> bool:
            removed = set(removable[:count])
            position = 0
            for index, char in enumerate(s):
                if index not in removed and position < len(p) and char == p[position]:
                    position += 1
            return position == len(p)

        low, high = 0, len(removable)
        while low < high:
            middle = (low + high + 1) // 2
            if remains_subsequence(middle):
                low = middle
            else:
                high = middle - 1
        return low
