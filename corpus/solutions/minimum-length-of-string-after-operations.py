class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if count % 2 else 2 for count in Counter(s).values())
