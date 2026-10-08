class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        odd_counts = sum(count % 2 for count in Counter(s).values())
        return odd_counts <= k <= len(s)
