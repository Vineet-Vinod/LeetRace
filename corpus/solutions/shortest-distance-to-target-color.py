class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        positions = {c: [] for c in (1, 2, 3)}
        for i, c in enumerate(colors):
            positions[c].append(i)
        import bisect

        ans = []
        for i, c in queries:
            arr = positions[c]
            j = bisect.bisect_left(arr, i)
            choices = []
            if j < len(arr):
                choices.append(arr[j] - i)
            if j:
                choices.append(i - arr[j - 1])
            ans.append(min(choices) if choices else -1)
        return ans
