class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        if len(s) - k + 1 < needed:
            return False
        seen: set[int] = set()
        mask = needed - 1
        value = 0
        for i, char in enumerate(s):
            value = ((value << 1) & mask) | (char == "1")
            if i >= k - 1:
                seen.add(value)
                if len(seen) == needed:
                    return True
        return False
