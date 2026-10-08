class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        target = len(arr) // 2
        removed = 0
        for count, frequency in enumerate(
            sorted(Counter(arr).values(), reverse=True), 1
        ):
            removed += frequency
            if removed >= target:
                return count
        return len(Counter(arr))
